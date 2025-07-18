# 🤖 LIVE_KIT_JARVIS - Friday AI Assistant

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![LiveKit](https://img.shields.io/badge/LiveKit-Agents-green.svg)](https://livekit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Friday** is an AI-powered personal assistant inspired by the iconic AI from Iron Man. Built with LiveKit Agents and Google's Realtime AI, Friday provides real-time voice interaction with a sophisticated, sarcastic personality that makes everyday tasks more engaging.

## ✨ Features

- 🎭 **Iron Man-inspired Personality**: Classy butler with witty, sarcastic responses
- 🌤️ **Weather Information**: Get current weather for any city
- 🔍 **Web Search**: Search the internet using DuckDuckGo
- 📧 **Email Integration**: Send emails through Gmail
- 🎙️ **Real-time Voice**: Natural voice conversations with Google's Realtime AI
- 🔇 **Noise Cancellation**: Enhanced audio quality with LiveKit's noise cancellation
- 📱 **Video Support**: Full video calling capabilities

## 🏗️ Project Structure

```
LIVE_KIT_JARVIS/
├── src/                    # Source code
│   ├── __init__.py
│   ├── agent.py           # Main agent implementation
│   └── tools.py           # AI tools (weather, search, email)
├── config/                # Configuration files
│   ├── __init__.py
│   └── prompt.py          # AI personality prompts
├── docs/                  # Documentation
├── main.py               # Main entry point
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not tracked)
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- LiveKit account and API keys
- Google Cloud account with Realtime AI access
- Gmail account with App Password (for email functionality)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Prathamsimgh/Live_kit_Friday.git
   cd Live_kit_Friday
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the root directory:

   ```env
   # LiveKit Configuration
   LIVEKIT_URL=your_livekit_url
   LIVEKIT_API_KEY=your_api_key
   LIVEKIT_API_SECRET=your_api_secret

   # Google Cloud Configuration
   GOOGLE_APPLICATION_CREDENTIALS=path/to/your/credentials.json

   # Gmail Configuration (for email functionality)
   GMAIL_USER=your_email@gmail.com
   GMAIL_APP_PASSWORD=your_app_password
   ```

4. **Run Friday**
   ```bash
   python main.py
   ```

## 🛠️ Configuration

### Environment Variables

| Variable                         | Description                           | Required |
| -------------------------------- | ------------------------------------- | -------- |
| `LIVEKIT_URL`                    | Your LiveKit server URL               | ✅       |
| `LIVEKIT_API_KEY`                | LiveKit API key                       | ✅       |
| `LIVEKIT_API_SECRET`             | LiveKit API secret                    | ✅       |
| `GOOGLE_APPLICATION_CREDENTIALS` | Path to Google Cloud credentials      | ✅       |
| `GMAIL_USER`                     | Gmail address for email functionality | ⚠️       |
| `GMAIL_APP_PASSWORD`             | Gmail App Password                    | ⚠️       |

⚠️ = Required only for email functionality

### Gmail Setup

To enable email functionality:

1. Enable 2-Factor Authentication on your Google account
2. Generate an App Password:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate a password for "Mail"
3. Use this App Password in your `.env` file

## 🎯 Available Commands

Friday responds to natural language and can perform these actions:

- **Weather**: "What's the weather in New York?"
- **Search**: "Search for the latest AI news"
- **Email**: "Send an email to john@example.com about the meeting"
- **General conversation**: Friday will respond with his characteristic wit

## 🎭 Personality

Friday is designed with a sophisticated personality:

- **Classy Butler**: Professional yet approachable
- **Sarcastic Wit**: Adds humor to interactions
- **Concise Responses**: Gets to the point quickly
- **Acknowledgment Style**: Uses phrases like "Will do, Sir" and "Roger Boss"

## 🔧 Development

### Adding New Tools

To add new functionality:

1. Create a new function in `src/tools.py`
2. Decorate it with `@function_tool()`
3. Add it to the tools list in `src/agent.py`

Example:

```python
@function_tool()
async def new_tool(context: RunContext, parameter: str) -> str:
    """Description of what this tool does."""
    # Your implementation here
    return "Result"
```

### Customizing Personality

Modify the prompts in `config/prompt.py`:

- `AGENT_INSTRUCTION`: Core personality traits
- `SESSION_INSTRUCTION`: Session-specific behavior

## 📋 Dependencies

- **livekit-agents**: Core LiveKit agents framework
- **livekit-plugins-google**: Google AI integration
- **livekit-plugins-noise-cancellation**: Audio enhancement
- **duckduckgo-search**: Web search functionality
- **requests**: HTTP requests for weather API
- **python-dotenv**: Environment variable management

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the AI assistant from Iron Man
- Built with [LiveKit](https://livekit.io/) real-time communication platform
- Powered by Google's Realtime AI technology
- Weather data from [wttr.in](https://wttr.in/)
- Web search via [DuckDuckGo](https://duckduckgo.com/)

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/Prathamsimgh/Live_kit_Friday/issues) page
2. Create a new issue with detailed information
3. Join the LiveKit community for technical support

---

**"Just like Jarvis, but with more attitude."** - Friday 🤖
