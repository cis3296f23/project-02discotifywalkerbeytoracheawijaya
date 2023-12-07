bot
====================

hello
-----

.. function:: hello(ctx)

   This asynchronous function sends a greeting to the user who invoked the command.

   :param ctx: The context in which the command was called. Contains information like the channel and guild where the command was invoked.

   **Usage:**

   .. code-block:: none

      !hello

   Upon invocation, this command will send a message in the form of "Hello, @User!" mentioning the user who called the command.

authenticate
------------

.. function:: authenticate(ctx)

   This command starts the Spotify authentication process for the user. It sends a message with a button that the user can click to authenticate via Spotify.

   :param ctx: The context in which the command was called. Contains information like the channel and guild where the command was invoked.

   **Usage:**

   .. code-block:: none

      !auth

   When the user clicks the authentication button, they will be redirected to Spotify's login page to complete the authentication process.

spotify_callback
----------------

.. function:: spotify_callback()

   This function handles the Spotify callback after user authentication. It retrieves the authorization code from Spotify and exchanges it for access tokens.

   The function checks if the state matches and then requests access and refresh tokens from Spotify. If the state does not match, it returns an error.

   **Endpoint:** ``/callback``

   **Method:** GET

   **Returns:**
      A message indicating successful authentication or an error message in case of state mismatch.

run_flask_app
-------------

.. function:: run_flask_app()

   This function runs the Flask application in a separate thread. It's used to handle the Spotify authentication callback.

   **Usage:**

   The function is used internally and is not directly callable via Discord.

on_ready
--------

.. function:: on_ready()

   This event handler function is triggered when the bot is ready. It prints a message to the console indicating that the bot has successfully logged in.

   **Usage:**

   Automatically triggered by the Discord API when the bot starts and is ready to receive commands.

play
----

.. function:: play(ctx, *, query: str)

   Plays a track on Spotify based on the given query. The query can be a Spotify URL, track name, or track name with artist.

   :param ctx: The context in which the command was called.
   :param query: The search query or Spotify URL for the track.

   **Usage:**

   .. code-block:: none

      !play <Spotify URL or track name>

pause
-----

.. function:: pause(ctx)

   Pauses the current Spotify playback.

   :param ctx: The context in which the command was called.

   **Usage:**

   .. code-block:: none

      !pause

start
-----

.. function:: start(ctx)

   Resumes Spotify playback.

   :param ctx: The context in which the command was called.

   **Usage:**

   .. code-block:: none

      !start

next_track
----------

.. function:: next_track(ctx)

   Skips to the next track in the Spotify queue.

   :param ctx: The context in which the command was called.

   **Usage:**

   .. code-block:: none

      !next

previous_track
--------------

.. function:: previous_track(ctx)

   Goes back to the previous track in the Spotify queue.

   :param ctx: The context in which the command was called.

   **Usage:**

   .. code-block:: none

      !previous

devices
-------

.. function:: devices(ctx)

   Lists all available Spotify devices.

   :param ctx: The context in which the command was called.

   **Usage:**

   .. code-block:: none

      !devices

show_help
---------

.. function:: show_help(ctx)

   Lists all available commands in the bot.

   :param ctx: The context in which the command was called.

   **Usage:**

   .. code-block:: none

      !help

top_tracks
----------

.. function:: top_tracks(ctx)

   Shows the user's top 10 tracks on Spotify.

   :param ctx: The context in which the command was called.

   **Usage:**

   .. code-block:: none

      !toptracks

playlist
--------

.. function:: playlist(ctx, *, query: str)

   Plays a playlist from the user's Spotify library based on the given name.

   :param ctx: The context in which the command was called.
   :param query: The name of the playlist to play.

   **Usage:**

   .. code-block:: none

      !playlist <playlist name>

spotify_profile
---------------

.. function:: spotify_profile(ctx)

   Displays the user's Spotify profile details
