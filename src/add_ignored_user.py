import amino

client = amino.Client()

def add_user_to_ignore(link):
    uid = client.get_from_code(link).objectId
    print(uid)

user = 'LINK TO USER'

if __name__ == '__main__':
    add_user_to_ignore(user)