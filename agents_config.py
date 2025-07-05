import os

translations = {
    "en": {
        "title": "IO Assistant",
        "input_placeholder": "Enter your prompt here...",
        "send_button": "Send",
        "clear_button": "Clear Chat",
        "technical_details_button": "Technical Details",
        "help_button": "Help",
        "help_title": "Agent Help",
        "technical_details_title": "Technical Details",
        "copy_button": "Copy to Clipboard",
        "copy_success": "Copied to clipboard!",
        "social_label": "Follow us: ",
        "loading": "Processing...",
        "wrong_agent_warning": "You selected '{selected_agent}' ({selected_agent_description}). Did you mean '{correct_agent}' ({correct_agent_description})? Click Yes to switch, No to continue.",
        "content_warning": "Content may contain inappropriate elements. Please review the technical details.",
        "safe_content": "Content is safe.",
        "issues_detected": "Issues detected: {issues}",
        "positive_sentiment": "The sentiment is positive.",
        "negative_sentiment": "The sentiment is negative.",
        "neutral_sentiment": "The sentiment is neutral.",
        "unknown_sentiment_error": "Unable to determine sentiment.",
        "entities_detected": "Entities detected: {entities}",
        "classification_result": "Classified as: {category}",
        "translation_result": "Translated text: {translated_text}",
        "summary_result": "Summary: {summary}\nKey Points: {key_points}",
        "custom_result": "Response: {response}",
        "agent_descriptions": {
            "Summary Agent": "Summarizes text into concise points.",
            "Sentiment Analysis Agent": "Analyzes the sentiment of the text (positive, negative, neutral).",
            "Named Entity Recognizer": "Identifies entities like names, organizations, and locations in text.",
            "Moderation Agent": "Checks text for inappropriate content.",
            "Classification Agent": "Classifies text into predefined categories.",
            "Translation Agent": "Translates text into another language.",
            "Custom Agent": "Handles custom queries with flexible responses."
        },
        "agent_examples": {
            "Summary Agent": "e.g., 'How does blockchain technology make financial transactions secure?'",
            "Sentiment Analysis Agent": "e.g., 'This product is awesome, you should definitely buy it!'",
            "Named Entity Recognizer": "e.g., 'Tesla opened a new factory in New York.'",
            "Moderation Agent": "e.g., 'Is there any inappropriate language in this comment?'",
            "Classification Agent": "e.g., 'Is this review positive or negative?'",
            "Translation Agent": "e.g., 'Translate to English: Merhaba, nasılsın?'",
            "Custom Agent": "e.g., 'What is AI and how does it work?'"
        },
        "agent_features": {
            "Summary Agent": "Concise summaries, key point extraction",
            "Sentiment Analysis Agent": "Positive/negative/neutral sentiment detection",
            "Named Entity Recognizer": "Entity detection (names, places, organizations)",
            "Moderation Agent": "Content safety check",
            "Classification Agent": "Text categorization",
            "Translation Agent": "Multi-language translation",
            "Custom Agent": "Flexible query handling"
        },
        "classification_categories": {
            "positive": "Positive",
            "negative": "Negative",
            "neutral": "Neutral"
        }
    },
    "tr": {
        "title": "IO Asistan",
        "input_placeholder": "Komutunuzu buraya girin...",
        "send_button": "Gönder",
        "clear_button": "Sohbeti Temizle",
        "technical_details_button": "Teknik Detaylar",
        "help_button": "Yardım",
        "help_title": "Ajan Yardımı",
        "technical_details_title": "Teknik Detaylar",
        "copy_button": "Panoya Kopyala",
        "copy_success": "Panoya kopyalandı!",
        "social_label": "Bizi takip edin: ",
        "loading": "İşleniyor...",
        "wrong_agent_warning": "'{selected_agent}' seçtiniz ({selected_agent_description}). '{correct_agent}' ({correct_agent_description}) mi demek istediniz? Değiştirmek için Evet, devam etmek için Hayır tıklayın.",
        "content_warning": "İçerik uygunsuz öğeler içerebilir. Lütfen teknik detayları inceleyin.",
        "safe_content": "İçerik güvenli.",
        "issues_detected": "Tespit edilen sorunlar: {issues}",
        "positive_sentiment": "Duygu pozitif.",
        "negative_sentiment": "Duygu negatif.",
        "neutral_sentiment": "Duygu nötr.",
        "unknown_sentiment_error": "Duygu belirlenemedi.",
        "entities_detected": "Tespit edilen varlıklar: {entities}",
        "classification_result": "Sınıflandırıldı: {category}",
        "translation_result": "Çevrilen metin: {translated_text}",
        "summary_result": "Özet: {summary}\nAna Noktalar: {key_points}",
        "custom_result": "Yanıt: {response}",
        "agent_descriptions": {
            "Summary Agent": "Metni kısa ve öz noktalara özetler.",
            "Sentiment Analysis Agent": "Metnin duygusunu analiz eder (pozitif, negatif, nötr).",
            "Named Entity Recognizer": "Metindeki isim, organizasyon ve konum gibi varlıkları tanımlar.",
            "Moderation Agent": "Metni uygunsuz içerik açısından kontrol eder.",
            "Classification Agent": "Metni önceden tanımlanmış kategorilere sınıflandırır.",
            "Translation Agent": "Metni başka bir dile çevirir.",
            "Custom Agent": "Esnek yanıtlarla özel sorguları işler."
        },
        "agent_examples": {
            "Summary Agent": "Örn: 'Blockchain teknolojisi finansal işlemleri nasıl güvenli hale getiriyor?'",
            "Sentiment Analysis Agent": "Örn: 'Bu ürün harika, kesinlikle almalısınız!'",
            "Named Entity Recognizer": "Örn: 'Tesla, New York’ta yeni bir fabrika açtı.'",
            "Moderation Agent": "Örn: 'Bu yorumda uygunsuz bir dil var mı?'",
            "Classification Agent": "Örn: 'Bu inceleme pozitif mi, negatif mi?'",
            "Translation Agent": "Örn: 'İngilizceye çevir: Merhaba, nasılsın?'",
            "Custom Agent": "Örn: 'Yapay zeka nedir ve nasıl çalışır?'"
        },
        "agent_features": {
            "Summary Agent": "Kısa özetler, ana nokta çıkarma",
            "Sentiment Analysis Agent": "Pozitif/negatif/nötr duygu tespiti",
            "Named Entity Recognizer": "Varlık tespiti (isimler, yerler, organizasyonlar)",
            "Moderation Agent": "İçerik güvenliği kontrolü",
            "Classification Agent": "Metin kategorizasyonu",
            "Translation Agent": "Çok dilli çeviri",
            "Custom Agent": "Esnek sorgu işleme"
        },
        "classification_categories": {
            "positive": "Pozitif",
            "negative": "Negatif",
            "neutral": "Nötr"
        }
    },
    "de": {
        "title": "IO Assistent",
        "input_placeholder": "Geben Sie hier Ihre Anfrage ein...",
        "send_button": "Senden",
        "clear_button": "Chat löschen",
        "technical_details_button": "Technische Details",
        "help_button": "Hilfe",
        "help_title": "Agent-Hilfe",
        "technical_details_title": "Technische Details",
        "copy_button": "In die Zwischenablage kopieren",
        "copy_success": "In die Zwischenablage kopiert!",
        "social_label": "Folgen Sie uns: ",
        "loading": "Verarbeitung...",
        "wrong_agent_warning": "Sie haben '{selected_agent}' ({selected_agent_description}) ausgewählt. Meinten Sie '{correct_agent}' ({correct_agent_description})? Klicken Sie auf Ja zum Wechseln, Nein zum Fortfahren.",
        "content_warning": "Inhalt kann unangemessene Elemente enthalten. Bitte überprüfen Sie die technischen Details.",
        "safe_content": "Inhalt ist sicher.",
        "issues_detected": "Erkannte Probleme: {issues}",
        "positive_sentiment": "Die Stimmung ist positiv.",
        "negative_sentiment": "Die Stimmung ist negativ.",
        "neutral_sentiment": "Die Stimmung ist neutral.",
        "unknown_sentiment_error": "Stimmung konnte nicht bestimmt werden.",
        "entities_detected": "Erkannte Entitäten: {entities}",
        "classification_result": "Klassifiziert als: {category}",
        "translation_result": "Übersetzter Text: {translated_text}",
        "summary_result": "Zusammenfassung: {summary}\nSchlüsselpunkte: {key_points}",
        "custom_result": "Antwort: {response}",
        "agent_descriptions": {
            "Summary Agent": "Fasst Texte in kurze Punkte zusammen.",
            "Sentiment Analysis Agent": "Analysiert die Stimmung des Textes (positiv, negativ, neutral).",
            "Named Entity Recognizer": "Erkennt Entitäten wie Namen, Organisationen und Orte im Text.",
            "Moderation Agent": "Überprüft Texte auf unangemessene Inhalte.",
            "Classification Agent": "Klassifiziert Texte in vordefinierte Kategorien.",
            "Translation Agent": "Übersetzt Texte in eine andere Sprache.",
            "Custom Agent": "Behandelt benutzerdefinierte Anfragen mit flexiblen Antworten."
        },
        "agent_examples": {
            "Summary Agent": "Bsp.: 'Wie macht Blockchain-Technologie Finanztransaktionen sicher?'",
            "Sentiment Analysis Agent": "Bsp.: 'Dieses Produkt ist toll, Sie sollten es unbedingt kaufen!'",
            "Named Entity Recognizer": "Bsp.: 'Tesla hat in New York eine neue Fabrik eröffnet.'",
            "Moderation Agent": "Bsp.: 'Enthält dieser Kommentar unangemessene Sprache?'",
            "Classification Agent": "Bsp.: 'Ist diese Bewertung positiv oder negativ?'",
            "Translation Agent": "Bsp.: 'Ins Englische übersetzen: Hallo, wie geht’s?'",
            "Custom Agent": "Bsp.: 'Was ist KI und wie funktioniert sie?'"
        },
        "agent_features": {
            "Summary Agent": "Kurze Zusammenfassungen, Extraktion von Schlüsselpunkten",
            "Sentiment Analysis Agent": "Erkennung von positiver/negativer/neutraler Stimmung",
            "Named Entity Recognizer": "Erkennung von Entitäten (Namen, Orte, Organisationen)",
            "Moderation Agent": "Überprüfung der Inhaltssicherheit",
            "Classification Agent": "Textkategorisierung",
            "Translation Agent": "Mehrsprachige Übersetzung",
            "Custom Agent": "Flexible Anfragebearbeitung"
        },
        "classification_categories": {
            "positive": "Positiv",
            "negative": "Negativ",
            "neutral": "Neutral"
        }
    }
}

agent_task_mapping = {
    "Summary Agent": {"task": "summarize", "args": {"max_length": 100}},
    "Sentiment Analysis Agent": {"task": "sentiment_analysis", "args": {}},
    "Named Entity Recognizer": {"task": "named_entity_recognition", "args": {}},
    "Moderation Agent": {"task": "moderation", "args": {}},
    "Classification Agent": {"task": "classification", "args": {"categories": ["positive", "negative", "neutral"]}},
    "Translation Agent": {"task": "translation", "args": {"target_language": "en"}},
    "Custom Agent": {"task": "custom", "args": {}}
}

agent_icons = {
    "Summary Agent": "icons/summary.png",
    "Sentiment Analysis Agent": "icons/sentiment.png",
    "Named Entity Recognizer": "icons/entity.png",
    "Moderation Agent": "icons/moderation.png",
    "Classification Agent": "icons/classification.png",
    "Translation Agent": "icons/translation.png",
    "Custom Agent": "icons/custom.png"
}