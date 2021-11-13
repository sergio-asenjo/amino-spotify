import credentials
import requests
import spotipy
import song
import amino
import time
from spotipy.oauth2 import SpotifyOAuth
from credentials import SCOPE
from PIL import Image

client = amino.Client()
print(client.login(email=credentials.EMAIL, password=credentials.PWD))
subclient = amino.SubClient(comId=credentials.COM_ID, profile=client.profile)

def create_image(url_i):
    img_data = requests.get(url_i).content
    with open('img/cd.jpg', 'wb') as handler:
        handler.write(img_data)
    img1 = Image.open('img/black.png')
    img2 = Image.open('img/cd.jpg')
    back_im = img1.copy()
    back_im.paste(img2, (390, 771))
    back_im.save('img/combined.png', quality=95)
    return True

if __name__ == '__main__':

    sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=SCOPE))
    
    while True:
        try:
            img_url = song.get_image_url(sp)
            create_image(img_url)
            amino_link = client.upload_media(open("img/combined.png", "rb"), "image")
            subclient.edit_profile(backgroundImage=amino_link)
            time.sleep(10)
        except Exception as e:
            sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=SCOPE))
            time.sleep(20)
            print(e)
