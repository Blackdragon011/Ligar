import socket
import time

# Configuração do servidor IRC
server_ip = '192.168.1.101'
port = 6668

# Nomes de canal atualizados
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
            print(response)
            if "PING" in response:
                irc.send("PONG :Pong\r\n".encode())  # Responde ao PING para manter a conexão ativa
            
            # Adicionar condições para ligar/desligar conforme necessário
            if "ligar" in response.lower():
                print("Luz ligada!")
                # Enviar comando para ligar a luz
                # (aqui você pode adicionar o comando específico para ligar a lâmpada ou relé)
            elif "desligar" in response.lower():
                print("Luz desligada!")
                # Enviar comando para desligar a luz
                # (aqui você pode adicionar o comando específico para desligar a lâmpada ou relé)
            time.sleep(1)  # Atraso para evitar sobrecarga do servidor
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        irc.close()

# Conectar ao IRC e enviar comandos
connect_to_irc()
