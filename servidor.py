import random
import socket

# configuração do servidor
host = ''  # endereço de IP do servidor
port = 12345         # número de porta do servidor

# lógica do jogo
user_points = 0
computer_points = 0

options = ["r", "t", "p", "l", "s"]

# cria um socket udp
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# liga o socket ao endereço do servidor
sock.bind((host, port))

print("Servidor iniciado. Esperando por conexão...")

while True:
    # recebe dado do cliente
    data, addr = sock.recvfrom(1024)
    user_choice = data.decode().lower()

    if user_choice == 'q':
        break

    if user_choice not in options:
        print("\nLetra inválida. Digite uma letra de acordo com as opções.")
        continue

    computer_choice = random.randint(0, 4)
    computer_option = options[computer_choice]

    print("Escolha do cliente: " + user_choice)
    print("Escolha do servidor: " + computer_option)

    if user_choice == computer_option:
        result = "Empate!"
    elif user_choice == "r":
        if computer_option == "t" or computer_option == "l":
            result = "Você ganhou!"
            user_points += 1
        else:
            result = "Você perdeu!"
            computer_points += 1
    elif user_choice == "p":
        if computer_option == "r" or computer_option == "s":
            result = "Você ganhou!"
            user_points += 1
        else:
            result = "Você perdeu!"
            computer_points += 1
    elif user_choice == "t":
        if computer_option == "p" or computer_option == "l":
            result = "Você ganhou!"
            user_points += 1
        else:
            result = "Você perdeu!"
            computer_points += 1
    elif user_choice == "l":
        if computer_option == "p" or computer_option == "s":
            result = "Você ganhou!"
            user_points += 1
        else:
            result = "Você perdeu!"
            computer_points += 1
    elif computer_option == "r" or computer_option == "t":
        result = "Você ganhou!"
        user_points += 1
    else:
        result = "Você perdeu!"
        computer_points += 1

    # envia o resultado(result) de volta pro cliente
    sock.sendto(result.encode(), addr)

# fecha o socket
sock.close()

print("\nSua pontuação: " + str(user_points))
print("Pontuação do Computador: " + str(computer_points))

if computer_points > user_points:
    print("\nDerrota!")
elif computer_points == user_points:
    print("\nEmpate")
else:
    print("\nVitória!!")
