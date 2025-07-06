# 🧠 AI Hack Mentor Bot

> An intelligent assistant powered by IO.net's LLM agents to help developers navigate complex information with clarity.

## 🚀 What is AI Hack Mentor Bot?

AI Hack Mentor Bot is an open-source desktop application designed to assist developers by summarizing and analyzing complex content such as documentation, research papers, or articles. Built using the IO.net AI Agent infrastructure and powered by the Llama 3-70B Instruct model, it offers a user-friendly GUI with multi-language support (English, Turkish, German).

Ideal for:
- Developers participating in hackathons
- Summarizing technical documentation
- Mentoring teammates with dense information
- Translating technical terms across languages

## 📷 Screenshots

| Main Interface | Chat Output |
|----------------|-------------|
| ![Main Interface](https://github.com/user-attachments/assets/6f81ecc0-43cb-4ac2-ac25-1f7824d3bd66) | ![Chat Output](https://github.com/user-attachments/assets/8e629f39-a867-4133-9ba6-7cd508a1e181) |

## 🎥 Demo Video

https://youtu.be/ou2yVMcDXzM


Watch the demo: [AI Hack Mentor Bot Demo](https://github.com/user-attachments/assets/e7c8c6b7-8b6c-4e47-b8d7-ee9377b00503)

## ✨ Features

- 📚 **Summarization**: Condenses long technical texts into concise summaries with key points.
- 😊 **Sentiment Analysis**: Analyzes text sentiment (positive, negative, neutral).
- 🏷️ **Named Entity Recognition**: Identifies entities like people, organizations, and locations.
- 🛡️ **Content Moderation**: Detects inappropriate content (hate speech, harassment).
- 📊 **Text Classification**: Categorizes text into predefined labels.
- 🌐 **Translation**: Translates text into multiple languages (e.g., Spanish, English).
- ❓ **Custom Queries**: Handles flexible queries with tailored responses (e.g., explaining `io.net`).
- 🌍 **Multi-Language GUI**: Supports English, Turkish, and German interfaces.
- 🔗 **Social Media Integration**: Copy GitHub, Discord, and Twitter links with a click.
- 🧹 **Chat History Management**: Clear chat history with a dedicated button.
- 📜 **Robust Logging**: Detailed debug logs for troubleshooting.

## 💡 How It Works

The bot:
1. Launches a GUI for user interaction.
2. Allows selection of language (English, Turkish, German) and agent (e.g., Summary, Translation).
3. Accepts text or query input and processes it via the IO.net AI Agent API.
4. Returns structured responses in the chat area.
5. Supports clearing chat history and copying social media links.

## 🛠️ Tech Stack

- Python 3.12
- PyQt5 (GUI framework)
- IO.net AI Agents API (powered by Llama-3-70B-Instruct)
- deep-translator (multi-language translation)
- asyncio (asynchronous task execution)
- python-dotenv (environment variable management)

## 🔧 Installation

1. Clone the repository:
    ```bash
   git clone https://github.com/bysoclose/io-mentor-bot.git
   cd io-mentor-bot


2. Create and activate a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the mentor bot:
  ```bash
python io_mentor_bot.py
```

🔐 API Key Setup This project requires an IO.net API key:

```bash
Go to https://intelligence.io.solutions and log in.
Generate your API key.
Create a .env file in the project root with the following content:

IOINTEL_API_KEY=io-v2-xxxxxxxxxxxxxxxxxxxxxxxx
IO_LANGUAGE=tr
```

📄 Example Output
Summary Agent:
```bash
Input: Blockchain, merkezi olmayan bir veritabanı kullanarak işlemleri şifreler...
Output: Özet: Blockchain, merkezi olmayan bir veritabanı... Ana Noktalar: Blockchain, Merkezi, Olmayan
```
Translation Agent:
```bash
Input: İspanyolcaya çevir: Teknoloji, insanların hayatını kolaylaştırmak için sürekli gelişiyor.
Output: Çevrilen metin: La tecnología evoluciona constantemente para facilitar la vida de las personas.
```
Custom Agent:
```bash
Input: io.net nedir ?
Output: io.net, yapay zeka ve makine öğrenimi iş yükleri için merkezi olmayan bir hesaplama platformudur.
```

```bash
📁 Project Structure

io-mentor-bot/
├── io_mentor_bot.py        # Main application (GUI and logic)
├── workflow.py             # Agent task processing
├── utils.py               # Helper functions (e.g., parse_json_safely)
├── social_links.py        # Social media link integration
├── agents_config.py       # Agent definitions and translations
├── background.jpg         # GUI background image
├── corrections.json       # Turkish character corrections
├── languages.json         # Language settings
├── requirements.txt       # Dependencies
├── debug.log             # Application logs
├── .env                   # Environment variables (API key, language)
├── .gitignore            # Git exclusions
└── icons/                # Language and agent icons
    ├── uk.png
    ├── tr.png
    ├── de.png
    ├── github.png
    ├── discord.png
    ├── twitter.png
    ├── summary.png
    ├── sentiment.png
    ├── entity.png
    ├── moderation.png
    ├── classification.png
    ├── translation.png
    ├── custom.png
```
🪪 License

This project is open-source and licensed under the MIT License.

🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to open a pull request or submit an issue.

🌍 Credits

Made with ❤️ bysoclose (Bilal İbanoğlu) Powered by IO.net Intelligence API

Discord: Bilalibanoglu X (Twitter): @Bilal_ibanoglu
