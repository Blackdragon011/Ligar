import irc.bot
import time

class RelayControlBot(irc.bot.SingleServerIRCBot):
    def __init__(self, server, port, channel, nickname):
        self.channel = channel
        self.nickname = nickname
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)

    def on_welcome(self, c, e):
        print(f"Conectado ao servidor {server}:{port}. Entrando no canal {self.channel}...")
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        message = e.arguments[0].lower()

        if message == "ligar":
            self.control_relay("ligar")
        elif message == "desligar":
            self.control_relay("desligar")
        else:
            print(f"Comando desconhecido: {message}")

    def control_relay(self, command):
        if command == "ligar":
            print("Enviando comando para ligar o relé...")
            # Enviar comando IRC para ligar o relé
            self.connection.privmsg(self.channel, "ligar")  # Substitua "ligar" pelo comando correto do seu relé
            print("Lâmpada ligada!")

        elif command == "desligar":
            print("Enviando comando para desligar o relé...")
            # Enviar comando IRC para desligar o relé
            self.connection.privmsg(self.channel, "desligar")  # Substitua "desligar" pelo comando correto do seu relé
            print("Lâmpada desligada!")

if __name__ == "__main__":
    server = "192.168.1.101"  # IP do servidor IRC
    port = 6668  # Porta do servidor IRC
    channel = "#sala"  # Canal IRC
    nickname = "RelayBot"  # Nome do bot no IRC
    bot = RelayControlBot(server, port, channel, nickname)
    bot.start()
