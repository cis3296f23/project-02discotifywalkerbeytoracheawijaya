import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import asyncio

# Load environment variables
load_dotenv()

# Set up Discord bot intents
intents = discord.Intents.default()
intents.message_content = True 

# Initialize Discord bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Initialize Spotify client with OAuth for user authentication
spotify_oauth = SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri="http://localhost:8888",  # Redirect URI for Spotify authentication
    scope="user-modify-playback-state user-read-playback-state"  # Spotify scopes for access
)

# Global variable to store Spotify access and refresh tokens
spotify_tokens = {
    'access_token': None,
    'refresh_token': None
}

@bot.event
async def on_ready():
    """ Event triggered when bot is ready """
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    """ Command to greet the user """
    await ctx.send(f'Hello, {ctx.author.mention}!')

@bot.command(name='auth', help='Authenticate with Spotify')
async def authenticate(ctx):
    """ Command to handle Spotify authentication """
    # Generate and send authentication URL
    auth_url = spotify_oauth.get_authorize_url()
    await ctx.send(f"Please authenticate with Spotify here: {auth_url}")

    await ctx.send("Please paste the callback URL after authentication.")

    # Wait for user's response
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        message = await bot.wait_for('message', check=check, timeout=300)  # 5 minutes timeout
        callback_url = message.content
        code = spotify_oauth.parse_response_code(callback_url)
        token_info = spotify_oauth.get_access_token(code)
        spotify_tokens['access_token'] = token_info['access_token']
        spotify_tokens['refresh_token'] = token_info['refresh_token']
        await ctx.send("Authenticated successfully with Spotify.")
    except asyncio.TimeoutError:
        await ctx.send("Authentication timeout. Please try again.")

async def refresh_spotify_token():
    """ Helper function to refresh Spotify token """
    global spotify_tokens
    token_info = spotify_oauth.refresh_access_token(spotify_tokens['refresh_token'])
    spotify_tokens['access_token'] = token_info['access_token']

@bot.command(name='play', help='play a track on Spotify by name, name and artist, or Spotify URL.')
async def play(ctx, *, query: str):
    """ Command to play a track on Spotify """
    if spotify_tokens['access_token'] is None:
        await ctx.send("You need to authenticate with Spotify first.")
        return

    await refresh_spotify_token()

    spotify = spotipy.Spotify(auth=spotify_tokens['access_token'])

    try:
        devices = spotify.devices()
        device_id = devices['devices'][0]['id'] if devices['devices'] else None

        if query.startswith('https://open.spotify.com/track/'):
            track_id = query.split('/')[-1].split('?')[0]
            track = spotify.track(track_id)
        else:
            results = spotify.search(q=query, type='track', limit=1)
            if not results['tracks']['items']:
                await ctx.send("Sorry, I couldn't find that track.")
                return
            track = results['tracks']['items'][0]
            track_id = track['id']

        track_name = track['name']
        track_url = track['external_urls']['spotify']
        requester = ctx.author.mention

        spotify.start_playback(device_id=device_id, uris=[f'spotify:track:{track_id}'])
        await ctx.send(f'Now playing "{track_name}"\nRequested by: {requester}\nTrack URL: {track_url}')
    except spotipy.exceptions.SpotifyException as e:
        await ctx.send("An error occurred: " + str(e))
#pause the mussic
@bot.command(name='pause', help='Pause playback on Spotify')
async def pause(ctx):
    """ Command to pause playback on Spotify """
    if spotify_tokens['access_token'] is None:
        await ctx.send("You need to authenticate with Spotify first.")
        return

    await refresh_spotify_token()

    spotify = spotipy.Spotify(auth=spotify_tokens['access_token'])

    try:
        devices = spotify.devices()
        device_id = devices['devices'][0]['id'] if devices['devices'] else None

        if device_id:
            spotify.pause_playback(device_id=device_id)
            await ctx.send("Playback paused on your Spotify device.")
        else:
            await ctx.send("No available Spotify devices found.")
    except spotipy.exceptions.SpotifyException as e:
        await ctx.send("An error occurred: " + str(e))

