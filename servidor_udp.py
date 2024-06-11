import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT_UDP = 12346  # Porta do servidor UDP
BUFFER_SIZE = 1024

def server_udp():
    """
    Inicia um servidor UDP que ecoa de volta qualquer dado recebido.

    Cria um socket UDP, liga-o a um endereço IP e porta, e escuta por mensagens de entrada. Quando uma mensagem é recebida,
    ela é enviada de volta ao remetente como uma confirmação (ACK).

    Não recebe argumentos e não retorna nenhum valor. Controla a execução do servidor UDP.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((SERVER_IP, SERVER_PORT_UDP))
    print("UDP server listening on port", SERVER_PORT_UDP)
    while True:
        data, addr = sock.recvfrom(BUFFER_SIZE)
        sock.sendto(data, addr)  # Simples eco para ACK
    sock.close()

if __name__ == "__main__":
    server_udp()

