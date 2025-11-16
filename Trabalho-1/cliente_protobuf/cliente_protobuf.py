import socket
import time
import struct
import sd_protocol_pb2

HOST = "3.88.99.255"
PORT = 8082

MATRICULA = "497314"

print(f"Conectando a {HOST}:{PORT}...")
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(30.0)
        sock.connect((HOST, PORT))
        req_auth = sd_protocol_pb2.Requisicao()
        req_auth.auth.aluno_id = MATRICULA
        req_auth.auth.timestamp_cliente = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
        payload_binario = req_auth.SerializeToString()
        tamanho_payload = len(payload_binario)
        cabecalho = struct.pack("!I", tamanho_payload)

        print(f"Enviando AUTH (Cabeçalho: 4 bytes, Payload: {tamanho_payload} bytes)")
        sock.sendall(cabecalho)
        sock.sendall(payload_binario)

        cabecalho_resposta = sock.recv(4)
        if not cabecalho_resposta:
            raise Exception("Conexão perdida (sem cabeçalho de resposta)")
        
        tamanho_resposta = struct.unpack("!I", cabecalho_resposta)[0]
        payload_resposta = sock.recv(tamanho_resposta)
        
        resposta = sd_protocol_pb2.Resposta()
        resposta.ParseFromString(payload_resposta)
        
        tipo_resposta = resposta.WhichOneof('tipo') 
        
        if tipo_resposta == 'ok':
            dados = resposta.ok.dados
            token = dados.get('token')
            if not token:
                raise Exception("Sucesso, mas token não foi recebido.")
            print(f"Resposta: {dados}")
            
            # Operacao ECHO
            req_echo = sd_protocol_pb2.Requisicao()
            req_echo.operacao.token = token
            req_echo.operacao.operacao = "echo"
            req_echo.operacao.parametros["mensagem"] = "olá mundo"
            payload_binario = req_echo.SerializeToString()
            tamanho_payload = len(payload_binario)
            cabecalho = struct.pack("!I", tamanho_payload)

            print(f"Enviando ECHO (Cabeçalho: 4 bytes, Payload: {tamanho_payload} bytes)")
            sock.sendall(cabecalho)
            sock.sendall(payload_binario)

            cabecalho_resposta = sock.recv(4)
            if not cabecalho_resposta:
                raise Exception("Conexão perdida (sem cabeçalho de resposta)")
            
            tamanho_resposta = struct.unpack("!I", cabecalho_resposta)[0]
            payload_resposta = sock.recv(tamanho_resposta)
            
            resposta = sd_protocol_pb2.Resposta()
            resposta.ParseFromString(payload_resposta)
            if resposta.WhichOneof('tipo') == 'ok':
                dados = resposta.ok.dados
                print(f"Resposta: {dados}")
            
            #Operacao SOMA
            req_soma = sd_protocol_pb2.Requisicao()
            req_soma.operacao.token = token
            req_soma.operacao.operacao = "soma"
            req_soma.operacao.parametros["numeros"] = "10, 20, 30"
            payload_binario = req_soma.SerializeToString()
            tamanho_payload = len(payload_binario)
            cabecalho = struct.pack("!I", tamanho_payload)

            print(f"Enviando SOMA (Cabeçalho: 4 bytes, Payload: {tamanho_payload} bytes)")
            sock.sendall(cabecalho)
            sock.sendall(payload_binario)

            cabecalho_resposta = sock.recv(4)
            if not cabecalho_resposta:
                raise Exception("Conexão perdida (sem cabeçalho de resposta)")
            
            tamanho_resposta = struct.unpack("!I", cabecalho_resposta)[0]
            payload_resposta = sock.recv(tamanho_resposta)
            
            resposta = sd_protocol_pb2.Resposta()
            resposta.ParseFromString(payload_resposta)
            if resposta.WhichOneof('tipo') == 'ok':
                dados = resposta.ok.dados
                print(f"Resposta: {dados}")

            #Operacao TIMESTAMP
            req_timestamp = sd_protocol_pb2.Requisicao()
            req_timestamp.operacao.token = token
            req_timestamp.operacao.operacao = "timestamp"
            payload_binario = req_timestamp.SerializeToString()
            tamanho_payload = len(payload_binario)
            cabecalho = struct.pack("!I", tamanho_payload)

            print(f"Enviando TIMESTAMP (Cabeçalho: 4 bytes, Payload: {tamanho_payload} bytes)")
            sock.sendall(cabecalho)
            sock.sendall(payload_binario)

            cabecalho_resposta = sock.recv(4)
            if not cabecalho_resposta:
                raise Exception("Conexão perdida (sem cabeçalho de resposta)")
            
            tamanho_resposta = struct.unpack("!I", cabecalho_resposta)[0]
            payload_resposta = sock.recv(tamanho_resposta)
            
            resposta = sd_protocol_pb2.Resposta()
            resposta.ParseFromString(payload_resposta)
            if resposta.WhichOneof('tipo') == 'ok':
                dados = resposta.ok.dados
                print(f"Resposta: {dados}")
            
            #Operacao STATUS
            req_status = sd_protocol_pb2.Requisicao()
            req_status.operacao.token = token
            req_status.operacao.operacao = "status"
            req_status.operacao.parametros["detalhado"] = "False"
            payload_binario = req_status.SerializeToString()
            tamanho_payload = len(payload_binario)
            cabecalho = struct.pack("!I", tamanho_payload)

            print(f"Enviando STATUS (Cabeçalho: 4 bytes, Payload: {tamanho_payload} bytes)")
            sock.sendall(cabecalho)
            sock.sendall(payload_binario)

            cabecalho_resposta = sock.recv(4)
            if not cabecalho_resposta:
                raise Exception("Conexão perdida (sem cabeçalho de resposta)")
            
            tamanho_resposta = struct.unpack("!I", cabecalho_resposta)[0]
            payload_resposta = sock.recv(tamanho_resposta)
            
            resposta = sd_protocol_pb2.Resposta()
            resposta.ParseFromString(payload_resposta)
            if resposta.WhichOneof('tipo') == 'ok':
                dados = resposta.ok.dados
                print(f"Resposta: {dados}")

            #Operacao HISTORICO
            req_historico = sd_protocol_pb2.Requisicao()
            req_historico.operacao.token = token
            req_historico.operacao.operacao = "historico"
            req_historico.operacao.parametros["limite"] = "6"
            payload_binario = req_historico.SerializeToString()
            tamanho_payload = len(payload_binario)
            cabecalho = struct.pack("!I", tamanho_payload)

            print(f"Enviando HISTORICO (Cabeçalho: 4 bytes, Payload: {tamanho_payload} bytes)")
            sock.sendall(cabecalho)
            sock.sendall(payload_binario)

            cabecalho_resposta = sock.recv(4)
            if not cabecalho_resposta:
                raise Exception("Conexão perdida (sem cabeçalho de resposta)")
            
            tamanho_resposta = struct.unpack("!I", cabecalho_resposta)[0]
            payload_resposta = sock.recv(tamanho_resposta)
            
            resposta = sd_protocol_pb2.Resposta()
            resposta.ParseFromString(payload_resposta)
            if resposta.WhichOneof('tipo') == 'ok':
                dados = resposta.ok.dados
                print(f"Resposta: {dados}")
            
            #Logout
            req_logout = sd_protocol_pb2.Requisicao()
            req_logout.logout.token = token
            payload_binario = req_logout.SerializeToString()
            tamanho_payload = len(payload_binario)
            cabecalho = struct.pack("!I", tamanho_payload)

            print(f"Enviando LOGOUT (Cabeçalho: 4 bytes, Payload: {tamanho_payload} bytes)")
            sock.sendall(cabecalho)
            sock.sendall(payload_binario)

            cabecalho_resposta = sock.recv(4)
            if not cabecalho_resposta:
                raise Exception("Conexão perdida (sem cabeçalho de resposta)")
            
            tamanho_resposta = struct.unpack("!I", cabecalho_resposta)[0]
            payload_resposta = sock.recv(tamanho_resposta)
            
            resposta = sd_protocol_pb2.Resposta()
            resposta.ParseFromString(payload_resposta)
            if resposta.WhichOneof('tipo') == 'ok':
                dados = resposta.ok.dados
                print(f"Resposta: {dados}")
        
        elif tipo_resposta == 'erro':
            raise Exception(f"Erro do Servidor: {resposta.erro.mensagem}")
        else:
            raise Exception("Resposta mal formatada recebida.")            
except ConnectionRefusedError:
    print("Erro: A conexão foi recusada.")
except socket.timeout:
    print(f"Erro de Rede: Timeout durante a conexão.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    