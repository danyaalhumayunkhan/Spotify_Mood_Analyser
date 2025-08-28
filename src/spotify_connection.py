import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up Spotify API connection
client_credentials_manager = SpotifyClientCredentials(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Create function to get tracks from a Spotify playlist URL
def get_playlist_tracks(playlist_url: str):
    #Extract playlist ID from URL
    playlist_id = playlist_url.split("/")[-1].split("?")[0]

    try:
        #Try to fetch tracks
        results = sp.playlist_tracks(playlist_id)
    except spotipy.exceptions.SpotifyException as e:
        #Inspect the error to decide what to do
        if getattr(e, 'http_status', None) == 404:
            raise ValueError(
                "Playlist not found or is owned by Spotify - it cannot be analysed"
                ) from None
        #If it is not a 404 error, re-raise the exception
        raise


    #Get tracks from playlist
    #results = sp.playlist_tracks(playlist_id)
    tracks = results['items']

    #Handling pagination
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    return tracks

if __name__ == "__main__":
    #Example playlist
    test_url = "https://open.spotify.com/playlist/3ilMGO4S6owQivbsylJoCt?si=b808dc2015b14308"
    tracks = get_playlist_tracks(test_url)

    print(f"Total tracks in playlist: {len(tracks)}")
    #print first 5 tracks 
    for i, item in enumerate(tracks[:5], start=1):
        track = item['track']
        print(f"{i}. {track["name"]} - {track["artists"][0]["name"]}")
