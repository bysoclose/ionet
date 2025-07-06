from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap  # QPixmap eklendi
from PyQt5.QtCore import QSize  # QSize eklendi
import os

def create_social_links(parent, current_language, copy_to_clipboard):
    widget = QWidget(parent)
    layout = QHBoxLayout(widget)
    layout.setContentsMargins(0, 0, 0, 0)  # Kenar boşluklarını sıfırla
    layout.setSpacing(10)  # Iconlar arası mesafe

    links = {
        "GitHub": "https://github.com/bysoclose/io-mentor-bot",
        "Discord": "https://discord.gg/cXN3WghNhG",
        "Twitter": "https://twitter.com/bilal_ibanoglu"
    }
    icons = {
        "GitHub": "icons/github.png",
        "Discord": "icons/discord.png",
        "Twitter": "icons/twitter.png"
    }

    for name, url in links.items():
        icon_path = icons[name]
        if os.path.exists(icon_path):
            icon = QIcon(icon_path)
            if not icon.isNull():
                label = QLabel(widget)
                label.setPixmap(icon.pixmap(QSize(32, 32)))  # Sabit icon boyutu
                label.setToolTip(url)
                label.mousePressEvent = lambda e, u=url, n=name: copy_to_clipboard(u, current_language)
                layout.addWidget(label)
            else:
                print(f"Invalid icon: {icon_path}")
        else:
            print(f"Icon not found: {icon_path}")

    layout.addStretch()  # Sağ tarafı esnet
    widget.setLayout(layout)
    return widget