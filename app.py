import praw
import schedule
import time
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Reddit API credentials
REDDIT_CLIENT_ID = 'b4P7VlM0ZIOl7nROFj8r-nw'
REDDIT_CLIENT_SECRET = 'tp-ex6nVcQyJWpT209wONvv0puUFrA'
REDDIT_USERNAME = 'Simran0305'
REDDIT_PASSWORD = 'simransmidel'
REDDIT_USER_AGENT = 'GroqContentBot/0.1'

# Groq API credentials
GROQ_API_KEY = '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'
GROQ_API_URL = 'https://api.groq.com/openai/v1/chat/completions'

# Initialize Reddit client
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD,
    user_agent=REDDIT_USER_AGENT
)

# Function to generate content using Groq AI
def generate_content():
    try:
        # Test API reachability
        test_response = requests.get(GROQ_API_URL)
        test_response.raise_for_status()
        
        # Make the actual API request
        response = requests.post(
            GROQ_API_URL,
            headers={
                'Authorization': f'Bearer {GROQ_API_KEY}',
                'Content-Type': 'application/json'
            },
            json={
                'prompt': 'Create an engaging Reddit post',
                'parameters': {
                    'length': 'medium'
                }
            }
        )
        response.raise_for_status()
        data = response.json()
        return data.get('content', 'Default fallback content if none provided')
    except requests.exceptions.RequestException as e:
        logging.error(f"Error generating content: {e}")
        return None

# Function to post content to Reddit
def post_to_reddit(subreddit_name, title, body):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        subreddit.submit(title, selftext=body)
        logging.info(f"Successfully posted to r/{subreddit_name}: {title}")
    except Exception as e:
        logging.error(f"Error posting to Reddit: {e}")

# Scheduled job to generate and post content
def daily_post():
    content = generate_content()
    if content:
        title = "Here's your daily dose of AI-generated content!"
        post_to_reddit('test', title, content)
    else:
        logging.warning("No content generated; skipping post.")

# Bonus: Simple comment generator
def generate_comment():
    return "This is an AI-generated comment!"

def comment_on_posts():
    try:
        for submission in reddit.subreddit('test').hot(limit=5):
            submission.comments[0].reply(generate_comment())
            logging.info(f"Commented on post: {submission.title}")
    except Exception as e:
        logging.error(f"Error commenting on posts: {e}")

# Set up daily schedule
schedule.every().day.at("23:04").do(daily_post)

if __name__ == "__main__":
    logging.info("Starting Reddit bot...")
    while True:
        schedule.run_pending()
        time.sleep(1)
