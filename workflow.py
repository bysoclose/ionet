import os
import logging
from agents_config import agent_task_mapping
from deep_translator import GoogleTranslator

logger = logging.getLogger(__name__)

async def run_workflow(user_input, selected_agent_name, current_language):
    logger.debug("Simulating API response for testing")
    if selected_agent_name == "Summary Agent":
        clean_input = user_input.replace("Summarize:", "").replace("Özetle:", "").replace("Zusammenfassen:", "").strip()
        return {
            "summary": clean_input[:100] + "..." if len(clean_input) > 100 else clean_input,
            "key_points": [word.capitalize() for word in clean_input.split()[:3]]
        }
    elif selected_agent_name == "Sentiment Analysis Agent":
        positive_keywords = ["love", "sevdim", "harika", "mükemmel", "güzel", "hızlı", "kullanışlı", "inanılmaz"]
        negative_keywords = ["kötü", "berbat", "sinir bozucu", "can sıkıcı"]
        if any(kw in user_input.lower() for kw in positive_keywords):
            return "positive"
        elif any(kw in user_input.lower() for kw in negative_keywords):
            return "negative"
        return "neutral"
    elif selected_agent_name == "Named Entity Recognizer":
        entities = {"person": [], "organization": [], "location": []}
        if "Elon Musk" in user_input:
            entities["person"].append("Elon Musk")
        if "Tesla" in user_input:
            entities["organization"].append("Tesla")
        if "SpaceX" in user_input:
            entities["organization"].append("SpaceX")
        if "California" in user_input:
            entities["location"].append("California")
        return {"entities": entities}
    elif selected_agent_name == "Moderation Agent":
        inappropriate_keywords = ["kötü", "pislik", "göt", "orospu", "harmful", "berbat", "dolandırıcı", "israf"]
        return {
            "hate_speech": 0.5 if any(kw in user_input.lower() for kw in inappropriate_keywords) else 0.0,
            "harassment": 0.5 if any(kw in user_input.lower() for kw in inappropriate_keywords) else 0.0,
            "extreme_profanity": 0.5 if any(kw in ["göt", "orospu"] for kw in user_input.lower().split()) else 0.0
        }
    elif selected_agent_name == "Classification Agent":
        positive_keywords = ["harika", "mükemmel", "inanılmaz", "güzel", "etkileyici", "positive"]
        negative_keywords = ["kötü", "berbat", "sinir bozucu", "negatif"]
        if any(kw in user_input.lower() for kw in positive_keywords):
            return "positive"
        elif any(kw in user_input.lower() for kw in negative_keywords):
            return "negative"
        return "neutral"
    elif selected_agent_name == "Translation Agent":
        clean_input = user_input.lower().strip()
        # Çeviri komutunu temizle
        for cmd in ["translate to", "çevir:", "ispanyolcaya çevir", "ingilizceye çevir", "fransızcaya çevir", "türkçeye çevir", "übersetzen ins", "übersetzung"]:
            if cmd in clean_input:
                clean_input = clean_input.split(cmd, 1)[1].strip()
        text_to_translate = clean_input
        target_lang = None
        source_lang = "auto"

        # Hedef dili algıla
        if "ispanyolca" in user_input.lower() or "spanish" in user_input.lower():
            target_lang = "es"
        elif "fransızca" in user_input.lower() or "french" in user_input.lower():
            target_lang = "fr"
        elif "türkçe" in user_input.lower() or "turkish" in user_input.lower():
            target_lang = "tr"
        elif "ingilizce" in user_input.lower() or "english" in user_input.lower():
            target_lang = "en"
        else:
            target_lang = "en" if current_language != "en" else "tr"

        # Kaynak dili ayarla
        if current_language == "tr":
            source_lang = "tr"
        elif current_language == "en":
            source_lang = "en"
        elif current_language == "de":
            source_lang = "de"

        try:
            translator = GoogleTranslator(source=source_lang, target=target_lang)
            translation = translator.translate(text_to_translate)
            return translation
        except Exception as e:
            logger.error(f"Translation error: {str(e)}")
            return f"Çeviri hatası: {text_to_translate} ({str(e)})"
    elif selected_agent_name == "Custom Agent":
        return "AI, verileri işlemek, örüntüleri öğrenmek ve kararlar almak için algoritmalar kullanır."
    return {"error": "Unknown agent"}