# Jarvis AI Voice Assistant

Jarvis is a Python-based AI voice assistant that can listen to voice commands, speak responses, open websites, launch applications, perform searches across multiple platforms, and answer questions using a Large Language Model (LLM).

## Features

* 🎙️ Voice Recognition
* 🔊 Text-to-Speech Responses
* 🌐 Open Websites with Voice Commands
* 💻 Launch Desktop Applications
* 🔎 Search Google, YouTube, GitHub, Wikipedia, Reddit, and more
* 🤖 AI-Powered Chatbot
* ⚡ Fast Command Processing
* 🎯 Wake Word Activation ("Jarvis")

## Supported Commands

### Open Websites

* Open Google
* Open YouTube
* Open Facebook
* Open Instagram
* Open Reddit
* Open GitHub
* Open LinkedIn
* Open Gmail
* Open Google Maps
* Open Spotify
* And many more...

### Open Applications

* Open Chrome
* Open Edge
* Open Firefox
* Open VS Code
* Open Notepad
* Open Calculator
* Open Paint
* Open Command Prompt
* Open PowerShell
* Open File Explorer
* Microsoft Office Apps

### Search Commands

Examples:

* Search Python tutorials on YouTube
* Search AI news on Google
* Search machine learning on GitHub
* Search Python documentation on Stack Overflow

### AI Chat

Examples:

* Jarvis, how are you?
* Jarvis, explain recursion.
* Jarvis, write a Python function to reverse a string.
* Jarvis, what is a vector database?

## Technologies Used

* Python
* SpeechRecognition
* PyAudio
* pyttsx3
* Groq API
* WebBrowser Module

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/jarvis.git
cd jarvis
```

### Install Dependencies

```bash
pip install SpeechRecognition
pip install PyAudio
pip install pyttsx3
pip install groq
```

Or:

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Never commit your API keys to GitHub.

### Run Jarvis

```bash
python main.py
```

## Project Structure

```text
jarvis/
│
├── main.py
├── Models/chat_bot.py
├── Models/search_correct.py
├── Models/command_identifier
├── History/history.json
|── requirements.txt
├── .env
└── README.md
```

## Future Improvements

* Wake Word Detection without saying "Jarvis" every time
* Conversation Memory
* AI Agent Capabilities
* File Management Commands
* Email Automation
* Calendar Integration
* Weather Information
* Smart Home Control

## Contributing

Contributions, feature requests, and improvements are welcome.

## License

This project is open source and available under the MIT License.

## Author

Built by M. Fasil Ali.
