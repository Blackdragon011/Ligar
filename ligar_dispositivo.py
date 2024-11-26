import requests

def ligar_dispositivo(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Dispositivo ligado com sucesso!")
        else:
            print("Falha ao ligar o dispositivo. Status:", response.status_code)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar: {e}")

# URL do dispositivo (exemplo de IP local)
url_do_dispositivo = "http://192.168.1.100/ligar"
ligar_dispositivo(url_do_dispositivo)
