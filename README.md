# Trabalhos Sistemas Distribuidos
**Aluno:** GABRIEL MIRANDA DOS SANTOS
**Matrícula:** 497314
**Disciplina:** Sistemas Distribuídos

## Trabalho Prático: Clientes Multi-Protocolo (Strings, JSON, Protobuf)

---

### 1. Visão Geral

Este projeto consiste na implementação de três clientes de rede em Python, cada um se comunicando com um servidor remoto através de um protocolo diferente:

1.  **Protocolo Strings:** Comunicação por texto plano estruturado (Porta 8080).
2.  **Protocolo JSON:** Comunicação por objetos JSON (Porta 8081).
3.  **Protocolo Protocol Buffers:** Comunicação binária serializada (Porta 8082).

O objetivo é executar um fluxo completo de operações (Autenticação, Operações de Negócio e Logout) e comparar as características de cada protocolo.

### 2. Pré-requisitos e Instalação

#### 2.1. Pré-requisitos

* Python 3.7+
* Um terminal (Linux, macOS ou Windows)

#### 2.2. Instalação

1.  Clone este repositório:
    ```bash
    git clone git@github.com:seu-usuario/trabalhos-sistemas-distribuidos.git
    cd trabalhos-sistemas-distribuidos
    ```

2.  Instale a única dependência (biblioteca `protobuf` do Google), necessária para o Cliente Protocol Buffers:
    ```bash
    pip install protobuf
    ```
    *(Os clientes de Strings e JSON não requerem nenhuma biblioteca externa.)*

### 3. Configuração

Antes de executar, verifique se as variáveis globais no topo de cada script (`cliente_string.py`, `cliente_json.py`, `cliente_protobuf.py`) estão corretas:

```python
# IP do servidor (fornecido pelo professor)
HOST = "3.88.99.255" 

# Sua matrícula
MATRICULA = ""
```

### 4. Execução

Para executar cada cliente, navegue até a pasta raiz do projeto e use os seguintes comandos:

#### 4.1 Cliente Strings (Porta 8080)
```bash
python cliente-strings/cliente_string.py
```

#### 4.2 Cliente Json (Porta 8081)
```bash
python cliente-json/cliente_json.py
```

#### 4.3 Cliente Protocol Buffers (Porta 8082)
Este cliente depende do arquivo *sd_protocol_pb2.py* (incluído no repositório) para funcionar.
```bash
python cliente-protobuf/cliente_protobuf.py
```