import socket
import time
import json

HOST = "3.88.99.255"
PORT = 8081

MATRICULA = "497314"

print(f"Conectando a {HOST}:{PORT}...")
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(30.0)
        sock.connect((HOST, PORT))
        estrutura_requisicao = {
            "tipo": "autenticar",
            "aluno_id": MATRICULA,
            "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
        }
        mensagem = json.dumps(estrutura_requisicao, indent=4) + "\n"
        sock.sendall(mensagem.encode('utf-8'))
        resposta = sock.recv(1024)
        resposta = json.loads(resposta.decode('utf-8').strip())
        print(f"Recebido: {resposta}")
        token = resposta['token']

        if token:
            #Operacao ECHO
            estrutura_requisicao = {
                "tipo": "operacao",
                "token": token,
                "operacao": "echo",
                "parametros": {
                    "mensagem": "Olá Servidor"
                },
                "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
            }
            mensagem = json.dumps(estrutura_requisicao, indent=4) + "\n"
            sock.sendall(mensagem.encode('utf-8'))
            resposta = sock.recv(1024)
            resposta = json.loads(resposta.decode('utf-8').strip())
            print(f"Recebido: {resposta}")

            #Operacao SOMA
            estrutura_requisicao = {
                "tipo": "operacao",
                "token": token,
                "operacao": "soma",
                "parametros": {
                    "numeros":[10, 20, 30]
                },
                "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
            }
            mensagem = json.dumps(estrutura_requisicao, indent=4) + "\n"
            sock.sendall(mensagem.encode('utf-8'))
            resposta = sock.recv(1024)
            resposta = json.loads(resposta.decode('utf-8').strip())
            print(f"Recebido: {resposta}")

            #Operacao TIMESTAMP
            estrutura_requisicao = {
                "tipo": "operacao",
                "token": token,
                "operacao": "timestamp",
                "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
            }
            mensagem = json.dumps(estrutura_requisicao, indent=4) + "\n"
            sock.sendall(mensagem.encode('utf-8'))
            resposta = sock.recv(1024)
            resposta = json.loads(resposta.decode('utf-8').strip())
            print(f"Recebido: {resposta}")

            #Operacao STATUS
            estrutura_requisicao = {
                "tipo": "operacao",
                "token": token,
                "parametros": {
                    "detalhado": True
                },
                "operacao": "status",
                "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
            }
            mensagem = json.dumps(estrutura_requisicao, indent=4) + "\n"
            sock.sendall(mensagem.encode('utf-8'))
            resposta = sock.recv(2048)
            resposta = json.loads(resposta.decode('utf-8').strip())
            print(f"Recebido: {resposta}")

            #Operacao HISTORICO
            estrutura_requisicao = {
                "tipo": "operacao",
                "token": token,
                "parametros": {
                    "limite": 6
                },
                "operacao": "historico",
                "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
            }
            mensagem = json.dumps(estrutura_requisicao, indent=4) + "\n"
            sock.sendall(mensagem.encode('utf-8'))
            resposta = sock.recv(1024)
            resposta = json.loads(resposta.decode('utf-8').strip())
            print(f"Recebido: {resposta}")

            #LOGOUT
            estrutura_requisicao = {
                "tipo": "logout",
                "token": token,
                "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
            }
            mensagem = json.dumps(estrutura_requisicao, indent=4) + "\n"
            sock.sendall(mensagem.encode('utf-8'))
            resposta = sock.recv(1024)
            resposta = json.loads(resposta.decode('utf-8').strip())
            print(f"Recebido: {resposta}")
        else:
            raise Exception('Resposta OK, mas não foi possível encontrar o token.')
except ConnectionRefusedError:
    print("Erro: A conexão foi recusada.")
except socket.timeout:
    print(f"Erro de Rede: Timeout durante a conexão inicial.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")