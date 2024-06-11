import socket
import threading
import time
import random

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12346  # Altere para a mesma porta usada pelo servidor
BUFFER_SIZE = 1024

# Configurações de Controle
WINDOW_SIZE = 5  # Controle de Fluxo
RETRANSMISSION_TIMEOUT = 2  # Tempo para retransmissão

# Mensagens para enviar
messages = [f"Message {i}" for i in range(1000)]
acknowledged = [False] * len(messages)
window_base = 0

def simulate_packet_loss():
    """
    Simula a perda de pacotes com uma probabilidade de 10%.

    Retorna:
        bool: True se o pacote for considerado perdido (simulação de falha), False caso contrário.
    """
    return random.random() < 0.1  # 10% de perda

def send_message(sock, msg, seq_num):
    """
    Envia uma mensagem para o servidor, a menos que a simulação de perda de pacotes indique o contrário.

    Args:
        sock (socket.socket): O socket usado para enviar a mensagem.
        msg (str): A mensagem a ser enviada.
        seq_num (int): O número de sequência da mensagem, usado para identificação.

    Não retorna nenhum valor.
    """
    if not simulate_packet_loss():
        print(f"Sending message {seq_num}: {msg}")
        sock.sendto(f"{seq_num}:{msg}".encode(), (SERVER_IP, SERVER_PORT))

def receive_acks(sock):
    """
    Recebe ACKs do servidor e atualiza a base da janela deslizante conforme os ACKs são recebidos.

    Args:
        sock (socket.socket): O socket usado para receber os ACKs.

    Não retorna nenhum valor. Atualiza a variável global 'window_base' e a lista 'acknowledged'.
    """
    global window_base
    while window_base < len(messages):
        data, _ = sock.recvfrom(BUFFER_SIZE)
        ack_num = int(data.decode())
        print(f"Received ACK for message {ack_num}")
        acknowledged[ack_num] = True
        while window_base < len(messages) and acknowledged[window_base]:
            window_base += 1

def client():
    """
    Função principal que inicia a comunicação do cliente, envia mensagens e gerencia a retransmissão de mensagens não reconhecidas.

    Cria um socket UDP, inicia um thread para receber ACKs e gerencia o envio e retransmissão de mensagens até que todas sejam reconhecidas.

    Não recebe argumentos e não retorna nenhum valor. Controla a execução geral do cliente.
    """
    global window_base
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    threading.Thread(target=receive_acks, args=(sock,)).start()
    while window_base < len(messages):
        for i in range(window_base, min(window_base + WINDOW_SIZE, len(messages))):
            if not acknowledged[i]:
                send_message(sock, messages[i], i)
        time.sleep(RETRANSMISSION_TIMEOUT)
    print("All messages sent and acknowledged")

if __name__ == "__main__":
    client()

