import irc.client

def on_connect(connection, event):
    connection.join("#canal")

def on_join(connection, event):
    connection.privmsg("#canal", "Olá, servidor IRC!")

client = irc.client.Reactor()
try:
    client.server().connect("192.168.1.101", 6668, "nome_de_usuario")
except irc.client.ServerConnectionError as e:
    print("Falha na conexão:", e)
    exit(1)

client.process_forever()
