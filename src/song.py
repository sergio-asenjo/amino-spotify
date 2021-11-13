import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
from credentials import SCOPE
from datetime import timedelta

BAR1 =  '○━━━━━━━━━━━━━━━━━━━'
BAR2 =  '━━○━━━━━━━━━━━━━━━━━'
BAR3 =  '━━━━○━━━━━━━━━━━━━━━'
BAR4 =  '━━━━━━○━━━━━━━━━━━━━'
BAR5 =  '━━━━━━━━○━━━━━━━━━━━'
BAR6 =  '━━━━━━━━━━○━━━━━━━━━'
BAR7 =  '━━━━━━━━━━━━○━━━━━━━'
BAR8 =  '━━━━━━━━━━━━━━○━━━━━'
BAR9 =  '━━━━━━━━━━━━━━━━○━━━'
BAR10 = '━━━━━━━━━━━━━━━━━━○━'
BAR11 = '━━━━━━━━━━━━━━━━━━━○'

sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=SCOPE))

def get_image_url(sp):
    track_info = sp.current_user_playing_track()
    cd_url = track_info['item']['album']['images'][1]['url']
    return cd_url
    

def get_track_data(sp):
    track_info = sp.current_user_playing_track()

    track_name = track_info['item']['name']
    all_artists = [artist for artist in track_info['item']['artists']]
    artists_names = ', '.join([artist['name'] for artist in all_artists])
    track_progress = track_info['progress_ms']
    track_duration = track_info['item']['duration_ms']
    link = track_info['item']['external_urls']['spotify']

    current_track_info = {
        "track_name": track_name,
        "artists": artists_names,
        "progress": track_progress,
        "duration": track_duration,
        "link": link
    }
    return current_track_info

def calculate_percentage(current, total):
    perc = round((current*100)/total)
    bar = BAR1
    if perc >= 0 and perc <= 10:
        bar = BAR1
    elif perc > 10 and perc <= 20:
        bar = BAR2
    elif perc > 20 and perc <= 30:
        bar = BAR3
    elif perc > 30 and perc <= 40:
        bar = BAR4
    elif perc > 40 and perc <= 50:
        bar = BAR5
    elif perc > 50 and perc <= 60:
        bar = BAR6
    elif perc > 60 and perc <= 70:
        bar = BAR7
    elif perc > 70 and perc <= 80:
        bar = BAR8
    elif perc > 80 and perc <= 90:
        bar = BAR9
    elif perc > 90 and perc <= 95:
        bar = BAR10
    elif perc > 95 and perc <= 100:
        bar = BAR11
    return bar

def calculate_seconds(ms_time):
    c_time = str(timedelta(milliseconds=ms_time)).split('.')[0].split(':',maxsplit=1)
    return c_time[1]

if __name__ == '__main__':

    while True:
        print(get_track_data(sp))
        time.sleep(10)
