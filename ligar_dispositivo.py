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
        
        # Processa cada canal individualmente
        for channel in channels:
            # Entra no canal
            irc.send(f'JOIN {channel}\r\n'.encode())
            print(f"Entrando no canal {channel}")
            time.sleep(2)  # Atraso entre as tentativas de entrada
            
            # Aguardar comandos ou saída para cada canal
            while True:
                response = irc.recv(2048).decode()
                print(f"Resposta recebida do canal {channel}: {response}")  # Exibe a resposta do servidor IRC

                if "PING" in response:
                    irc.send("PONG :Pong\r\n".encode())  # Responde ao PING para manter a conexão ativa
                
                # Verifica os comandos de controle de luz (on / off)
                if "on" in response.lower():
                    print(f"Luz no canal {channel} ligada!")
                    # Substitua com o comando real para ligar a luz ou relé
                    irc.send(f"PRIVMSG {channel} :Ligar luz\r\n".encode())  # Enviar comando para ligar luz
                elif "off" in response.lower():
                    print(f"Luz no canal {channel} desligada!")
                    # Substitua com o comando real para desligar a luz ou relé
                    irc.send(f"PRIVMSG {channel} :Desligar luz\r\n".encode())  # Enviar comando para desligar luz

                # Condição para sair do loop se um comando específico for dado
                if "sair" in response.lower():
                    print("Saindo do canal e encerrando...")
                    irc.send(f"PRIVMSG {channel} :Desconectando do canal\r\n".encode())
                    break  # Sai do loop de interação do canal atual

                time.sleep(1)  # Atraso para evitar sobrecarga do servidor

            # Após terminar a interação em um canal, sai para o próximo
            irc.send(f'PART {channel}\r\n'.encode())
            print(f"Saindo do canal {channel}")
            time.sleep(1)  # Atraso antes de passar para o próximo canal

    except Exception as e:
        print(f"Erro ao conectar: {e}")
        irc.close()

# Conectar ao IRC e enviar comandos
connect_to_irc()
