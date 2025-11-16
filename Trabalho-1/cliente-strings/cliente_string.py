import socket
import time

HOST = "3.88.99.255"
PORT = 8080

MATRICULA = ""


print(f"Conectando a {HOST}:{PORT}...")
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(30.0)
        sock.connect((HOST, PORT))
        # Operação AUTH
        timestamp = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
        mensagem = f"AUTH|aluno_id={MATRICULA}|TIMESTAMP={timestamp}|FIM\n"
        print(f"Enviando: {mensagem.strip()}")
        sock.sendall(mensagem.encode('utf-8'))
        resposta = sock.recv(1024)
        resposta = resposta.decode('utf-8').strip()
        print(f"Recebido: {resposta}")
        token = ""
        if resposta.startswith("OK"):
            partes = resposta.split("|")
            for parte in partes:
                if parte.startswith("token="):
                    token = parte.split('=', 1)[1]
                    break
            if token:
                print(f"Token extraído com sucesso: {token}")
            else:
                raise Exception('Resposta OK, mas não foi possível encontrar o token.')
        
        # Operação ECHO
        timestamp = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
        mensagem = f"OP|operacao=echo|mensagem=Hello World|token={token}|TIMESTAMP={timestamp}|FIM\n"
        print(f"Enviando: {mensagem.strip()}")
        sock.sendall(mensagem.encode('utf-8'))
        resposta = sock.recv(1024)
        print(f"Recebido: {resposta.decode('utf-8').strip()}")

        # Operação SOMA
        numeros = ["10", "20", "30"]
        numeros_str = ','.join(numeros)
        timestamp = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
        mensagem = f"OP|operacao=soma|nums={numeros_str}|token={token}|TIMESTAMP={timestamp}|FIM\n"
        print(f"Enviando: {mensagem.strip()}")
        sock.sendall(mensagem.encode('utf-8'))
        resposta = sock.recv(1024)
        print(f"Recebido: {resposta.decode('utf-8').strip()}")

        # Operação TIMESTAMP
        timestamp = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
        mensagem = f"OP|operacao=timestamp|token={token}|TIMESTAMP={timestamp}|FIM\n"
        print(f"Enviando: {mensagem.strip()}")
        sock.sendall(mensagem.encode('utf-8'))
        resposta = sock.recv(1024)
        print(f"Recebido: {resposta.decode('utf-8').strip()}")

        # Operação STATUS
        timestamp = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
        mensagem = f"OP|operacao=status|detalhado=false|token={token}|TIMESTAMP={timestamp}|FIM\n"
        print(f"Enviando: {mensagem.strip()}")
        sock.sendall(mensagem.encode('utf-8'))
        resposta = sock.recv(1024)
        print(f"Recebido: {resposta.decode('utf-8').strip()}")

        # Operação HISTORICO
        timestamp = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
        mensagem = f"OP|operacao=historico|limite=6|token={token}|TIMESTAMP={timestamp}|FIM\n"
        print(f"Enviando: {mensagem.strip()}")
        sock.sendall(mensagem.encode('utf-8'))
        resposta = sock.recv(1024)
        print(f"Recebido: {resposta.decode('utf-8').strip()}")

        # INFO
        timestamp = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
        mensagem = f"info|tipo=basico|token={token}|TIMESTAMP={timestamp}|FIM\n"
        print(f"Enviando: {mensagem.strip()}")
        sock.sendall(mensagem.encode('utf-8'))
        resposta = sock.recv(1024)
        print(f"Recebido: {resposta.decode('utf-8').strip()}")
        
        # LOGOUT
        timestamp = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
        mensagem = f"logout|token={token}|TIMESTAMP={timestamp}|FIM\n"
        print(f"Enviando: {mensagem.strip()}")
        sock.sendall(mensagem.encode('utf-8'))
        resposta = sock.recv(1024)
        print(f"Recebido: {resposta.decode('utf-8').strip()}")
except ConnectionRefusedError:
    print("Erro: A conexão foi recusada.")
except socket.timeout:
    print(f"Erro de Rede: Timeout durante a conexão inicial.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
