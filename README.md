# Reddit Bot Using Groq AI

## Overview
This project is a Reddit bot that generates engaging content daily using Groq AI's API and posts it to a specified subreddit. It also includes functionality for commenting on other posts.

## Features
- **Daily Automated Posts**: The bot generates content and posts it to Reddit at a user-specified time.
- **AI Content Generation**: Uses the Groq AI API to create engaging text.
- **Error Handling and Logging**: Ensures smooth operation and logs any issues.
- **Bonus Feature**: Adds simple comments to existing posts in a subreddit.

## Prerequisites
Before running this bot, make sure you have:
- Python 3.7 or higher installed on your system.
- A Reddit account with API credentials (Client ID, Client Secret, Username, Password, and User Agent).
- A valid Groq AI API key.

## Installation
1. Clone this repository:
      git clone <repository_url>
   cd <repository_directory>
   
2. Install the required dependencies:
   pip install -r requirements.txt
   
## Configuration
1. Update the `app.py` file with your Reddit API credentials:
   
   REDDIT_CLIENT_ID = '<your_client_id>'
   REDDIT_CLIENT_SECRET = '<your_client_secret>'
   REDDIT_USERNAME = '<your_username>'
   REDDIT_PASSWORD = '<your_password>'
   REDDIT_USER_AGENT = '<your_user_agent>'
   

2. Update the file with your Groq AI API details:
   python
   GROQ_API_KEY = '<your_groq_api_key>'
   GROQ_API_URL = 'https://api.groq.ai/generate-content'
   

## Usage
1. Run the bot:
   bash
   python groqbot.py
   
2. The bot will execute daily at the scheduled time specified in the code.

## Files
- `groqbot.py`: The main script for the bot.
- `requirements.txt`: Lists the dependencies needed for the project.

## Sample Output
The bot will log its activity and errors in the console. A successful post example:

INFO - Successfully posted to r/test: Here's your daily dose of AI-generated content!


## Troubleshooting
- Ensure your API keys and credentials are correct.
- Verify that the Groq AI API URL is accessible.
- Check the logs for error messages and debug accordingly.

## Future Enhancements
- Improve the comment generation logic for more engaging interactions.
- Add support for scheduling multiple posts per day.
- Incorporate additional AI models for varied content generation.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

