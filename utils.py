import re
import json
import os
import logging
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
    input_lower = user_input.lower().strip()

    # Özetleme için
    if any(kw in input_lower for kw in ["summarize", "özet", "zusammenfassung", "özetle"]):
        return "Summary Agent"
    elif len(input_lower.split()) > 20:  # Uzun metinler için Summary Agent öner
        return "Summary Agent"

    # Duygu analizi için
    elif any(kw in input_lower for kw in ["sentiment", "duygu", "stimmung", "hızlı", "kullanışlı", "harika", "berbat", "güzel", "kötü"]):
        return "Sentiment Analysis Agent"

    # Varlık tanıma için
    elif any(kw in input_lower for kw in ["entity", "entities", "varlık", "entitäten", "elon musk", "tesla", "spacex", "california"]):
        return "Named Entity Recognizer"

    # Moderasyon için
    elif any(kw in input_lower for kw in ["moderate", "denetim", "harmful", "uygunsuz", "berbat", "dolandırıcı", "para israfı"]):
        return "Moderation Agent"

    # Sınıflandırma için
    elif any(kw in input_lower for kw in ["classify", "sınıflandır", "klassifizierung", "pozitif", "positive", "negatif", "negative", "harika", "mükemmel", "inanılmaz"]):
        return "Classification Agent"

    # Çeviri için
    elif any(kw in input_lower for kw in ["translate", "çevir", "übersetzung", "türkis", "ispanyolca", "fransızca", "ingilizce"]):
        return "Translation Agent"
    elif any(kw in input_lower for kw in ["merhaba", "hello", "hallo", "nasılsın", "how are you", "burası neresi", "where is this", "nerede", "naber"]):
        return "Translation Agent"

    # Varsayılan
    return "Custom Agent"