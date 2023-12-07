import discord
from requests import post
import base64
import json
from discord import SyncWebhook, Colour
from datetime import datetime
import os
from dotenv import load_dotenv
import logging

# initializing logging at the start
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# A class for interacting with Discord webhooks
class Discord:
    """
    A class for interacting with Discord webhooks.

    This class provides methods to send messages to a Discord channel using webhooks.
    It is initialized with a webhook URL and offers functionality to format and 
    send messages in a streamlined manner.

    Attributes:
        webhook_url (str): The URL of the Discord webhook used to send messages.
    """
    def __init__(self) -> None:
        """
        Initializes the Discord class with a given webhook URL.
        """
        self.webhook_url = "https://discord.com/api/webhooks/1172199875421675652/Amb011OU5QzJ4AY-XjF9k7JkkZZcYHdnhSVG-nkAfloLv4OwZ9Gvpd2J822JRbdABSGW"

    def send_webhook(self, message_description: str) -> None:
        """
        Sends a message to the Discord channel associated with the webhook.

        Args:
            message_description (str): The message to be sent to the Discord channel.
        """
        # Create webhook from url
        webhook = SyncWebhook.from_url(self.webhook_url)

        # Embed message to send
        embed = discord.Embed(
            title="Spotify Info",
            description=message_description,
            colour=Colour.red(),
            timestamp=datetime.now()
        )

        # Send payload to webhook url
        webhook.send(embed=embed)

 # Load environment variables from the .env file
load_dotenv() 
# Spotify Client ID and Secret (Would never post in code would use env variable or some key management host)
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

if not client_id or not client_secret:
    print("Error: Spotify client ID or secret not found in environment variables.")
    exit(1)

def get_access_token():
    """
    Retrieves the access token from the Spotify API for authentication purposes
    """
    try:
        # Build authorization string
        authorization_string = client_id + ":" + client_secret
        authorization_bytes = authorization_string.encode('utf-8')
        authorization_base64 = str(base64.b64encode(authorization_bytes), 'utf-8')

        # Build payload to send
        token_url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": "Basic " + authorization_base64,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials"
        }

        # Send payload and retrieve access token
        query = post(token_url, headers=headers, data=data)
        json_data = json.loads(query.content)
        access_token = json_data["access_token"]
        logging.info("Access token received.")
        return access_token
    except Exception as e:
        logging.error(f"Error getting access token: {e}")
        return None

# Get access token
access_token = get_access_token()
discord_bot = Discord()

# Sends tokens to discord and show logging information if an error or not has happened.
if access_token:
    try:
        discord_bot.send_webhook(access_token)
        logging.info("Access token sent to discord.")
    except Exception as e:
        logging.error(f"Error sending token to Discord: {e}")
else:
    logging.error("Access token not retrieved, cannot send to Discord.")

# Send token to discord
#message = "Testing by Par!"
# compiles and works for Adam after a grueling troubleshooting session
# discord_bot = Discord()
## Send the access token to the Discord webhook
# discord_bot.send_webhook(access_token)
#discord_bot.send_webhook(message)
for i in range(10):
    print("Successfully send token to discord webhook!\n")