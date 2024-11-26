import socket
import time

# Configurações do servidor IRC
HOST = "192.168.1.101"  # IP do servidor IRC
PORT = 6668  # Porta do servidor IRC
CHANNEL = "#sala"  # Canal IRC onde o relé responde

# Função para enviar mensagem IRC
def send_message(sock, message):
    sock.send(f"PRIVMSG {CHANNEL} :{message}\r\n".encode('utf-8'))

# Conectar ao servidor IRC
def connect_irc():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    
    # Enviar o comando de identificação
    sock.send(f"NICK relé_bot\r\n".encode('utf-8'))
    sock.send(f"USER relé_bot 0 * :rele_bot\r\n".encode('utf-8'))
    
    return sock

# Função para ligar o relé
def ligar(sock):
    send_message(sock, "ligar")  # Enviar comando para ligar a lâmpada
    print("Comando: Ligar")

# Função para desligar o relé
def desligar(sock):
    send_message(sock, "desligar")  # Enviar comando para desligar a lâmpada
    print("Comando: Desligar")

# Função para ligar usando 'on'
def ligar_on(sock):
    send_message(sock, "on")  # Enviar comando 'on' para ligar a lâmpada
    print("Comando: On")

# Função para desligar usando 'off'
def desligar_off(sock):
    send_message(sock, "off")  # Enviar comando 'off' para desligar a lâmpada
    print("Comando: Off")

# Testar os comandos
def test_commands():
    sock = connect_irc()

    # Esperar a conexão ser estabelecida
    time.sleep(5)

    # Testar os comandos
    ligar(sock)  # Testar comando 'ligar'
    time.sleep(2)
    desligar(sock)  # Testar comando 'desligar'
    time.sleep(2)
    ligar_on(sock)  # Testar comando 'on'
    time.sleep(2)
    desligar_off(sock)  # Testar comando 'off'

    # Fechar a conexão
    sock.close()

if __name__ == "__main__":
    test_commands()
