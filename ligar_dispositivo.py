import socket
import time

# Configurações do servidor IRC
HOST = "192.168.1.101"  # IP do servidor IRC
PORT = 6668  # Porta do servidor IRC
CHANNELS = ["#luz_sala", "#sala", "#luz_da_sala"]  # Canais personalizados

# Função para enviar mensagem IRC para múltiplos canais
def send_message(sock, channel, message):
    sock.send(f"PRIVMSG {channel} :{message}\r\n".encode('utf-8'))

# Conectar ao servidor IRC
def connect_irc():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    
    # Enviar o comando de identificação
    sock.send(f"NICK relé_bot\r\n".encode('utf-8'))
    sock.send(f"USER relé_bot 0 * :rele_bot\r\n".encode('utf-8'))
    
    return sock

# Função para ligar o relé em múltiplos canais
def ligar(sock):
    for channel in CHANNELS[:3]:  # Limitar para no máximo 3 canais
        send_message(sock, channel, "ligar")  # Enviar comando para ligar a lâmpada
        print(f"Comando: Ligar no canal {channel}")

# Função para desligar o relé em múltiplos canais
def desligar(sock):
    for channel in CHANNELS[:3]:  # Limitar para no máximo 3 canais
        send_message(sock, channel, "desligar")  # Enviar comando para desligar a lâmpada
        print(f"Comando: Desligar no canal {channel}")

# Função para ligar usando 'on' em múltiplos canais
def ligar_on(sock):
    for channel in CHANNELS[:3]:  # Limitar para no máximo 3 canais
        send_message(sock, channel, "on")  # Enviar comando 'on' para ligar a lâmpada
        print(f"Comando: On no canal {channel}")

# Função para desligar usando 'off' em múltiplos canais
def desligar_off(sock):
    for channel in CHANNELS[:3]:  # Limitar para no máximo 3 canais
        send_message(sock, channel, "off")  # Enviar comando 'off' para desligar a lâmpada
        print(f"Comando: Off no canal {channel}")

# Testar os comandos em múltiplos canais
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
