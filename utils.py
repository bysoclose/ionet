import re
import json
import os
from agents_config import translations

def fix_turkish_chars(text):
    if not isinstance(text, str):
        return text
    corrections_file = "corrections.json"
    if os.path.exists(corrections_file):
        with open(corrections_file, 'r', encoding='utf-8') as f:
            corrections = json.load(f)
        for wrong, correct in corrections.items():
            text = text.replace(wrong, correct)
    return text

def filter_key_points(key_points, user_input):
    filtered_points = []
    for point in key_points:
        if len(point.strip()) > 5 and any(word.lower() in point.lower() for word in user_input.split()):
            filtered_points.append(point)
    return filtered_points[:3]

def detect_correct_agent(user_input, current_language):
    input_lower = user_input.lower()
    if "summarize" in input_lower or "özet" in input_lower or "zusammenfassung" in input_lower:
        return "Summary Agent"
    elif "sentiment" in input_lower or "duygu" in input_lower or "stimmung" in input_lower:
        return "Sentiment Analysis Agent"
    elif "entity" in input_lower or "entities" in input_lower or "varlık" in input_lower or "entitäten" in input_lower:
        return "Named Entity Recognizer"
    elif "moderate" in input_lower or "denetim" in input_lower or "harmful" in input_lower or any(kw in input_lower for kw in ["kötü", "pislik", "göt", "orospu"]):
        return "Moderation Agent"
    elif "classify" in input_lower or "sınıflandır" in input_lower or "klassifizierung" in input_lower or "pozitif" in input_lower or "positive" in input_lower:
        return "Classification Agent"
    elif "translate" in input_lower or "çevir" in input_lower or "übersetzung" in input_lower or "türkis" in input_lower or "ispanyolca" in input_lower or "fransızca" in input_lower or "ingilizce" in input_lower:
        return "Translation Agent"
    # Basit selamlaşma veya yer sorguları için de Translation Agent öner
    elif any(kw in input_lower for kw in ["merhaba", "hello", "hallo", "nasılsın", "how are you", "burası neresi", "where is this"]):
        return "Translation Agent"
    return "Custom Agent"