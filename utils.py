import re

def fix_turkish_chars(text):
    corrections = {
        "saglik": "sağlık", "egitim": "eğitim", "donusturuyor": "dönüştürüyor",
        "teshis": "teşhis", "yapiyor": "yapıyor", "Ogrencilerin": "Öğrencilerin",
        "ogrenme": "öğrenme", "sureclerini": "süreçlerini", "kisisellestiriyor": "kişiselleştiriyor",
        "calisiyor": "çalışıyor", "olusturuyor": "oluşturuyor", "ise yaramaz": "işe yaramaz",
        "fineransal": "finansal", "Gülen": "Güvenli işlemler", "guvenli": "güvenli",
        "seffaf": "şeffaf", "dunyayi": "dünyayı", "degistiriyor": "değiştiriyor"
    }
    text = re.sub(r'[^\x00-\x7FğüşöçıİĞÜŞÖÇ]+', '', text)
    for wrong, correct in corrections.items():
        text = text.replace(wrong, correct)
    if text and text[-1] not in '.!?':
        text += '.'
    return text

def clean_response_text(text):
    """
    API yanıtındaki anlamsız kelimeleri, kod parçalarını ve karışık metinleri temizler.
    """
    # HTML etiketlerini ve kod benzeri yapıları kaldır
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\([^)]+\.[^\s]+', '', text)  # Fonksiyon çağrıları (örneğin, Handy(concat-appendCatBeing.u))
    text = re.sub(r'[^\w\s.,:?!-ğüşöçıİĞÜŞÖÇ]', '', text)  # Özel karakterleri kaldır
    text = re.sub(r'\b[A-Za-z0-9_]+[.]+\w+\b', '', text)  # Kod benzeri ifadeleri kaldır (örneğin, strom.getTable)
    text = re.sub(r'\s+', ' ', text)  # Fazla boşlukları temizle
    # Tekrar eden cümleleri kaldır
    sentences = text.split('.')
    seen = set()
    cleaned_sentences = []
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence and sentence not in seen:
            seen.add(sentence)
            cleaned_sentences.append(sentence)
    return '. '.join(cleaned_sentences).strip() + ('.' if cleaned_sentences else '')

def filter_key_points(key_points, input_text):
    input_lower = input_text.lower()
    filtered = []
    for kp in key_points:
        kp_clean = kp.strip('.').strip()
        if (kp_clean.lower() not in input_lower and 
            kp_clean.lower() not in ["blok zinciri", "blockchain", "finanasal işlemler", "finanztransaktionen", 
                                     "teknoloji dünyayı değiştiriyor", "technology changing the world"]):
            filtered.append(kp_clean)
    return filtered if filtered else ["None"]

def detect_correct_agent(user_input, current_language):
    input_lower = user_input.lower()
    word_count = len(input_lower.split())
    
    if any(keyword in input_lower for keyword in ["çevir", "translate to", "übersetzen"]):
        return "Translation Agent"
    elif "özet" in input_lower or "summary" in input_lower or "zusammenfassung" in input_lower or \
         any(keyword in input_lower for keyword in ["teknoloji", "işlem", "sistem", "blockchain", "blok zinciri",
                                                   "technology", "transaction", "system", "technologie", "transaktion"]) or \
         word_count >= 5:
        return "Summary Agent"
    elif any(keyword in input_lower for keyword in ["born", "doğdu", "geboren", "date", "tarih", "datum", "location", "konum", "ort"]):
        return "Named Entity Recognizer"
    elif any(keyword in input_lower for keyword in ["sentiment", "duygu", "stimmung", "feel", "hiss", "gefüh"]):
        return "Sentiment Analysis Agent"
    elif any(keyword in input_lower for keyword in ["classify", "sınıfland", "klassifiz"]):
        return "Classification Agent"
    elif any(keyword in input_lower for keyword in ["kötü", "berbat", "işe yaramaz", "bad", "terrible", "useless", "schlecht", "nutzlos"]):
        return "Moderation Agent"
    else:
        return "Custom Agent"