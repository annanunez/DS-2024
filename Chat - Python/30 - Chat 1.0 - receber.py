from click import clear
import time

while True:
    clear()
    with open("Chat_1.txt", "r") as arquivo:
        mensagens = arquivo.readlines()

    for mensagem in reversed(mensagens):
        print(mensagem)
    time.sleep(3)