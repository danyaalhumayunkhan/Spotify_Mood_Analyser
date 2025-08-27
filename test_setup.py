import spotipy
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

#Load API keys
load_dotenv()

print("All libraries imported successfully.")
print(f"Client ID loaded: {os.getenv('SPOTIFY_CLIENT_ID')[:10]}...")

#Test Spotify connection
try:
    from spotipy.oauth2 import SpotifyClientCredentials

    client_credentials_manager = SpotifyClientCredentials(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    #Try to get a playlist
    results = sp.playlist('2F9EwHY9pqMVoAzfGu5vOp')
    print(f"Spotify API connected! Found playlist: {results['name']}")

except Exception as e:
    print(f"Error connecting to Spotify API: {e}")
