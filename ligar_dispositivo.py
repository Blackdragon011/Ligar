import socket
import time

# Configuração do servidor IRC
server_ip = '192.168.1.101'
port = 6668

# Nome do canal único
channel = '#luz_externa'

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
        
        # Entra no canal único
        irc.send(f'JOIN {channel}\r\n'.encode())
        print(f"Entrando no canal {channel}")
        time.sleep(2)  # Atraso para garantir que o JOIN seja aceito
        
        # Aguardar comandos ou saída
        while True:
            response = irc.recv(2048).decode()
            print(response)  # Exibe a resposta do servidor IRC
            
            if "PING" in response:
                irc.send("PONG :Pong\r\n".encode())  # Responde ao PING para manter a conexão ativa
            
            # Verifica os comandos de controle de luz
            if "on" in response.lower() or "ligar" in response.lower():
                print(f"Luz ligada no canal {channel}!")
                # Substitua com o comando real para ligar a luz ou relé
                irc.send(f"PRIVMSG {channel} :Ligar luz\r\n".encode())  # Enviar comando para ligar luz
            elif "off" in response.lower() or "desligar" in response.lower():
                print(f"Luz desligada no canal {channel}!")
                # Substitua com o comando real para desligar a luz ou relé
                irc.send(f"PRIVMSG {channel} :Desligar luz\r\n".encode())  # Enviar comando para desligar luz

            # Condição para sair do loop se um comando específico for dado
            if "sair" in response.lower():
                print(f"Saindo do canal {channel}...")
                irc.send("PONG :Pong\r\n".encode())  # Envia para manter a conexão
                break  # Sai do loop do canal

            time.sleep(1)  # Atraso para evitar sobrecarga do servidor

    except Exception as e:
        print(f"Erro ao conectar: {e}")
        irc.close()

# Conectar ao IRC e enviar comandos
connect_to_irc()
