import irc.bot
import time

class RelayControlBot(irc.bot.SingleServerIRCBot):
    def __init__(self, server, port, channel, nickname, password=None):
        self.channel = channel
        self.nickname = nickname
        self.password = password

        # Conectar ao servidor IRC
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)

    def on_welcome(self, c, e):
        print(f"Conectado ao servidor IRC {server}:{port}. Entrando no canal {self.channel}...")
        c.join(self.channel)

        if self.password:
            # Se precisar de uma senha para o canal, envie a senha aqui
            c.privmsg(self.channel, self.password)

    def on_pubmsg(self, c, e):
        """Responde aos comandos no canal"""
        message = e.arguments[0].lower()

        if message == "ligar":
            self.control_relay("ligar")
        elif message == "desligar":
            self.control_relay("desligar")
        else:
            print(f"Comando desconhecido: {message}")

    def control_relay(self, command):
        """Simula o controle de relé - substituir por comandos reais do dispositivo"""
        if command == "ligar":
            print("Ligando o relé...")
            # Aqui você pode adicionar o código real para ligar o relé via IRC
        elif command == "desligar":
            print("Desligando o relé...")
            # Aqui você pode adicionar o código real para desligar o relé via IRC

    def on_disconnect(self, c, e):
        print("Desconectado do servidor IRC")
        raise SystemExit()

# Configurações do servidor IRC e canal
server = "192.168.1.101"  # IP do servidor IRC
port = 6668  # Porta IRC (geralmente 6668 ou 6667)
channel = "#sala"  # Canal IRC em que o relé está
nickname = "ReléBot"  # Nome de usuário para o bot IRC

# Iniciar o bot
bot = RelayControlBot(server, port, channel, nickname)
bot.start()
