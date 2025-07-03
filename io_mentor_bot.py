import sys
import asyncio
import logging
import warnings
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QSpacerItem,
    QMessageBox, QComboBox, QDialog
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QObject
from utils import fix_turkish_chars, filter_key_points, detect_correct_agent
from agents_config import translations, agent_task_mapping, agent_icons
from workflow import run_workflow
import nest_asyncio
from dotenv import load_dotenv
import os
import json

# DeprecationWarning'leri bastır
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Log ayarları (sadece debug.log'a yaz)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log', mode='w', encoding='utf-8'),
    ],
    force=True
)
logger = logging.getLogger(__name__)

nest_asyncio.apply()
load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    logger.error("OPENAI_API_KEY eksik!")
    sys.exit(1)

def copy_to_clipboard(text, current_language):
    logger.debug("Panoya kopyalanıyor: %s", text)
    app.clipboard().setText(text)
    QMessageBox.information(None, translations[current_language]["copy_success"], f"'{text}' {translations[current_language]['copy_success']}")

def on_click_copy(text, current_language):
    copy_to_clipboard(text, current_language)

class AgentHelpDialog(QDialog):
    def __init__(self, current_language, parent=None):
        super().__init__(parent)
        logger.debug("AgentHelpDialog başlatılıyor")
        self.setWindowTitle(translations[current_language]["help_title"])
        self.setGeometry(200, 200, 500, 400)
        layout = QVBoxLayout(self)

        self.help_text = QTextEdit(self)
        self.help_text.setReadOnly(True)
        help_content = ""
        for agent, desc in translations[current_language]["agent_descriptions"].items():
            help_content += f"<b>{agent}</b><br>{desc}<br><i>{translations[current_language]['agent_examples'][agent]}</i><br><br>"
        self.help_text.setHtml(help_content)
        self.help_text.setStyleSheet("font-size: 14px; color: black; border: 1px solid black; padding: 10px;")
        layout.addWidget(self.help_text)

        close_btn = QPushButton("Close", self)
        close_btn.setStyleSheet("background-color: #162447; color: white; padding: 5px;")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)

class TechnicalDetailsDialog(QDialog):
    def __init__(self, result, current_language, parent=None):
        super().__init__(parent)
        logger.debug("TechnicalDetailsDialog başlatılıyor")
        self.setWindowTitle(translations[current_language]["technical_details_title"])
        self.setGeometry(200, 200, 400, 300)
        layout = QVBoxLayout(self)

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        self.text_edit.setText(result)
        self.text_edit.setStyleSheet("font-size: 14px; color: black; border: 1px solid black; font-family: Monospace; padding: 10px;")
        layout.addWidget(self.text_edit)

        copy_btn = QPushButton(translations[current_language]["copy_button"], self)
        copy_btn.setStyleSheet("background-color: #162447; color: white; padding: 5px;")
        copy_btn.clicked.connect(lambda: copy_to_clipboard(result, current_language))
        layout.addWidget(copy_btn)

class WorkerSignals(QObject):
    result_ready = pyqtSignal(str)

class Worker(QThread):
    def __init__(self, user_input, selected_agent_name, signals, current_language):
        super().__init__()
        self.user_input = user_input
        self.selected_agent_name = selected_agent_name
        self.signals = signals
        self.current_language = current_language
        logger.debug("Worker başlatılıyor: %s, %s", user_input, selected_agent_name)

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            result = loop.run_until_complete(run_workflow(self.user_input, self.selected_agent_name, self.current_language))
            self.signals.result_ready.emit(str(result))
        except Exception as e:
            logger.error("Worker hatası: %s", str(e))
            self.signals.result_ready.emit(f"Error: {str(e)}")
        finally:
            loop.close()

