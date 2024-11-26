import socket
import time

def connect_to_irc():
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc.connect(("192.168.1.101", 6668))  # Conecta ao servidor IRC e à porta
    irc.send(b"NICK rele_bot\r\n")  # Envia o nome do bot
    irc.send(b"USER nome_do_usuario 0 * :Controle\r\n")  # Envia o usuário
    return irc

def join_channels(irc):
    channels = ['#Luz_de_fora', '#luz_externa', '#luz_fora']  # Lista de canais
    for channel in channels:
        irc.send(f"JOIN {channel}\r\n".encode())  # Entra nos canais
        time.sleep(2)  # Aguarda um pouco antes de enviar a próxima mensagem
        print(f"Entrando no canal {channel}")
        
def send_command(irc, channel, command):
    # Envia o comando de ligar ou desligar
    irc.send(f"PRIVMSG {channel} :{command}\r\n".encode())
    print(f"Comando '{command}' enviado para o canal {channel}")
    
def receive_message(irc):
    response = irc.recv(2048).decode("utf-8")  # Recebe a resposta do servidor IRC
    return response

def control_lights():
    irc = connect_to_irc()  # Conecta ao IRC
    join_channels(irc)  # Entra nos canais
    
    # Lógica de controle (ligar ou desligar)
    while True:
        response = receive_message(irc)  # Recebe mensagens do servidor IRC
        if "Ligar" in response:  # Se encontrar o comando "Ligar" na resposta
            send_command(irc, "#Luz_de_fora", "on")  # Ligar a luz no canal Luz_de_fora
            print("Luz ligada!")
        elif "Desligar" in response:  # Se encontrar o comando "Desligar" na resposta
            send_command(irc, "#Luz_de_fora", "off")  # Desligar a luz no canal Luz_de_fora
            print("Luz desligada!")
        time.sleep(1)  # Aguarda 1 segundo antes de tentar novamente

if __name__ == "__main__":
    control_lights()  # Inicia o controle de luz
