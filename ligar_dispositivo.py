import socket
import time

# Função para conectar ao IRC
def conectar_irc():
    try:
        # Endereço do servidor e a porta
        irc_server = "192.168.1.101"
        irc_port = 6668
        irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        irc_socket.connect((irc_server, irc_port))

        # Entrar com NICK e USER
        irc_socket.send(bytes("NICK rele_bot\r\n", "UTF-8"))
        irc_socket.send(bytes("USER nome_do_usuario 0 * :Controle\r\n", "UTF-8"))
        print(f"Conectado ao servidor {irc_server} na porta {irc_port}")

        return irc_socket

    except Exception as e:
        print(f"Erro ao conectar ao servidor: {e}")
        return None

# Função para entrar no canal
def entrar_no_canal(irc_socket, canal):
    try:
        # Enviar comando JOIN para entrar no canal
        irc_socket.send(bytes(f"JOIN {canal}\r\n", "UTF-8"))
        print(f"Entrando no canal {canal}")

        # Esperar resposta do servidor (pode demorar)
        response = irc_socket.recv(2048).decode("utf-8")
        print("Resposta do servidor:", response)

        if "JOIN" in response:
            print(f"Conectado ao canal {canal}")
        else:
            print(f"Falha ao entrar no canal {canal}, resposta: {response}")
            return False

        return True

    except Exception as e:
        print(f"Erro ao entrar no canal {canal}: {e}")
        return False

# Função para enviar comandos de controle (on/off)
def enviar_comando(irc_socket, canal, comando):
    try:
        # Enviar comando de ligar/desligar
        comando_ir = f"{comando}\r\n"
        irc_socket.send(bytes(f"PRIVMSG {canal} :{comando_ir}", "UTF-8"))
        print(f"Comando '{comando}' enviado para o canal {canal}")

        # Esperar resposta do servidor
        response = irc_socket.recv(2048).decode("utf-8")
        print(f"Resposta recebida do canal {canal}: {response}")

    except Exception as e:
        print(f"Erro ao enviar comando {comando} para o canal {canal}: {e}")

# Função principal
def main():
    # Conectar ao IRC
    irc_socket = conectar_irc()
    if irc_socket is None:
        return

    canais = ["#Luz_de_fora", "#luz_externa", "#luz_fora"]
    
    # Entrar nos canais
    for canal in canais:
        if not entrar_no_canal(irc_socket, canal):
            continue  # Se falhar em um canal, tenta o próximo

    # Testar os comandos on/off nos canais
    comandos = ["on", "off"]
    for comando in comandos:
        for canal in canais:
            enviar_comando(irc_socket, canal, comando)
            time.sleep(2)  # Aguarda 2 segundos antes de enviar o próximo comando

    # Fechar a conexão
    irc_socket.close()
    print("Conexão com o servidor IRC encerrada.")

if __name__ == "__main__":
    main()
