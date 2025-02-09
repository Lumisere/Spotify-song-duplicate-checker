# Spotify Playlist Duplicate Remover

This Python script helps you find and remove duplicate tracks from your Spotify playlists. It uses the Spotify Web API to interact with your account and manage your playlists.

## Prerequisites

Before you start, make sure you have the following:

1. **Spotify Developer Account**: You need to create a Spotify Developer account and set up an application to get your `Client ID` and `Client Secret`.
2. **Python 3.x**: The script is written in Python, so you'll need Python installed on your machine.
3. **Spotipy Library**: This script uses the `spotipy` library to interact with the Spotify API.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Lumisere/Spotify-song-duplicate-checker.git
   cd Spotify-song-duplicate-checker
   ```

2. **Install the required Python packages**:
   ```bash
   pip install spotipy
   ```

3. **Set up your Spotify Developer Application**:
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
   - Create a new application.
   - Note down the `Client ID` and `Client Secret`.
   - Set the `Redirect URI` to `http://localhost:8888/callback`.
   - **Add Your Account as a Verified User**:
     - In the Spotify Developer Dashboard, go to your app's settings.
     - Navigate to the **User Management** section.
     - Add your Spotify account email as a verified user. This step is required to authorize your account to use the app.

4. **Update the script with your credentials**:
   - Open the script in your favorite text editor.
   - Replace `'ENTER CLIENTID'` and `'ENTER SECRET'` with your actual `Client ID` and `Client Secret`.

## How to Use

1. **Run the script**:
   ```bash
   python main.py
   ```

2. **Authenticate**:
   - The script will open a browser window asking you to log in to your Spotify account and authorize the application.
   - After authorization, you will be redirected to `http://localhost:8888/callback`.

3. **Select a Playlist**:
   - The script will list all your playlists.
   - Enter the number corresponding to the playlist you want to check for duplicates.

4. **Find and Remove Duplicates**:
   - The script will scan the selected playlist for duplicate tracks.
   - If duplicates are found, you will be prompted to delete them.

## Important Notes

- **Rate Limits**: Be aware of Spotify's API rate limits. If you have a large number of playlists or tracks, the script may take some time to process everything.
- **Verified User**: Ensure your Spotify account is added as a verified user in the Spotify Developer Dashboard. Without this, the authentication will fail.

## Contributing

Feel free to fork this repository and submit pull requests. If you find any issues or have suggestions for improvements, please open an issue.

