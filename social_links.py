from PyQt5.QtWidgets import QHBoxLayout, QLabel, QPushButton, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from agents_config import translations
import os

def create_social_links(parent, current_language, copy_to_clipboard):
    social_widget = QWidget()  # Yeni bir QWidget oluştur
    social_layout = QHBoxLayout()  # Layout'u widget içine yerleştir
    social_widget.setLayout(social_layout)

    social_label = QLabel(translations[current_language]["social_label"])
    social_label.setStyleSheet("font-size: 16px; color: white;")
    social_layout.addWidget(social_label)

    social_platforms = [
        ("GitHub", "https://github.com/bysoclose/io-mentor-bot", "icons/github.png"),
        ("Discord", "https://discord.gg/VDE6VBwX6z", "icons/discord.png"),
        ("Twitter", "https://x.com/Bilal_ibanoglu", "icons/twitter.png")
    ]

    for platform, url, icon_path in social_platforms:
        if os.path.exists(icon_path):
            button = QPushButton()
            button.setIcon(QIcon(icon_path))
            button.setStyleSheet("background-color: #162447; border: none;")
            button.setFixedSize(24, 24)
            button.clicked.connect(lambda checked, u=url: copy_to_clipboard(u, current_language))
            social_layout.addWidget(button)
        else:
            print(f"Warning: Icon not found - {icon_path}")

    social_layout.addStretch()
    return social_widget  # QWidget döndür