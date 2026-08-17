# YouTube Playlist Shuffler

A simple Python script that takes any public YouTube playlist, shuffles its videos, and creates a brand-new private playlist on your own YouTube account using the official YouTube Data API v3.

## Google Cloud Console

### Create the project & Get credentials
1. Go to [Google Cloud Console](https://console.cloud.google.com/) and create a new project.
2. Navigate to **APIs & Services > Library**, search for **YouTube Data API v3**, and click **Enable**.
3. Go to the **Google Auth Platform** (or OAuth consent screen). Click **Get started**, choose **External**, and make sure to add your email address under **Test users**.
4. Go to the **Clients** (or Credentials) tab, click **Create Client**, and select **Desktop app** as the application type.
5. Download the generated credentials file and rename it to `client.json`.

## Prerequisites
* Python 3.x installed on your computer.
* Install required libraries by opening your terminal or command prompt and running:
    ```bash
    pip install -r requirements.txt
    ```
* The `.json` file with your secret from the step above, renamed to `client.json` and placed in the same folder.
* A `playlist_id.py` file containing the target playlist ID:
    ```python
    SOURCE_PLAYLIST_ID = "YOUR_PLAYLIST_ID_HERE" 
    ```
    *(You can find the ID in the URL: `www.youtube.com/playlist?list=PLAYLIST_ID`)*

## Usage
1. Make sure all files (`script.py`, `client.json`, `playlist_id.py`, `requirements.txt`) are in the same folder.
2. Run the script in your terminal:
    ```bash
    python script.py
    ```
3. A browser window will open. Log in with your Google account to grant permission to create the new playlist. Done!

## Delete the project from GC [Optional]
If you want to clean up and remove the API access:
1. Go to Google Cloud Console.
2. Navigate to **IAM & Admin > Settings**.
3. Click **SHUT DOWN** (or Delete) at the top of the page.
4. Type your Project ID to confirm and delete. You can now delete the local files as well.