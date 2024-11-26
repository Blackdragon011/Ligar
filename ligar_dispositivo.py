import socket
import time

# Configuração do servidor IRC
server_ip = '192.168.1.101'
port = 6668

# Nomes de canal
channels = ['#Luz_de_fora', '#luz_externa', '#luz_fora']

# Configuração do nick
nickname = 'rele_bot'

# Função para se conectar e enviar comandos
def connect_to_irc():
    try:
        # Cria o socket
        irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Conecta ao servidor IRC
        irc.connect((server_ip, port))
        print(f"Conectado ao servidor {server_ip} na porta {port}")

        # Envia o comando NICK (nome do usuário)
        irc.send(f'NICK {nickname}\r\n'.encode())
        time.sleep(2)  # Atraso para garantir que o NICK seja aceito
        
        # Envia o comando USER (informações do usuário)
        irc.send(f'USER {nickname} 0 * :Controle\r\n'.encode())
        time.sleep(2)  # Atraso para garantir que o USER seja aceito
        
        # Entra nos canais
        for channel in channels:
            irc.send(f'JOIN {channel}\r\n'.encode())
            print(f"Entrando no canal {channel}")
            time.sleep(2)  # Atraso entre as tentativas de entrada

        # Aguardar comandos ou saída
        while True:
            response = irc.recv(2048).decode()
            print(response)  # Exibe a resposta do servidor IRC
            
            if "PING" in response:
                irc.send("PONG :Pong\r\n".encode())  # Responde ao PING para manter a conexão ativa
            
            # Comandos para ligar/desligar a luz
            if "on" in response.lower() or "ligar" in response.lower():
                print("Luz ligada!")
                # Substitua com o comando para ligar a luz ou relé
                # Exemplo: enviar um comando para ligar a lâmpada/relé
                irc.send(f"PRIVMSG {channels[0]} :Ligar luz\r\n".encode())  # Enviar comando para ligar luz
            elif "off" in response.lower() or "desligar" in response.lower():
                print("Luz desligada!")
                # Substitua com o comando para desligar a luz ou relé
                # Exemplo: enviar um comando para desligar a lâmpada/relé
                irc.send(f"PRIVMSG {channels[0]} :Desligar luz\r\n".encode())  # Enviar comando para desligar luz

            time.sleep(1)  # Atraso para evitar sobrecarga do servidor
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        irc.close()

# Conectar ao IRC e enviar comandos
connect_to_irc()
