import os
import random
import google_auth_oauthlib.flow
import googleapiclient.discovery

from playlist_id import SOURCE_PLAYLIST_ID

# Permissions needed to read and modify playlists
scopes = ["https://www.googleapis.com/auth/youtube"]

def get_authenticated_service():
    '''
    Open Browser and ask for log in
    '''
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        "client.json", scopes)
    credentials = flow.run_local_server(port=0)
    
    return googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

def get_playlist_videos(youtube, playlist_id):
    videos = []
    request = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=50
    )
    
    print("Saving videos from the original playlist...")
    while request is not None:
        response = request.execute()
        for item in response["items"]:
            videos.append(item["snippet"]["resourceId"]["videoId"])
        request = youtube.playlistItems().list_next(request, response)
        
    return videos

def create_new_playlist(youtube, title):
    print(f"Creating the playlist '{title}'...")
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
          "snippet": {
            "title": title,
            "description": "An automatically shuffled playlist with Python!",
          },
          "status": {
            "privacyStatus": "private" # You can change this to 'public' or 'unlisted'
          }
        }
    )
    response = request.execute()
    return response["id"]

def add_videos_to_playlist(youtube, playlist_id, video_ids):
    print(f"Adding {len(video_ids)} videos to the new playlist...")
    for index, video_id in enumerate(video_ids):
        try:
            request = youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": playlist_id,
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": video_id
                        }
                    }
                }
            )
            request.execute()
            print(f"Added {index + 1}/{len(video_ids)}: {video_id}")
        except Exception as e:
            print(f"Error with video {video_id} (possibly deleted/private): {e}")

def main():
    new_name = "Playlist Shuffled (Fresh)"

    youtube = get_authenticated_service()

    videos = get_playlist_videos(youtube, SOURCE_PLAYLIST_ID)
    
    random.shuffle(videos)
    
    new_playlist_id = create_new_playlist(youtube, new_name)
    
    add_videos_to_playlist(youtube, new_playlist_id, videos)
    
    print("\nDone! The playlist has been created successfully on your account!")

if __name__ == "__main__":
    main()