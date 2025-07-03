import requests

api_key = os.environ["OPENAI_API_KEY"]  # .env ya da sistem değişkeninden gelsin
AGENT_ID = "SENIN_AGENT_IDIN"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "messages": [
        {"role": "user", "content": "Hackathona nasıl katılırım?"}
    ],
    "agent_id": AGENT_ID
}

response = requests.post("https://api.io.net/v1/agent-chat", headers=headers, json=data)
print("Yanıt:", response.json())


import customtkinter as ctk
import asyncio
import pyperclip
from PIL import Image, ImageTk

# Tema ayarları
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Ana pencere
app = ctk.CTk()
app.geometry("720x400")
app.title("IO Mentor Link Paneli")

# 🔹 Arka plan resmi yükle
bg_image = Image.open("background.png").resize((720, 400))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = ctk.CTkLabel(app, image=bg_photo, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# 🔹 Kopyalama işlevi
def on_click_copy(event, textbox):
    text = textbox.get("0.0", "end-1c")
    pyperclip.copy(text)
    status_label.configure(text=f"Kopyalandı: {text}")

# 🔹 Link kutusu oluşturucu
def create_link_box(label_text, url, y_pos):
    label = ctk.CTkLabel(app, text=label_text, width=100, anchor="w", fg_color="transparent")
    label.place(x=40, y=y_pos)

    textbox = ctk.CTkTextbox(app, height=25, width=500)
    textbox.insert("0.0", url)
    textbox.configure(state="disabled")
    textbox.place(x=150, y=y_pos)
    textbox.bind("<Button-1>", lambda e: on_click_copy(e, textbox))

    return textbox

# 🔹 Tema değiştirme
def toggle_theme():
    mode = ctk.get_appearance_mode()
    ctk.set_appearance_mode("light" if mode == "dark" else "dark")

# 🔹 Tema butonu
theme_button = ctk.CTkButton(app, text="Tema Değiştir", command=toggle_theme)
theme_button.place(x=40, y=20)

# 🔹 Link kutuları
create_link_box("GitHub:", "https://github.com/bysoclose/io-mentor-bot", 80)
create_link_box("Discord:", "https://discord.gg/cXN3WghNhG", 130)
create_link_box("Twitter:", "https://twitter.com/bilal_ibanoglu", 180)

# 🔹 Kopyalandı bildirimi
status_label = ctk.CTkLabel(app, text="", text_color="gray", fg_color="transparent")
status_label.place(x=40, y=230)

# 🔁 Async Main Loop
async def main_loop():
    while True:
        app.update()
        await asyncio.sleep(0.01)

asyncio.run(main_loop())
