import amino
import time
import credentials

client = amino.Client()
n_acc = len(credentials.USERS)

def claim_lottery():
    for i in range(n_acc):
        try:
            client.login(email=credentials.USERS[i], password=credentials.PASS[i])
            subclient = amino.SubClient(comId=credentials.T_COM_ID, profile=client.profile)
            subclient.lottery()
            print("Lotería lista para usuario {i}".format(i=i))
        except amino.lib.util.exceptions.AlreadyPlayedLottery as err:
            print("Usuario {i} lotería ya hecha.".format(i=i))
        except amino.lib.util.exceptions.VerificationRequired as err:
            print(err)
        except amino.lib.util.exceptions.InvalidAccountOrPassword:
            print("Acc {acc} pass {pwd}".format(pwd=credentials.PASS[i], acc=credentials.USERS[i]))
    return print("Lotería Lista.")

def send_coins():
    for i in range(n_acc):
        client.login(email=credentials.USERS[i], password=credentials.PASS[i])
        subclient = amino.SubClient(comId=credentials.T_COM_ID, profile=client.profile)
        amount = round(subclient.get_wallet_info().totalCoins)
        try:
            subclient.send_coins(coins=amount,blogId=credentials.BLOG_COINS)
            time.sleep(5)
        except amino.lib.util.exceptions.CannotSendCoins as err:
            print(err)
            time.sleep(5)
        except amino.lib.util.exceptions.NotEnoughCoins:
            time.sleep(5)
        except Exception as e:
            print(e)
            time.sleep(5)
    return print("Envío listo.")

if __name__ == '__main__':
    claim_lottery()
    send_coins()
    print("Todo listo.")