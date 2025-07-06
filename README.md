🧠 AI Hack Mentor Bot

An intelligent assistant powered by IO.net's LLM agents to help developers navigate complex information with clarity.

🚀 What is AI Hack Mentor Bot?
AI Hack Mentor Bot is an open-source desktop application designed to assist developers by summarizing and analyzing complex content such as documentation, research papers, or articles. Built using the IO.net AI Agent infrastructure and powered by the Llama 3-70B Instruct model, it offers a user-friendly GUI with multi-language support (English, Turkish, German).
Ideal for:

Developers participating in hackathons
Summarizing technical documentation
Mentoring teammates with dense information
Translating technical terms across languages

✨ Features

📚 Summarization: Condenses long technical texts into concise summaries with key points.
😊 Sentiment Analysis: Analyzes text sentiment (positive, negative, neutral).
🏷️ Named Entity Recognition: Identifies entities like people, organizations, and locations.
🛡️ Content Moderation: Detects inappropriate content (hate speech, harassment).
📊 Text Classification: Categorizes text into predefined labels.
🌐 Translation: Translates text into multiple languages (e.g., Spanish, English).
❓ Custom Queries: Handles flexible queries with tailored responses (e.g., explaining io.net).
🌍 Multi-Language GUI: Supports English, Turkish, and German interfaces.
🔗 Social Media Integration: Copy GitHub, Discord, and Twitter links with a click.
🧹 Chat History Management: Clear chat history with a dedicated button.
📜 Robust Logging: Detailed debug logs for troubleshooting.

📷 Screenshots



Main Interface
Chat Output







🎥 Demo Video
Watch the demo: AI Hack Mentor Bot Demo
💡 How It Works

Launch the application to access the GUI.
Select a language (English, Turkish, German) and an agent (e.g., Summary, Translation).
Input text or a query and click "Send."
The selected agent processes the input using the IO.net AI Agent API and returns a structured response.
View results in the chat area, clear history if needed, or copy social media links.

🛠️ Tech Stack

Python: 3.12
PyQt5: For the GUI
IO.net AI Agents API: Powered by Llama-3-70B-Instruct
deep-translator: For multi-language translation
asyncio: For asynchronous task execution
python-dotenv: For environment variable management

🔧 Installation

Clone the repository:
git clone https://github.com/bysoclose/io-mentor-bot.git
cd io-mentor-bot


Create and activate a virtual environment (recommended):
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Install dependencies:
pip install -r requirements.txt


🔐 API Key Setup:

Go to https://intelligence.io.solutions and log in.
Generate your API key.
Create a .env file in the project root:IOINTEL_API_KEY=your_api_key_here
IO_LANGUAGE=tr




Run the application:
python io_mentor_bot.py



📄 Example Usage

Summary Agent:
Input: Blockchain, merkezi olmayan bir veritabanı kullanarak işlemleri şifreler...
Output: Özet: Blockchain, merkezi olmayan bir veritabanı... Ana Noktalar: Blockchain, Merkezi, Olmayan


Translation Agent:
Input: İspanyolcaya çevir: Teknoloji, insanların hayatını kolaylaştırmak için sürekli gelişiyor.
Output: Çevrilen metin: La tecnología evoluciona constantemente para facilitar la vida de las personas.


Custom Agent:
Input: io.net nedir ?
Output: io.net, yapay zeka ve makine öğrenimi iş yükleri için merkezi olmayan bir hesaplama platformudur.



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
├── .env                  # Environment variables (API key, language)
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

🪪 License
This project is licensed under the MIT License. See the LICENSE file for details.
🤝 Contributing
Contributions, issues, and feature requests are welcome! To contribute:

Fork the repository.
Create a new branch: git checkout -b feature/your-feature
Commit your changes: git commit -m "Add your feature"
Push to the branch: git push origin feature/your-feature
Open a pull request.

🌍 Credits
Made with ❤️ by bysoclose (Bilal İbanoğlu)Powered by IO.net Intelligence API  
Contact:  

Discord: Bilalibanoglu  
X (Twitter): @Bilal_ibanoglu
