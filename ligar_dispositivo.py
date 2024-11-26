import socket
import time

# Configurações de rede e IRC
SERVER = '192.168.1.101'  # IP do relé
PORT = 6668  # Porta de comunicação do relé
CHANNELS = ['#Luz_de_fora', '#luz_externa', '#luz_fora']  # Canais para controle

# Defina seu Nickname e Usuário
NICKNAME = 'rele_bot'
USER = 'nome_do_usuario'

def irc_send(socket, message):
    """Envia uma mensagem para o servidor IRC"""
    socket.send(f"{message}\r\n".encode('utf-8'))

def irc_connect():
    """Conecta-se ao servidor IRC e entra no canal"""
    irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc_socket.connect((SERVER, PORT))
    
    # Envia as informações de identificação
    irc_send(irc_socket, f'NICK {NICKNAME}')
    irc_send(irc_socket, f'USER {USER} 0 * :Controle')
    
    # Aguarda um pouco para garantir que a conexão seja estabelecida
    time.sleep(2)
    
    # Entra nos canais
    for channel in CHANNELS:
        irc_send(irc_socket, f'JOIN {channel}')
        print(f"Entrando no canal {channel}")
        time.sleep(1)
    
    return irc_socket

def send_command(irc_socket, channel, command):
    """Envia o comando 'on' ou 'off' para o canal"""
    irc_send(irc_socket, f'PRIVMSG {channel} :{command}')

def manual_command(irc_socket):
    """Permite que o usuário envie comandos manualmente"""
    while True:
        command = input("Digite o comando (on, off ou 'sair' para sair): ").strip().lower()
        
        if command == 'on':
            print("Enviando comando para ligar a lâmpada...")
            for channel in CHANNELS:
                send_command(irc_socket, channel, 'on')
        elif command == 'off':
            print("Enviando comando para desligar a lâmpada...")
            for channel in CHANNELS:
                send_command(irc_socket, channel, 'off')
        elif command == 'sair':
            print("Saindo do programa.")
            break
        else:
            print("Comando inválido! Use 'on', 'off' ou 'sair'.")

def main():
    # Conecta ao servidor IRC
    irc_socket = irc_connect()
    
    # Aguarda alguns segundos para garantir que a conexão esteja estável
    time.sleep(5)
    
    # Permite que o usuário envie comandos manualmente
    manual_command(irc_socket)
    
    # Fecha a conexão
    irc_socket.close()

if __name__ == "__main__":
    main()