#resumes the music 
@bot.command(name='start', help='Resume playback on Spotify')
async def start(ctx):
    """ Command to resume playback on Spotify """
    if spotify_tokens['access_token'] is None:
        await ctx.send("You need to authenticate with Spotify first.")
        return

    await refresh_spotify_token()

    spotify = spotipy.Spotify(auth=spotify_tokens['access_token'])

    try:
        devices = spotify.devices()
        device_id = devices['devices'][0]['id'] if devices['devices'] else None

        if device_id:
            spotify.start_playback(device_id=device_id)
            await ctx.send("Playback resumed on your Spotify device.")
        else:
            await ctx.send("No available Spotify devices found.")
    except spotipy.exceptions.SpotifyException as e:
        await ctx.send("An error occurred: " + str(e))

@bot.command(name='next', help='Skip to the next track on Spotify')
async def next_track(ctx):
    """ Command to skip to the next track on Spotify """
    if spotify_tokens['access_token'] is None:
        await ctx.send("You need to authenticate with Spotify first.")
        return

    await refresh_spotify_token()

    spotify = spotipy.Spotify(auth=spotify_tokens['access_token'])

    try:
        devices = spotify.devices()
        device_id = devices['devices'][0]['id'] if devices['devices'] else None

        if device_id:
            spotify.next_track(device_id=device_id)
            # Waiting for track to change
            await asyncio.sleep(1)
            current_track = spotify.current_playback()
            if current_track and current_track['item']:
                track_url = current_track['item']['external_urls']['spotify']
                await ctx.send(f"Skipped to the next track: {track_url}")
            else:
                await ctx.send("Skipped to the next track.")
        else:
            await ctx.send("No available Spotify devices found.")
    except spotipy.exceptions.SpotifyException as e:
        await ctx.send("An error occurred: " + str(e))

@bot.command(name='previous', help='Skip to the previous track on Spotify')
async def previous_track(ctx):
    """ Command to skip to the previous track on Spotify """
    if spotify_tokens['access_token'] is None:
        await ctx.send("You need to authenticate with Spotify first.")
        return

    await refresh_spotify_token()

    spotify = spotipy.Spotify(auth=spotify_tokens['access_token'])

    try:
        devices = spotify.devices()
        device_id = devices['devices'][0]['id'] if devices['devices'] else None

        if device_id:
            spotify.previous_track(device_id=device_id)
            # Waiting for track to change
            await asyncio.sleep(1)
            current_track = spotify.current_playback()
            if current_track and current_track['item']:
                track_url = current_track['item']['external_urls']['spotify']
                await ctx.send(f"Skipped to the previous track: {track_url}")
            else:
                await ctx.send("Skipped to the previous track.")
        else:
            await ctx.send("No available Spotify devices found.")
    except spotipy.exceptions.SpotifyException as e:
        await ctx.send("An error occurred: " + str(e))

@bot.command(name='devices', help='List available Spotify devices')
async def devices(ctx):
    """ Command to list available Spotify devices """
    if spotify_tokens['access_token'] is None:
        await ctx.send("You need to authenticate with Spotify first.")
        return

    spotify = spotipy.Spotify(auth=spotify_tokens['access_token'])

    try:
        results = spotify.devices()
        device_list = [device['name'] for device in results['devices']] if results['devices'] else []
        await ctx.send(f"Available devices: {', '.join(device_list)}" if device_list else "No available devices found.")
    except Exception as e:
        await ctx.send("An error occurred: " + str(e))

bot.remove_command('help')  # Remove the default help command
@bot.command(name='help', help='Show available commands')
async def show_help(ctx):
    """ Command to list available commands"""
    command_list = [f'!{command.name}' for command in bot.commands if not command.hidden]
    await ctx.send('Available commands: \n' + '\n'.join(command_list))
    
# Run the bot
token = os.getenv('DISCORD_TOKEN')
bot.run(token)