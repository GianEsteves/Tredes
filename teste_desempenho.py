import socket
import time

SERVER_IP = '127.0.0.1'
SERVER_PORT_TCP = 12345
SERVER_PORT_UDP = 12346
SERVER_PORT_UDP_MOD = 12347
BUFFER_SIZE = 1024

messages = [f"Message {i}" for i in range(1000)]

def send_tcp():
    """
    Envia uma série de mensagens usando TCP e mede o tempo total gasto.

    Conecta-se a um servidor TCP, envia uma lista de mensagens, recebe ACKs para cada mensagem enviada e mede o tempo total de transmissão.

    Retorna:
        float: O tempo total gasto para enviar todas as mensagens e receber os ACKs.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_IP, SERVER_PORT_TCP))
    start_time = time.time()
    for msg in messages:
        sock.sendall(msg.encode())
        sock.recv(BUFFER_SIZE)
    end_time = time.time()
    sock.close()
    return end_time - start_time

def send_udp():
    """
    Envia uma série de mensagens usando UDP e mede o tempo total gasto.

    Envia uma lista de mensagens para um servidor UDP e mede o tempo total de transmissão.

    Retorna:
        float: O tempo total gasto para enviar todas as mensagens.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    start_time = time.time()
    for msg in messages:
        sock.sendto(msg.encode(), (SERVER_IP, SERVER_PORT_UDP))
    end_time = time.time()
    sock.close()
    return end_time - start_time

def send_udp_mod():
    """
    Envia uma série de mensagens usando uma versão modificada do UDP e mede o tempo total gasto.

    Envia uma lista de mensagens para um servidor UDP modificado e mede o tempo total de transmissão.

    Retorna:
        float: O tempo total gasto para enviar todas as mensagens.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    start_time = time.time()
    for msg in messages:
        sock.sendto(msg.encode(), (SERVER_IP, SERVER_PORT_UDP_MOD))
    end_time = time.time()
    sock.close()
    return end_time - start_time

if __name__ == "__main__":
    tcp_time = send_tcp()
    udp_time = send_udp()
    udp_mod_time = send_udp_mod()
    print(f"TCP Time: {tcp_time:.2f} seconds")
    print(f"UDP Time: {udp_time:.2f} seconds")
    print(f"Modified UDP Time: {udp_mod_time:.2f} seconds")
