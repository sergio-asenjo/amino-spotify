import amino
import credentials
import time

client = amino.Client()
print(client.login(email=credentials.EMAIL, password=credentials.PWD))
subclient = amino.SubClient(comId=credentials.COM_ID, profile=client.profile)

user_ids = subclient.get_online_users().profile.userId
numero = 0

while True:
    for user_id in user_ids:
        if user_id not in credentials.IGNORED_USERS:
            wikis = subclient.get_user_wikis(userId=user_id).wikiId
            if len(wikis) > 0:
                for wiki in wikis:
                    subclient.like_blog(wikiId=wiki)
            print(f'Terminado user {numero}.'.format(numero=numero))
            numero = numero + 1
        else:
            userIg = subclient.get_user_info(userId=user_id).nickname
            print("User {name} ignorado.".format(name=userIg))
    print("Terminado listado actual.")
    time.sleep(10)
    ids = subclient.get_online_users().profile.userId