import socket
import time
import json

HOST = "3.88.99.255"
PORT = 8081

MATRICULA = ""

print(f"Conectando a {HOST}:{PORT}...")
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))

except ConnectionRefusedError:
    print("Erro: A conexão foi recusada.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")