![image](https://github.com/user-attachments/assets/6f81ecc0-43cb-4ac2-ac25-1f7824d3bd66)
![image](https://github.com/user-attachments/assets/8e629f39-a867-4133-9ba6-7cd508a1e181)


Video:
https://github.com/user-attachments/assets/e7c8c6b7-8b6c-4e47-b8d7-ee9377b00503


# 🧠 AI Hack Mentor Bot

> An intelligent assistant powered by IO.net's LLM agents to help developers navigate complex information with clarity.

## 🚀 What is AI Hack Mentor Bot?

AI Hack Mentor Bot is an open-source assistant designed to summarize and analyze complex content such as documentation, research papers, or articles. It is built using the IO.net AI Agent infrastructure and runs on the Llama 3-70B Instruct model.

Ideal for:
- Developers participating in hackathons  
- Summarizing technical documentation  
- Mentoring teammates with dense information  

## ✨ Features

- 📚 Summarizes long technical texts and documents  
- 💡 Continues and elaborates on topics using LLMs  
- 🔗 Connects to the [IO Intelligence API](https://intelligence.io.solutions/)  
- 🧑‍💻 Uses powerful models like `Llama-3-70B-Instruct`  
- ✅ Supports asynchronous execution for efficient performance  

## 💡 How It Works

The bot:
1. Accepts large input (text, documents, etc.)  
2. Sends the objective to an IO.net agent via API  
3. Uses a powerful AI model to extract key insights  
4. Returns a structured summary  

## 🛠️ Tech Stack

- Python 3.12  
- [IO.net AI Agents API](https://ai.io.net/ai/agents)  
- Llama-3.3-70B-Instruct model  
- Asyncio & Requests libraries  

## 🔧 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/bysoclose/io-mentor-bot.git
   cd io-mentor-bot
   ````

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ````

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ````

4. 🔐 **API Key Setup**
   This project requires an IO.net API key:

   * Go to [https://intelligence.io.solutions](https://intelligence.io.solutions) and log in.
   * Generate your API key.
   * Create a `.env` file in the project root with the following content:

     ````
     OPENAI_API_KEY=io-v2-xxxxxxxxxxxxxxxxxxxxxxxx
     ````

5. ▶️ Run the mentor bot:

   ```bash
   python io_mentor_bot.py
   ````

## 📄 Example Output

````
The global electric vehicle (EV) market has a rich history...  
From early inventions in the 1800s to Tesla's modern breakthroughs...
````

## 📁 Project Structure

````
io-mentor-bot/
├── io_mentor_bot.py        # Main script to execute tasks
├── app.py                  # Flask API (optional)
├── .env                    # API key (excluded from Git)
├── .gitignore              # Git exclusions
└── requirements.txt        # Dependencies
````

## 🪪 License

This project is open-source and licensed under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.
Feel free to open a pull request or submit an issue.

## 🌍 Credits

Made with ❤️ bysoclose (Bilal İbanoğlu)
Powered by IO.net Intelligence API

Discord: Bilalibanoglu
X (Twitter): @Bilal_ibanoglu

