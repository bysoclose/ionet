import os
import logging
from agents_config import agent_task_mapping
from googletrans import Translator

logger = logging.getLogger(__name__)

async def run_workflow(user_input, selected_agent_name, current_language):
    logger.debug("Simulating API response for testing")
    if selected_agent_name == "Summary Agent":
        clean_input = user_input.replace("Summarize:", "").replace("Özetle:", "").strip()
        return {
            "summary": clean_input,
            "key_points": [word.capitalize() for word in clean_input.split()[:3]]
        }
    elif selected_agent_name == "Sentiment Analysis Agent":
        positive_keywords = ["love", "sevdim", "harika", "mükemmel", "güzel"]
        return "positive" if any(kw in user_input.lower() for kw in positive_keywords) else "neutral"
    elif selected_agent_name == "Named Entity Recognizer":
        entities = {"person": [], "organization": [], "location": []}
        if "Apple" in user_input:
            entities["organization"].append("Apple")
        if "California" in user_input:
            entities["location"].append("California")
        return {"entities": entities}
    elif selected_agent_name == "Moderation Agent":
        inappropriate_keywords = ["kötü", "pislik", "göt", "orospu", "harmful"]
        return {
            "hate_speech": 0.5 if any(kw in user_input.lower() for kw in inappropriate_keywords) else 0.0,
            "harassment": 0.5 if any(kw in user_input.lower() for kw in inappropriate_keywords) else 0.0,
            "extreme_profanity": 0.5 if any(kw in ["göt", "orospu"] for kw in user_input.lower().split()) else 0.0
        }
    elif selected_agent_name == "Classification Agent":
        return "positive" if "pozitif" in user_input.lower() or "positive" in user_input.lower() else "neutral"
    elif selected_agent_name == "Translation Agent":
        clean_input = user_input.lower()
        text_to_translate = clean_input.split(":", 1)[1].strip() if ":" in clean_input else clean_input
        target_lang = None
        source_lang = None

        # Hedef dili algıla
        if "ispanyolcaya çevir" in clean_input or "ispanyolca" in clean_input:
            target_lang = "es"
        elif "fransızcaya çevir" in clean_input or "fransızca" in clean_input:
            target_lang = "fr"
        elif "türkçeye çevir" in clean_input or "türkis" in clean_input:
            target_lang = "tr"
        elif "ingilizceye çevir" in clean_input or "ingilizce" in clean_input:
            target_lang = "en"
        else:
            # Hedef dil belirtilmemişse, varsayılan olarak İngilizce
            target_lang = "en" if current_language != "en" else "tr"

        # Kaynak dili algıla (isteğe bağlı, googletrans otomatik algılıyor)
        if current_language == "tr":
            source_lang = "tr"
        elif current_language == "en":
            source_lang = "en"
        elif current_language == "de":
            source_lang = "de"

        try:
            translator = Translator()
            translation = translator.translate(text_to_translate, src=source_lang, dest=target_lang).text
            return translation
        except Exception as e:
            logger.error(f"Translation error: {str(e)}")
            return f"Çeviri hatası: {text_to_translate} ({str(e)})"
    elif selected_agent_name == "Custom Agent":
        return "AI, verileri işlemek, örüntüleri öğrenmek ve kararlar almak için algoritmalar kullanır."
    return {"error": "Unknown agent"}