# 🛠️ Setup Guide for Friday AI Assistant

This guide will walk you through setting up Friday, your AI personal assistant, step by step.

## 📋 Prerequisites

Before you begin, make sure you have:

- Python 3.8 or higher installed
- Git installed on your system
- A LiveKit account
- A Google Cloud account with AI services enabled
- A Gmail account (for email functionality)

## 🔧 Step-by-Step Setup

### 1. Clone and Install

```bash
# Clone the repository
git clone https://github.com/Prathamsimgh/Live_kit_Friday.git
cd Live_kit_Friday

# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. LiveKit Setup

1. **Create a LiveKit Account**

   - Go to [LiveKit Cloud](https://cloud.livekit.io/)
   - Sign up for a free account
   - Create a new project

2. **Get Your Credentials**
   - In your LiveKit dashboard, go to Settings → Keys
   - Copy your:
     - LiveKit URL
     - API Key
     - API Secret

### 3. Google Cloud Setup

1. **Create a Google Cloud Project**

   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one

2. **Enable Required APIs**

   - Enable the "Cloud Speech-to-Text API"
   - Enable the "Cloud Text-to-Speech API"
   - Enable any other AI services you plan to use

3. **Create Service Account**
   - Go to IAM & Admin → Service Accounts
   - Create a new service account
   - Download the JSON credentials file
   - Save it securely in your project directory

### 4. Gmail Setup (Optional)

If you want email functionality:

1. **Enable 2-Factor Authentication**

   - Go to your Google Account settings
   - Enable 2-Factor Authentication

2. **Generate App Password**
   - Go to Security → 2-Step Verification → App passwords
   - Select "Mail" as the app
   - Generate and copy the 16-character password

### 5. Environment Configuration

Create a `.env` file in the root directory:

```env
# LiveKit Configuration
LIVEKIT_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=your_api_key_here
LIVEKIT_API_SECRET=your_api_secret_here

# Google Cloud Configuration
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/credentials.json

# Gmail Configuration (Optional)
GMAIL_USER=your_email@gmail.com
GMAIL_APP_PASSWORD=your_16_character_app_password
```

### 6. Test Your Setup

```bash
# Run Friday
python main.py
```

If everything is configured correctly, you should see:

```
🤖 Starting Friday - Your AI Personal Assistant...
📡 Connecting to LiveKit...
```

## 🔍 Troubleshooting

### Common Issues

**1. Import Errors**

```bash
# Make sure you're in the virtual environment
pip install -r requirements.txt
```

**2. LiveKit Connection Issues**

- Verify your LiveKit URL format (should start with `wss://`)
- Check that your API key and secret are correct
- Ensure your LiveKit project is active

**3. Google Cloud Authentication**

- Verify the path to your credentials JSON file
- Ensure the service account has the necessary permissions
- Check that required APIs are enabled

**4. Email Functionality Not Working**

- Verify 2-Factor Authentication is enabled
- Use the App Password, not your regular Gmail password
- Check that the Gmail username is correct

### Getting Help

If you encounter issues:

1. Check the console output for error messages
2. Verify all environment variables are set correctly
3. Test each component individually
4. Check the [Issues](https://github.com/Prathamsimgh/Live_kit_Friday/issues) page

## 🚀 Next Steps

Once Friday is running:

1. **Test Basic Functionality**

   - Try asking about the weather
   - Test web search capabilities
   - Send a test email (if configured)

2. **Customize Friday**

   - Modify prompts in `config/prompt.py`
   - Add new tools in `src/tools.py`
   - Adjust personality settings

3. **Deploy to Production**
   - Consider using Docker for deployment
   - Set up proper logging
   - Configure monitoring

## 📚 Additional Resources

- [LiveKit Documentation](https://docs.livekit.io/)
- [Google Cloud AI Documentation](https://cloud.google.com/ai)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)

---

**Ready to meet Friday? Let's get started! 🤖**
