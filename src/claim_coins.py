import amino
import time
import os

client = amino.Client()
print(client.login(email=os.getenv('USER'), password=os.getenv('PASS')))
subclient = amino.SubClient(comId=os.getenv('COM_ID'), profile=client.profile)

while True:
    print(subclient.watch_ad())
    time.sleep(1000)