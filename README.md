# Discotify
Discotify is a Discord/Spotify bot solution to enhance user experiences when listening to Spotify music in Discord parties. Our Discord bot solution allows multiple people to control Spotify listening parties instead of a single person. Your listening experience can now become fun and collaborative!
Users who would benefit most from this program would be users who have Spotify premium and actively use Discord with friends or other people.
Once users are in Discord and in each others Spotify listening parties, users can send commands to the bot. These commands include but are not limited to actions such as start track, pause track, skip track, and add to queue.

# General Commands
1. `!hello` : Greets the user.
2. `!auth` : Initiates authentication with Spotify.
3. `!help` : Displays a list of avaiable commands.

# Spotify Playback Control
1. `!play <query>` : plays a track on Spotify. The `<query>` can be a Spotify link, song name, or song name with the artist.
2. `!pause` : Pauses the current playback on Spotify.
3. `!resume` : Resumes playback on Spotify.
4. `!next` : Skips to the next track on Spotify.
5. `!previous` : Goes to the previous track on Spotify
6. `!devices` : Lists avaiable Spotify devices.

# Spotify User Data
1. `!toptracks` : Shows the user's top 10 tracks on Spotify.
2. `!playlist <name>` : Plays a playlist from the user's library on Spotify by playlist name.
3. `!profile` : Show user Spotify profile

## Create a Discord Bot Account

