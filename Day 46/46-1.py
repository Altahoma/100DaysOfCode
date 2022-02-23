import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup


SPOTIFY_ID = 'example'
SPOTIFY_SECRET = 'example'
URL = 'https://www.billboard.com/charts/hot-100/'


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

date = input('Which year do you want to travel? Type the date in this format YYYY-MM-DD: ')
response = requests.get(URL + date)
soup = BeautifulSoup(response.content, 'html.parser')
all_songs_data = soup.find_all(name='div', class_='o-chart-results-list-row-container')

song_titles = []
for song in all_songs_data:
    song_title = song.find('h3').text.strip()
    song_titles.append(song_title)

song_uris = []
for song in song_titles:
    result = sp.search(q=song)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
