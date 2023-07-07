import socket

# configuração do servidor
host = ''  # endereço de IP do servidor
port = 12345         # número de porta do servidor

# cria um socket udp
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Essas são as regras do jogo: ")
print("Tesoura corta papel")
print("Papel cobre pedra")
print("Pedra esmaga lagarto")
print("Lagarto envenena Spock")
print("Spock esmaga (ou derrete) tesoura")
print("Tesoura decapita lagarto")
print("Lagarto come papel")
print("Papel refuta Spock")
print("Spock vaporiza pedra")
print("Pedra amassa tesoura")

while True:
    user_choice = input("\nEscolha R(Pedra)/T(Tesoura)/P(Papel)/L(Lagarto)/S(Spock) ou Q para sair: ").lower()

    # mandaa escolha do cliente (user) para o servidor
    sock.sendto(user_choice.encode(), (host, port))

    if user_choice == 'q':
        break

    # recebe o resultado (result) do servidor
    data, addr = sock.recvfrom(1024)
    result = data.decode()

    print(result)

# fecha o socket
sock.close()
