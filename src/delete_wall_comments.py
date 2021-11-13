import amino
import credentials

client = amino.Client()
print(client.login(email=credentials.EMAIL, password=credentials.PWD))
subclient = amino.SubClient(comId=credentials.COM_ID, profile=client.profile)

ids_commentaries = subclient.get_wall_comments(userId=credentials.MY_ID, sorting='oldest').commentId

for id_com in ids_commentaries:
    subclient.delete_comment(commentId=id_com, userId=credentials.MY_ID)