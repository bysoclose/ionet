import asyncio
from iointel import Agent, Workflow
from agents_config import agent_task_mapping, translations
from dotenv import load_dotenv
import os
import json

load_dotenv()
api_key = os.environ["OPENAI_API_KEY"]

async def run_workflow(user_input, selected_agent_name, current_language):
    agent_config = agent_task_mapping.get(selected_agent_name, agent_task_mapping["Custom Agent"])
    task_name = agent_config["task"]
    args = agent_config["args"].copy()
    instructions = translations[current_language]["agent_descriptions"][selected_agent_name]

    agent = Agent(
        name=selected_agent_name,
        instructions=instructions,
        model="meta-llama/Llama-3.3-70B-Instruct",
        api_key=api_key,
        base_url="https://api.intelligence.io.solutions/api/v1"
    )

    input_text = user_input
    if task_name == "translate_text":
        input_lower = input_text.lower()
        if "çevir" in input_lower or "translate to" in input_lower or "übersetzen" in input_lower:
            parts = input_text.split(":", 1) if ":" in input_text else input_text.split(" to ", 1)
            if len(parts) > 1:
                target_lang = parts[0].strip().lower()
                input_text = parts[1].strip()
                lang_map = {
                    "ingilizce": "en", "english": "en",
                    "fransızca": "fr", "french": "fr",
                    "ispanyolca": "es", "spanish": "es",
                    "almanca": "de", "german": "de"
                }
                args["target_language"] = lang_map.get(target_lang, "en")

    workflow = Workflow(objective=input_text, client_mode=False)

    try:
        if task_name == "summarize_text":
            result = await workflow.summarize_text(**args, agents=[agent]).run_tasks()
        elif task_name == "sentiment":
            result = await workflow.sentiment(**args, agents=[agent]).run_tasks()
        elif task_name == "extract_categorized_entities":
            result = await workflow.extract_categorized_entities(**args, agents=[agent]).run_tasks()
        elif task_name == "custom":
            args["objective"] = input_text
            args["instructions"] = instructions
            result = await workflow.custom(**args, agents=[agent]).run_tasks()
            # Custom görevi için sonucu kontrol et
            if isinstance(result, dict) and "results" in result and "custom" in result["results"]:
                return result["results"]["custom"]
            elif isinstance(result, dict) and "message" in result:
                return result["message"]  # API'nin döndürdüğü mesajı al
            else:
                return str(result)  # Ham sonucu döndür
        elif task_name == "moderation":
            result = await workflow.moderation(**args, agents=[agent]).run_tasks()
        elif task_name == "classify":
            result = await workflow.classify(**args, agents=[agent]).run_tasks()
        elif task_name == "translate_text":
            result = await workflow.translate_text(**args, agents=[agent]).run_tasks()
        else:
            raise ValueError(f"Unknown task: {task_name}")
        
        # Diğer görevler için standart sonuç işleme
        if isinstance(result, dict) and "results" in result and task_name in result["results"]:
            return result["results"][task_name]
        else:
            return str(result)  # Beklenmeyen formatta ise ham sonucu döndür

    except Exception as e:
        return f"Error: {str(e)}"