class IOAssistant(QMainWindow):
    def __init__(self):
        super().__init__()
        logger.debug("IOAssistant başlatılıyor")
        self.current_language = "en"
        self.last_result = ""
        self.setWindowTitle(translations[self.current_language]["title"])
        self.setGeometry(100, 100, 800, 900)
        self.workers = []

        try:
            main_widget = QWidget(self)
            self.setCentralWidget(main_widget)
            self.layout = QVBoxLayout(main_widget)
            logger.debug("Ana widget oluşturuldu")
        except Exception as e:
            logger.error("Ana widget oluşturulurken hata: %s", str(e))
            raise

        # Arka plan resmi
        self.background_label = QLabel(main_widget)
        background_path = "background.jpg"
        if os.path.exists(background_path):
            try:
                pixmap = QPixmap(background_path).scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
                if pixmap.isNull():
                    logger.error("background.jpg geçersiz veya bozuk")
                    self.background_label.setStyleSheet("background-color: #162447;")
                else:
                    self.background_label.setPixmap(pixmap)
                    logger.debug("background.jpg yüklendi")
            except Exception as e:
                logger.error("background.jpg yüklenirken hata: %s", str(e))
                self.background_label.setStyleSheet("background-color: #162447;")
        else:
            logger.warning("background.jpg bulunamadı, düz renk kullanılıyor")
            self.background_label.setStyleSheet("background-color: #162447;")
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.background_label.lower()

        self.title_label = QLabel(translations[self.current_language]["title"], self)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        self.layout.addWidget(self.title_label, alignment=Qt.AlignCenter)

        self.layout.addSpacerItem(QSpacerItem(20, 40))

        # Dil seçimi
        language_widget = QWidget(self)
        language_layout = QHBoxLayout(language_widget)
        self.language_label = QLabel("Language:", self)
        self.language_label.setStyleSheet("font-size: 18px; color: white;")
        self.language_combo = QComboBox(self)
        self.language_combo.addItems(["English", "Türkçe", "Deutsch"])
        self.language_combo.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: red; border: 3px solid white; padding: 5px; font-size: 18px;")
        self.language_combo.setMinimumWidth(280)
        self.language_combo.setMinimumHeight(42)
        language_icons = {
            "English": "icons/uk.png",
            "Türkçe": "icons/tr.png",
            "Deutsch": "icons/de.png"
        }
        for lang, icon_path in language_icons.items():
            if icon_path and os.path.exists(icon_path):
                try:
                    icon = QIcon(icon_path)
                    if icon.isNull():
                        logger.error("Dil ikonu geçersiz veya bozuk: %s", icon_path)
                    else:
                        self.language_combo.setItemIcon(self.language_combo.findText(lang), icon)
                        logger.debug("Dil ikonu yüklendi: %s", icon_path)
                except Exception as e:
                    logger.error("Dil ikonu yüklenirken hata: %s, %s", icon_path, str(e))
            else:
                logger.warning("Dil ikonu bulunamadı: %s", icon_path)
        self.language_combo.currentTextChanged.connect(self.change_language)
        language_layout.addWidget(self.language_label)
        language_layout.addWidget(self.language_combo)
        language_layout.addStretch()
        self.layout.addWidget(language_widget, alignment=Qt.AlignLeft)

        # Girdi alanı
        input_widget = QWidget(self)
        input_layout = QHBoxLayout(input_widget)
        self.agent_combo = QComboBox(self)
        self.agent_combo.addItems(translations[self.current_language]["agent_descriptions"].keys())
        self.agent_combo.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: red; border: 3px solid white; padding: 5px; font-size: 18px;")
        self.agent_combo.setMinimumWidth(280)
        self.agent_combo.setMinimumHeight(42)
        for agent in translations[self.current_language]["agent_descriptions"]:
            self.agent_combo.setItemData(
                self.agent_combo.findText(agent),
                translations[self.current_language]["agent_descriptions"][agent],
                Qt.ToolTipRole
            )
            icon_path = agent_icons.get(agent, "")
            if icon_path and os.path.exists(icon_path):
                try:
                    icon = QIcon(icon_path)
                    if icon.isNull():
                        logger.error("İkon geçersiz veya bozuk: %s", icon_path)
                    else:
                        self.agent_combo.setItemIcon(self.agent_combo.findText(agent), icon)
                        logger.debug("İkon yüklendi: %s", icon_path)
                except Exception as e:
                    logger.error("İkon yüklenirken hata: %s, %s", icon_path, str(e))
            else:
                logger.warning("İkon bulunamadı: %s", icon_path)
        self.agent_combo.currentTextChanged.connect(self.update_example_label)
        self.input_entry = QLineEdit(self)
        self.input_entry.setPlaceholderText(translations[self.current_language]["input_placeholder"])
        self.input_entry.setStyleSheet("background-color: rgba(0, 0, 0, 0); font-size: 26px; color: white; border: 3px solid white; padding: 5px;")
        self.input_entry.setMinimumWidth(840)
        self.input_entry.setMinimumHeight(100)
        self.input_entry.returnPressed.connect(self.on_submit)
        self.submit_btn = QPushButton(translations[self.current_language]["send_button"], self)
        self.submit_btn.setStyleSheet("background-color: #162447; color: red; padding: 5px;")
        self.submit_btn.clicked.connect(self.on_submit)
        self.help_btn = QPushButton(translations[self.current_language]["help_button"], self)
        self.help_btn.setStyleSheet("background-color: #162447; color: white; padding: 5px;")
        self.help_btn.clicked.connect(self.show_help_dialog)
        input_layout.addWidget(self.agent_combo)
        input_layout.addWidget(self.input_entry)
        input_layout.addWidget(self.submit_btn)
        input_layout.addWidget(self.help_btn)
        self.layout.addWidget(input_widget, alignment=Qt.AlignCenter)

        self.example_label = QLabel("", self)
        self.example_label.setStyleSheet("color: lightgray; font-style: italic; font-size: 13px;")
        self.layout.addWidget(self.example_label)
        self.features_label = QLabel("", self)
        self.features_label.setStyleSheet("color: lightgray; font-style: italic; font-size: 13px;")
        self.layout.addWidget(self.features_label)

        self.loading_label = QLabel("", self)
        self.loading_label.setStyleSheet("font-size: 16px; color: orange; qproperty-alignment: AlignCenter;")
        self.layout.addWidget(self.loading_label)

        self.chat_textbox = QTextEdit(self)
        self.chat_textbox.setReadOnly(True)
        self.chat_textbox.setStyleSheet("background-color: rgba(0, 0, 0, 0); font-size: 16px; color: white; border: 3px solid white;")
        self.layout.addWidget(self.chat_textbox)

        button_widget = QWidget(self)
        button_layout = QHBoxLayout(button_widget)
        self.clear_btn = QPushButton(translations[self.current_language]["clear_button"], self)
        self.clear_btn.setStyleSheet("background-color: #162447; color: white; padding: 5px;")
        self.clear_btn.clicked.connect(self.clear_chat_history)
        button_layout.addWidget(self.clear_btn)
        self.technical_details_btn = QPushButton(translations[self.current_language]["technical_details_button"], self)
        self.technical_details_btn.setStyleSheet("background-color: #162447; color: white; padding: 5px;")
        self.technical_details_btn.clicked.connect(self.show_technical_details)
        button_layout.addWidget(self.technical_details_btn)
        button_layout.addStretch()
        self.layout.addWidget(button_widget, alignment=Qt.AlignCenter)

        self.social_widget = QWidget(self)
        self.social_layout = QHBoxLayout(self.social_widget)
        self.social_label = QLabel(translations[self.current_language]["social_label"], self)
        self.social_label.setStyleSheet("font-size: 14px; font-weight: bold; color: white;")
        self.social_layout.addWidget(self.social_label)

        self.social_links = [
            ("github.png", "https://github.com/bysoclose/io-mentor-bot"),
            ("discord.png", "https://discord.gg/cXN3WghNhG"),
            ("twitter.png", "https://twitter.com/bilal_ibanoglu")
        ]
        self.social_link_labels = []
        for icon_path, link in self.social_links:
            if icon_path and os.path.exists(icon_path):
                try:
                    pixmap = QPixmap(icon_path).scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    if pixmap.isNull():
                        logger.error("Sosyal medya ikonu geçersiz veya bozuk: %s", icon_path)
                    else:
                        link_text = QLabel(self)
                        link_text.setPixmap(pixmap)
                        link_text.setStyleSheet("padding: 5px;")
                        link_text.setToolTip(link)
                        link_text.mousePressEvent = lambda e, t=link: on_click_copy(t, self.current_language)
                        self.social_layout.addWidget(link_text)
                        self.social_link_labels.append(link_text)
                        logger.debug("Sosyal medya ikonu yüklendi: %s", icon_path)
                except Exception as e:
                    logger.error("Sosyal medya ikonu yüklenirken hata: %s, %s", icon_path, str(e))
            else:
                logger.warning("Sosyal medya ikonu bulunamadı: %s", icon_path)
        self.social_layout.addStretch()
        self.layout.addWidget(self.social_widget, alignment=Qt.AlignCenter)

        self.resizeEvent = self.on_resize
        self.update_example_label(self.agent_combo.currentText())

        logger.debug("IOAssistant UI oluşturuldu")
        try:
            self.show()
            logger.debug("Pencere gösterildi")
        except Exception as e:
            logger.error("Pencere gösterilirken hata: %s", str(e))
            raise

    def on_submit(self):
        user_input = self.input_entry.text().strip()
        if user_input:
            logger.debug("Gönder butonuna basıldı: %s", user_input)
            self.process_user_input(user_input)

    def change_language(self, language):
        logger.debug("Dil değiştiriliyor: %s", language)
        lang_map = {"English": "en", "Türkçe": "tr", "Deutsch": "de"}
        self.current_language = lang_map.get(language, "en")
        self.language_combo.blockSignals(True)
        self.update_ui_language()
        self.language_combo.blockSignals(False)

    def update_ui_language(self):
        logger.debug("UI dili güncelleniyor: %s", self.current_language)
        self.setWindowTitle(translations[self.current_language]["title"])
        self.title_label.setText(translations[self.current_language]["title"])
        self.input_entry.setPlaceholderText(translations[self.current_language]["input_placeholder"])
        self.submit_btn.setText(translations[self.current_language]["send_button"])
        self.clear_btn.setText(translations[self.current_language]["clear_button"])
        self.technical_details_btn.setText(translations[self.current_language]["technical_details_button"])
        self.help_btn.setText(translations[self.current_language]["help_button"])
        self.social_label.setText(translations[self.current_language]["social_label"])
        current_agent = self.agent_combo.currentText()
        self.agent_combo.clear()
        self.agent_combo.addItems(translations[self.current_language]["agent_descriptions"].keys())
        for agent in translations[self.current_language]["agent_descriptions"]:
            self.agent_combo.setItemData(
                self.agent_combo.findText(agent),
                translations[self.current_language]["agent_descriptions"][agent],
                Qt.ToolTipRole
            )
            icon_path = agent_icons.get(agent, "")
            if icon_path and os.path.exists(icon_path):
                try:
                    icon = QIcon(icon_path)
                    if icon.isNull():
                        logger.error("İkon geçersiz veya bozuk: %s", icon_path)
                    else:
                        self.agent_combo.setItemIcon(self.agent_combo.findText(agent), icon)
                except Exception as e:
                    logger.error("İkon yüklenirken hata: %s, %s", icon_path, str(e))
        if current_agent in translations[self.current_language]["agent_descriptions"]:
            self.agent_combo.setCurrentText(current_agent)
        language_icons = {
            "English": "icons/uk.png",
            "Türkçe": "icons/tr.png",
            "Deutsch": "icons/de.png"
        }
        for lang, icon_path in language_icons.items():
            if icon_path and os.path.exists(icon_path):
                try:
                    icon = QIcon(icon_path)
                    if icon.isNull():
                        logger.error("Dil ikonu geçersiz veya bozuk: %s", icon_path)
                    else:
                        self.language_combo.setItemIcon(self.language_combo.findText(lang), icon)
                except Exception as e:
                    logger.error("Dil ikonu yüklenirken hata: %s, %s", icon_path, str(e))
        self.update_example_label(self.agent_combo.currentText())

    def update_example_label(self, agent_name):
        logger.debug("Örnek etiket güncelleniyor: %s", agent_name)
        example = translations[self.current_language]["agent_examples"].get(agent_name, "")
        features = translations[self.current_language]["agent_features"].get(agent_name, "")
        self.example_label.setText(example)
        self.features_label.setText(f"Features: {features}")

    def show_help_dialog(self):
        logger.debug("Yardım diyaloğu açılıyor")
        dialog = AgentHelpDialog(self.current_language, self)
        dialog.exec_()

    def on_resize(self, event):
        logger.debug("Pencere yeniden boyutlandırılıyor")
        background_path = "background.jpg"
        if os.path.exists(background_path):
            try:
                pixmap = QPixmap(background_path).scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
                if pixmap.isNull():
                    logger.error("background.jpg geçersiz veya bozuk")
                else:
                    self.background_label.setPixmap(pixmap)
            except Exception as e:
                logger.error("background.jpg yüklenirken hata: %s", str(e))
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)

    def process_user_input(self, user_input):
        logger.debug("Kullanıcı girişi işleniyor: %s", user_input)
        selected_agent_name = self.agent_combo.currentText()
        correct_agent = detect_correct_agent(user_input, self.current_language)
        logger.debug("Seçilen ajan: %s, Önerilen ajan: %s", selected_agent_name, correct_agent)
        if selected_agent_name != correct_agent:
            warning_msg = translations[self.current_language]["wrong_agent_warning"].format(
                selected_agent=selected_agent_name,
                selected_agent_description=translations[self.current_language]["agent_descriptions"][selected_agent_name],
                correct_agent=correct_agent,
                correct_agent_description=translations[self.current_language]["agent_descriptions"][correct_agent]
            )
            logger.debug("Yanlış ajan uyarısı gösteriliyor: %s", warning_msg)
            reply = QMessageBox.question(
                self, "Agent Selection", warning_msg,
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                selected_agent_name = correct_agent
                self.agent_combo.setCurrentText(correct_agent)
                logger.debug("Kullanıcı önerilen ajanı seçti: %s", correct_agent)

        self.loading_label.setText(translations[self.current_language]["loading"])
        self.submit_btn.setEnabled(False)
        signals = WorkerSignals()
        worker = Worker(user_input, selected_agent_name, signals, self.current_language)
        worker.signals.result_ready.connect(lambda result: self.handle_result(result))
        self.workers.append(worker)
        worker.finished.connect(lambda: self.workers.remove(worker))
        worker.start()

    def show_technical_details(self):
        logger.debug("Teknik detaylar diyaloğu açılıyor")
        dialog = TechnicalDetailsDialog(self.last_result, self.current_language, self)
        dialog.exec_()

    def handle_result(self, result):
        logger.debug("Sonuç işleniyor: %s", result)
        self.last_result = result
        selected_agent_name = self.agent_combo.currentText()
        user_friendly_output = result

        try:
            if selected_agent_name == "Moderation Agent":
                try:
                    result_dict = json.loads(result.replace("'", "\""))
                    issues = []
                    if result_dict.get('hate_speech', 0.0) >= 0.5:
                        issues.append("hate speech" if self.current_language == "en" else "nefret söylemi" if self.current_language == "tr" else "Hassrede")
                    if result_dict.get('harassment', 0.0) >= 0.5:
                        issues.append("harassment" if self.current_language == "en" else "taciz" if self.current_language == "tr" else "Belästigung")
                    if result_dict.get('extreme_profanity', 0.0) >= 0.5:
                        issues.append("extreme profanity" if self.current_language == "en" else "aşırı küfür" if self.current_language == "tr" else "extreme Obszönität")
                    if issues:
                        user_friendly_output = translations[self.current_language]["issues_detected"].format(issues=", ".join(issues))
                        QMessageBox.warning(self, "Content Warning", translations[self.current_language]["content_warning"])
                    else:
                        user_friendly_output = translations[self.current_language]["safe_content"]
                except json.JSONDecodeError:
                    result_lower = result.lower()
                    issues = []
                    if "hate speech" in result_lower:
                        issues.append("hate speech" if self.current_language == "en" else "nefret söylemi" if self.current_language == "tr" else "Hassrede")
                        user_friendly_output = translations[self.current_language]["hate_speech_detected"]
                    elif "harassment" in result_lower:
                        issues.append("harassment" if self.current_language == "en" else "taciz" if self.current_language == "tr" else "Belästigung")
                        user_friendly_output = translations[self.current_language]["harassment_detected"]
                    elif "extreme profanity" in result_lower:
                        issues.append("extreme profanity" if self.current_language == "en" else "aşırı küfür" if self.current_language == "tr" else "extreme Obszönität")
                        user_friendly_output = translations[self.current_language]["extreme_profanity_detected"]
                    else:
                        user_friendly_output = f"Hata: Çıktı işlenemedi. Ham sonuç: {result}"
                    if issues:
                        user_friendly_output = translations[self.current_language]["issues_detected"].format(issues=", ".join(issues))
                        QMessageBox.warning(self, "Content Warning", translations[self.current_language]["content_warning"])
            
            elif selected_agent_name == "Sentiment Analysis Agent":
                try:
                    sentiment_score = float(result)
                    if sentiment_score >= 0.5:
                        user_friendly_output = translations[self.current_language]["positive_sentiment"]
                    elif sentiment_score <= -0.5:
                        user_friendly_output = translations[self.current_language]["negative_sentiment"]
                    else:
                        user_friendly_output = translations[self.current_language]["neutral_sentiment"]
                except ValueError:
                    sentiment = result.lower()
                    if "positive" in sentiment:
                        user_friendly_output = translations[self.current_language]["positive_sentiment"]
                    elif "negative" in sentiment:
                        user_friendly_output = translations[self.current_language]["negative_sentiment"]
                    elif "neutral" in sentiment:
                        user_friendly_output = translations[self.current_language]["neutral_sentiment"]
                    else:
                        user_friendly_output = translations[self.current_language]["unknown_sentiment_error"]
            
            elif selected_agent_name == "Named Entity Recognizer":
                try:
                    result_clean = result.replace("'", "\"").replace("None", "null")
                    result_dict = json.loads(result_clean)
                    if "type" in result_dict and result_dict["type"] == "function" and "response" in result_dict["parameters"]:
                        entities_data = result_dict["parameters"]["response"][0][1]
                    else:
                        entities_data = result_dict
                    entities = []
                    for key, value in entities_data.items():
                        if value and isinstance(value, list):
                            for item in value:
                                if self.current_language == "tr":
                                    item = fix_turkish_chars(item)
                                entities.append(f"{key}: {item}")
                    if entities:
                        user_friendly_output = translations[self.current_language]["entities_detected"].format(entities=", ".join(entities))
                    else:
                        user_friendly_output = translations[self.current_language]["entities_detected"].format(entities="None")
                except json.JSONDecodeError:
                    user_friendly_output = f"Hata: Çıktı işlenemedi. Ham sonuç: {result}"
            
            elif selected_agent_name == "Classification Agent":
                category = result
                if self.current_language == "tr":
                    category = fix_turkish_chars(category)
                category_map = translations[self.current_language]["classification_categories"]
                translated_category = category_map.get(category, category)
                user_friendly_output = translations[self.current_language]["classification_result"].format(category=translated_category)
            
            elif selected_agent_name == "Translation Agent":
                if self.current_language == "tr":
                    result = fix_turkish_chars(result)
                user_friendly_output = translations[self.current_language]["translation_result"].format(translated_text=result)
            
            elif selected_agent_name == "Summary Agent":
                try:
                    result_clean = result.replace("'", "\"").replace("None", "null")
                    result_dict = json.loads(result_clean)
                    summary = result_dict.get("summary", result)
                    key_points = result_dict.get("key_points", [])
                    if self.current_language == "tr":
                        summary = fix_turkish_chars(summary)
                        key_points = filter_key_points([fix_turkish_chars(kp) for kp in key_points], self.input_entry.text().strip())
                    elif self.current_language == "de":
                        key_points = filter_key_points([kp.replace("Blockchain-Technologie in ", "") for kp in key_points], self.input_entry.text().strip())
                    else:
                        key_points = filter_key_points(key_points, self.input_entry.text().strip())
                    key_points_str = ", ".join(key_points) if key_points else "None"
                    user_friendly_output = translations[self.current_language]["summary_result"].format(summary=summary, key_points=key_points_str)
                except json.JSONDecodeError:
                    summary_match = re.search(r"summary='(.*?)'", result)
                    key_points_match = re.search(r"key_points=\[(.*?)\]", result)
                    summary = summary_match.group(1) if summary_match else result
                    key_points = []
                    if key_points_match:
                        key_points = [item.strip().strip("'") for item in key_points_match.group(1).split(", ")]
                    if self.current_language == "tr":
                        summary = fix_turkish_chars(summary)
                        key_points = filter_key_points([fix_turkish_chars(kp) for kp in key_points], self.input_entry.text().strip())
                    elif self.current_language == "de":
                        key_points = filter_key_points([kp.replace("Blockchain-Technologie in ", "") for kp in key_points], self.input_entry.text().strip())
                    else:
                        key_points = filter_key_points(key_points, self.input_entry.text().strip())
                    key_points_str = ", ".join(key_points) if key_points else "None"
                    user_friendly_output = translations[self.current_language]["summary_result"].format(summary=summary, key_points=key_points_str)
            
            elif selected_agent_name == "Custom Agent":
                if self.current_language == "tr":
                    result = fix_turkish_chars(result)
                user_friendly_output = translations[self.current_language]["custom_result"].format(response=result)

        except json.JSONDecodeError:
            user_friendly_output = f"Hata: Çıktı işlenemedi. Ham sonuç: {result}"

        self.chat_textbox.append(f"You: {self.input_entry.text().strip()}\nAgent: {user_friendly_output}\n")
        self.input_entry.clear()
        self.loading_label.setText("")
        self.submit_btn.setEnabled(True)
        logger.debug("Sonuç işlendi, chat_textbox güncellendi: %s", user_friendly_output)

    def clear_chat_history(self):
        logger.debug("Sohbet geçmişi temizleniyor")
        self.chat_textbox.clear()
        self.last_result = ""

if __name__ == "__main__":
    try:
        logger.debug("Uygulama başlatılıyor")
        logger.debug("Python sürümü: %s", sys.version)
        app = QApplication(sys.argv)
        logger.debug("QApplication başlatıldı")
        window = IOAssistant()
        logger.debug("Uygulama çalışıyor")
        sys.exit(app.exec_())
    except Exception as e:
        logger.error("Uygulama başlatılırken hata: %s", str(e))
        sys.exit(1)