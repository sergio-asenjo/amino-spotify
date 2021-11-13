import os
import time
import amino
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from credentials import SCOPE
import song

client = amino.Client()
print(client.login(email=os.getenv('USER'), password=os.getenv('PASS')))
subclient = amino.SubClient(comId=os.getenv('COM_ID'), profile=client.profile)

if __name__ == '__main__':

    sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=SCOPE))

    while True:
        try:
            song_info = song.get_track_data(sp)
            c_duration = song.calculate_seconds(song_info['duration'])
            c_progress = song.calculate_seconds(song_info['progress'])
            c_bar = song.calculate_percentage(song_info['progress'], song_info['duration'])
            with open("profile_info.txt", "r", encoding="utf8") as p_text:
                subclient.edit_profile(content=p_text.read().format(song_title=song_info['track_name'],
                                                             artists=song_info['artists'],
                                                             current_ms=c_progress,
                                                             bar=c_bar,
                                                             total_duration=c_duration,
                                                             link=song_info['link']))
            p_text.close()
            time.sleep(5)
        except:
            sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=SCOPE))
            p_text.close()
            time.sleep(10)
            print("Token error.")