1. **Go to the Discord Developer Portal**: Open your web browser and navigate to the [Discord Developer Portal](https://discord.com/developers/applications).

2. **Create a New Application**: Click on the `New Application` button. Give your application a name and confirm the creation.
   <img width="2056" alt="Screenshot 2023-12-02 at 3 15 41 PM" src="https://github.com/cis3296f23/project-02discotifywalkerbeytoracheawijaya/assets/79390380/0218dfa0-c533-4b04-a921-1fac253ccf27">

3. **Create a Bot User**: Within your application, find the `Bot` tab and click on `Add Bot`. Confirm the creation of the bot. <br />
    <img width="349" alt="Screenshot 2023-12-02 at 3 21 38 PM" src="https://github.com/cis3296f23/project-02discotifywalkerbeytoracheawijaya/assets/79390380/bf07680a-b349-4a0e-aa99-00249f0cc21b">

4. **Enable Intents**: In the bot tab, you will see options for `Privileged Gateway Intents`
   <img width="1393" alt="Screenshot 2023-12-02 at 3 32 53 PM" src="https://github.com/cis3296f23/project-02discotifywalkerbeytoracheawijaya/assets/79390380/3fc77a98-14ea-47b8-bb22-af8bcc750561">

## Get Your Bot Token

1. **Access the Bot Tab**: In your application, navigate to the `Bot` tab.
   
2. **Copy the Token**: Under the `Build-A-Bot` section, you’ll see a token. Click on `Reset Token` to reset your bot's token and copy bot's token. Keep this token secure, as it allows anyone to control your bot.
   <img width="1377" alt="Screenshot 2023-12-02 at 3 32 02 PM" src="https://github.com/cis3296f23/project-02discotifywalkerbeytoracheawijaya/assets/79390380/c85bb316-2590-40d0-8aac-96766f11ac77">


## Invite the Bot to Your Server

1. **Generate the Invite Link**: Go to the `OAuth2` tab in your application. Under `Scopes`, select `bot`. Then, under `Bot Permissions`, choose the permissions you want your bot to have.

2. **Copy and Use the Invite Link**: Copy the generated link and paste it into your web browser. Select the server to which you want to add the bot and authorize it.
    <img width="2056" alt="Screenshot 2023-12-02 at 3 40 25 PM" src="https://github.com/cis3296f23/project-02discotifywalkerbeytoracheawijaya/assets/79390380/f1384395-cf1b-46d4-8a2e-4f6d6272448b">

# How to run

**MacOS:**

1. Ensure you have python3 installed on your system. 
    - To check that python is installed properly run this command in your terminal:
        ```
        python --version
        ```
    - If the previous commands does not work try:
        ```
        python3 --version
        ```
    - If the command is successful you will see your current python version installed
    - You need Python 3.11 and greater to run this program 

2. Open a terminal or command prompt.

3. Use the following command to install the required modules using pip, the package installer for Python:

        pip install discord requests

4. Wait for the installation to complete. Once finished, the required modules will be installed in the Python environment.

5. Download executable from release in Repo **bot**

6. Set up environment variables
    - In the same directory the executable is located, create a .env file
    ```
        nano .env
    ``` 
    - Set your Client ID and Client Secret in the following format ([How to find Client ID and Client Secret](https://developer.spotify.com/documentation/web-api/concepts/apps)):

     ```
        SPOTIFY_CLIENT_ID= your_client_id
        SPOTIFY_CLIENT_SECRET= your_client_secret
        DISCORD_TOKEN= your_discord_token
    ``` 
    - Save that file.

5. Run executable.
    - In the directory you downloaded the executeable, Run:  
     ```
     ./bot 
     ```    


**Windows OS:**

1. Ensure you have python3 installed on your system. 
    - To check that python is installed properly run this command in your terminal:
        ```
        python --version
        ```
    - If the previous commands does not work try:
        ```
        python3 --version
        ```
    - If the command is successful you will see your current python version installed

2. Open a terminal or command prompt.

3. Use the following command to install the required modules using pip or pip3, the package installer for Python:

        pip install discord requests
    

4. Wait for the installation to complete. Once finished, the required modules will be installed in the Python environment.

5. Download executable from release in Repo **bot.exe**

6. Set up environment variables
    - In the same directory the executable is located, create a .env file in Notepad

    - Set your Client ID and Client Secret in the following format ([How to find Client ID and Client Secret](https://developer.spotify.com/documentation/web-api/concepts/apps)):

     ```
        SPOTIFY_CLIENT_ID= your_client_id
        SPOTIFY_CLIENT_SECRET= your_client_secret
        DISCORD_TOKEN= your_discord_token
    ``` 
    - Save that file.
    - Make sure you save it as type **All Files**

5. Run executable.
    - In the directory you downloaded the executeable, Run:  
     ```
     .\bot.exe 
     ```    
    - Can also run executable by right-clicking bot.exe in File Explorer and then clicking on **Open**

**Docker:**

1. Ensure Docker is installed on your current OS ([Docker Desktop Download](https://www.docker.com/products/docker-desktop/))
2. Once Docker is installed be sure to run the Docker application ensuring that the daemon is running.
3. Open a terminal of your choice and check to see if Docker is installed properly with the following command:
     ```
     docker --version
     ```   
4. Once you have verified Docker is installed and running pull our latest image.
     ```
     docker pull andrewto/discotify:v3.0
     ```
5. Once pulled be sure to setup your environment variables.
    - In the same directory the executable is located, create a .env file in Notepad

    - Set your Client ID and Client Secret in the following format ([How to find Client ID and Client Secret](https://developer.spotify.com/documentation/web-api/concepts/apps)):

     ```
        SPOTIFY_CLIENT_ID= your_client_id
        SPOTIFY_CLIENT_SECRET= your_client_secret
        DISCORD_TOKEN= your_discord_token
    ``` 
    - Save that file.
    - Make sure you save it as type **All Files**
6. Run the image with the following command:
     ```
     docker run --env-file env_file andrewto/discotify:v3.0
     ```
     - env_file will be the path to your .env file that you created in the previous step
    - to run multiple containers you can a command similar to:
     ```
    docker run --env-file env_file_1 -d --name container1 andrewto/discotify:v3.0
    docker run --env-file env_file_2 -d --name container2 andrewto/discotify:v3.0
     ```
     - env_file_1 and env_file_2 are paths to your two .env files while container1 and container2 can be any names you want to want to name your container

# General Commands
1. `!hello` : Greets the user.
2. `!auth` : Initiates authentication with Spotify.
3. `!help` : Displays a list of avaiable commands.

# Spotify Playback Control
1. `!play <query>` : plays a track on Spotify. The `<query>` can be a Spotify link, song name, or song name with the artist.
2. `!pause` : Pauses the current playback on Spotify.
3. `!resume` : Resumes playback on Spotify.
4. `!next` : Skips to the next track on Spotify.
5. `!previous` : Goes to the previous track on Spotify
6. `!devices` : Lists avaiable Spotify devices.

# Spotify User Data
1. `!toptracks` : Shows the user's top 10 tracks on Spotify.
2. `!playlist <name>` : Plays a playlist from the user's library on Spotify by playlist name.

# How to contribute
Follow this project board to know the latest status of the project: [http://...]([http://...])  

### How to build
https://github.com/orgs/cis3296f23/projects/112

- Use this github repository: ... 
- Specify what branch to use for a more stable release or for cutting edge development.  
- Use Visual Studio 
- Specify additional library to download if needed 
- What file and target to compile and run. 
- What is expected to happen when the app start.

# Troubleshooting Problems
Continuously adding new problems that come up through development or building, will post common problems and solutions for current/future developers to refer to.

### Compiling/Building Issues
If `pip install discord jsonlib base64 requests` doesn't work and you are on macOS, try removing the base64 and see if that works.
Make sure you are also using the correct interpreter for your IDE if you using that to run the program.
you can check what interpreter your terminal is using with `which python` or `which python3`.

### INVALID_CLIENT error when authenticating Issues
<img width="881" alt="Pasted Graphic" src="https://github.com/cis3296f23/project-02discotifywalkerbeytoracheawijaya/assets/50151203/73480024-ee16-48cb-a7f7-4e95b2b6b4fd">

If you received this error, make sure to add your Spotify Client ID and Secret to 4 environment variables as if you don't you will receive an `INVALID_CLIENT: Invalid client` error when you click on the authentication link sent by the discord bot.
Make sure you have also added your own Discord Bot token to the environment variable `DISCORD_TOKEN`.

### 403 Error with !previous
If you used !previous and got an error 403, it's most likely because you tried to do the command while not in a playlist. If you did !play and then !previous, you will get the error since you are playing just one single song and there hasn't been any previous history.


