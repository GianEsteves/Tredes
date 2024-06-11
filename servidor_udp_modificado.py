import socket
import threading
import random
import time

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12346 
BUFFER_SIZE = 1024

# Simulação de Congestionamento
MAX_QUEUE_SIZE = 50  # Tamanho máximo da fila de pacotes
message_queue = []
expected_seq_num = 0

def simulate_delay():
    """
    Simula um atraso de pacotes.

    Retorna:
        float: Um valor de atraso aleatório entre 50ms e 100ms.
    """
    return random.uniform(0.05, 0.1)  # Atraso entre 50ms e 100ms

def process_queue(sock, client_addr):
    """
    Processa a fila de mensagens, enviando um ACK para cada mensagem recebida na ordem correta.

    Args:
        sock (socket.socket): O socket usado para enviar os ACKs.
        client_addr (tuple): O endereço do cliente que enviou a mensagem.

    Não retorna nenhum valor. Envia ACKs para o cliente.
    """
    global expected_seq_num
    while True:
        if message_queue and message_queue[0][0] == expected_seq_num:
            seq_num, msg = message_queue.pop(0)
            print(f"Received: {msg} with sequence number: {seq_num}")
            sock.sendto(str(seq_num).encode(), client_addr)
            expected_seq_num += 1
        time.sleep(0.01)

def server():
    """
    Inicia um servidor UDP que recebe mensagens de clientes, simula atraso e congestionamento, e envia ACKs.

    Cria um socket UDP, liga-o a um endereço IP e porta, e escuta por mensagens de clientes. As mensagens recebidas são
    processadas e ordenadas antes de serem enviadas de volta como ACKs.

    Não recebe argumentos e não retorna nenhum valor. Controla a execução do servidor UDP.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((SERVER_IP, SERVER_PORT))
    client_addr = None
    threading.Thread(target=process_queue, args=(sock, client_addr)).start()
    while True:
        data, addr = sock.recvfrom(BUFFER_SIZE)
        seq_num, msg = data.decode().split(':', 1)
        seq_num = int(seq_num)
        if len(message_queue) < MAX_QUEUE_SIZE:
            message_queue.append((seq_num, msg))
            message_queue.sort()  # Ordenar pacotes na fila
            client_addr = addr
        time.sleep(simulate_delay())

if __name__ == "__main__":
    server()

