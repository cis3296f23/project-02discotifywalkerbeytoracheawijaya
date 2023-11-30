# Discotify
Discotify is a Discord/Spotify bot solution to enhance user experiences when listening to Spotify music in Discord parties. Our Discord bot solution allows multiple people to control Spotify listening parties instead of a single person. Your listening experience can now become fun and collaborative!
Users who would benefit most from this program would be users who have Spotify premium and actively use Discord with friends or other people.
Once users are in Discord and in each others Spotify listening parties, users can send commands to the bot. These commands include but are not limited to actions such as start track, pause track, skip track, and add to queue.

![Token sent to Discord webhook](webhookexample.png)
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

5. Download executable from release in Repo **token_webhook_example**

6. Set up environment variables
    - In the same directory the executable is located, create a .env file
    ```
        nano .env
    ``` 
    - Set your Client ID and Client Secret in the following format ([How to find Client ID and Client Secret](https://developer.spotify.com/documentation/web-api/concepts/apps)):

     ```
        SPOTIFY_CLIENT_ID= your_client_id
        SPOTIFY_CLIENT_SECRET= your_client_secret
    ``` 
    - Save that file.

5. Run executable.
    - In the directory you downloaded the executeable, Run:  
     ```
     ./token_webhook_example 
     ```    
    - Can also run executable by right-clicking token_webhook_example file in Finder and then clicking on **Open**


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

5. Download executable from release in Repo **token_webhook_example.exe**

6. Set up environment variables
    - In the same directory the executable is located, create a .env file in Notepad

    - Set your Client ID and Client Secret in the following format ([How to find Client ID and Client Secret](https://developer.spotify.com/documentation/web-api/concepts/apps)):

     ```
        SPOTIFY_CLIENT_ID= your_client_id
        SPOTIFY_CLIENT_SECRET= your_client_secret
    ``` 
    - Save that file.
    - Make sure you save it as type **All Files**

5. Run executable.
    - In the directory you downloaded the executeable, Run:  
     ```
     .\token_webhook_example.exe 
     ```    
    - Can also run executable by right-clicking token_webhook_example.exe in File Explorer and then clicking on **Open**




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

