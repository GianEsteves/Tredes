import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT_TCP = 12345  # Porta do servidor TCP
BUFFER_SIZE = 1024

def server_tcp():
    """
    Inicia um servidor TCP que aceita conexões de clientes e ecoa de volta qualquer dado recebido.

    Cria um socket TCP, liga-o a um endereço IP e porta, e escuta por conexões de entrada. Quando uma conexão é aceita,
    ele entra em um loop para receber dados do cliente e enviar de volta (eco), funcionando como uma simples confirmação (ACK).
    O servidor continua a funcionar até que não haja mais dados para receber.

    Não recebe argumentos e não retorna nenhum valor. Controla a execução do servidor TCP.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((SERVER_IP, SERVER_PORT_TCP))
    sock.listen(1)
    print("TCP server listening on port", SERVER_PORT_TCP)
    conn, addr = sock.accept()
    with conn:
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            conn.sendall(data)  # Simples eco para ACK
    sock.close()

if __name__ == "__main__":
    server_tcp()
