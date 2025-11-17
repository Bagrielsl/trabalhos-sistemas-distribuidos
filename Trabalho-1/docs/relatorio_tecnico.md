# Relatório Técnico: TriProtocol - Implementação e Análise Comparativa de Clientes Multi-Protocolo

**Aluno:** GABRIEL MIRANDA DOS SANTOS
**Matrícula:** 497314

---

## 1. Introdução

### 1.1. Objetivo

Este relatório detalha o primeiro projeto prático da disciplina de Sistemas Distribuídos, que consistiu na implementação de clientes para três protocolos de comunicação distintos: **Strings**, **JSON** e **Protocol Buffers**.

O objetivo central foi conectar a servidores remotos fornecidos, executar um conjunto completo de operações e, ao final, realizar uma análise comparativa sobre o desempenho, complexidade de implementação e facilidade de depuração de cada abordagem.

### 1.2. Metodologia

A implementação seguiu a abordagem sugerida pela especificação. Os três clientes foram desenvolvidos na linguagem **Python**, utilizando os servidores fornecidos pelo professor. O desenvolvimento progrediu do protocolo mais simples (Strings) para o mais complexo (Protocol Buffers).

---

## 2. Arquitetura e Decisões de Implementação

### 2.1. Ferramentas e Linguagem

* **Linguagem:** Python foi escolhido por sua simplicidade e suas robustas bibliotecas padrão.
* **Comunicação:** A biblioteca padrão `socket` foi usada para toda a comunicação TCP/IP.
* **Serialização JSON:** A biblioteca padrão `json` foi usada para serializar (`dumps`) e desserializar (`loads`) as mensagens.
* **Serialização Protobuf:** A biblioteca `protobuf` do Google foi usada. O compilador `protoc` foi utilizado para gerar o arquivo `sd_protocol_pb2.py` a partir do schema `.proto` fornecido pelo professor.

### 2.2. Gestão de Sessão e Fluxo

Para todos os três clientes, uma **única conexão TCP persistente** (`with socket.socket...`) foi estabelecida e mantida durante todo o ciclo de vida da aplicação.

O fluxo de comunicação seguiu o padrão exigido:
1.  **AUTH:** O cliente se autentica com a matrícula e armazena o `token` recebido.
2.  **OPERAÇÕES:** O `token` armazenado é enviado em cada operação subsequente (Echo, Soma, Timestamp, Status, Histórico).
3.  **LOGOUT:** O cliente envia o comando de logout para encerrar a sessão.

### 2.3. Tratamento de Erros

O tratamento de erros foi implementado em dois níveis, conforme os requisitos:

1.  **Erros de Rede:** Blocos `try...except` foram usados para capturar `ConnectionRefusedError` (servidor offline ou porta errada) e `socket.timeout`. Um timeout de 30 segundos foi definido para as operações do socket, conforme especificado.
2.  **Erros de Protocolo:** Após cada envio de comando, a resposta do servidor era verificada.
    * No cliente **Strings**, a verificação `if resposta.startswith("OK")` era usada.
    * Nos clientes **JSON** e **Protobuf**, os campos `if resposta_json['sucesso']` e `if resposta.WhichOneof('tipo') == 'ok'` eram verificados.
    * Caso qualquer verificação falhasse (especialmente no `AUTH`), uma exceção era levantada para interromper o script e impedir a execução de operações com um token inválido.

---

## 3. Análise Comparativa

Esta seção compara os três protocolos com base na experiência prática de implementação e depuração.

| Critério | Protocolo Strings (Porta 8080) | Protocolo JSON (Porta 8081) | Protocolo Protocol Buffers (Porta 8082) |
| :--- | :--- | :--- | :--- |
| **Complexidade de Implementação** | **Baixa para Conectar, Alta para Usar.** A conexão foi simples, mas o parsing das mensagens foi frágil e propenso a erros. Descobrir o formato correto dos parâmetros foi um processo de tentativa e erro (ex: a operação `soma` exigiu `nums=10,20,30` e não `[10,20,30]` ou `numeros=10|numeros=20`). | **Baixa.** A biblioteca `json` lidou nativamente com a conversão de dicionários (`dict`) Python para strings JSON. Tipos como listas (`[10, 20]`) e booleanos (`True`) foram tratados automaticamente, tornando o código limpo e direto. | **Alta.** Foi o mais complexo. Exigiu a instalação de um compilador (`protoc`), a geração de código (`.py` a partir do `.proto`), e a manipulação de dados binários, além de um empacotamento (`struct.pack`) do **cabeçalho de 4 bytes** exigido pela especificação. |
| **Facilidade de Debugging** | **Muito Alta.** Sendo texto plano, foi possível imprimir (`print()`) a requisição e a resposta no terminal. Erros do servidor (ex: `msg='numeros' deve ser uma lista`) foram importantes para a depuração. | **Alta.** Similar ao Strings, o JSON é legível por humanos. O uso de `json.dumps(..., indent=4)` tornou a visualização das estruturas de requisição e resposta muito clara. | **Muito Baixa.** O payload é binário e, portanto, ilegível. O debugging dependeu 100% de ter o `.proto` correto. Um erro no cabeçalho ou na serialização resultaria em um erro de timeout ou conexão fechada, sem uma mensagem de erro clara. |
| **Eficiência de Rede (Overhead)** | **Baixa (Alto Overhead).** É o mais verboso. Cada mensagem repete chaves (`operacao=`, `token=`), parâmetros (`timestamp=`) e o terminador (`|FIM`). | **Média.** Mais eficiente que Strings, pois é mais compacto e não usa o terminador `|FIM`. No entanto, ainda envia as chaves (`"token"`, `"parametros"`) como texto em todas as chamadas. | **Excelente (Baixo Overhead).** A mensagem é binária e extremamente compacta. As "chaves" são representadas por números de campo (`auth = 1`, `operacao = 2`), economizando muito espaço. O tamanho do payload foi visivelmente menor. |
| **Tipagem e Rigidez (Schema)** | **Nenhuma.** Tudo é string. Tipos complexos, como a lista de números da `soma`, tiveram que ser "achatados" para uma string (`"10,20,30"`), exigindo parsing manual. | **Fraca, mas Estruturada.** O JSON suporta tipos básicos (string, número, booleano, array), o que diminuiu a necessidade de conversão manual de listas, como visto na operação `soma`. | **Forte.** O schema `.proto` é um contrato rígido. O `oneof` garantiu que uma requisição não poderia ser `auth` e `operacao` ao mesmo tempo. O uso de `map` para parâmetros também foi estritamente definido. |

---

## 4. Conclusões

Este projeto demonstrou na prática os pros e contras fundamentais entre diferentes paradigmas de comunicação.

1.  O **Protocolo Strings** é simples de iniciar, mas sua fragilidade, falta de tipagem e a necessidade de "adivinhar" formatos de parâmetros o tornam inadequado para sistemas robustos. Sua facilidade de debug é seu único ponto forte.

2.  O **Protocol Buffers** é, sem dúvida, o mais performático em termos de tamanho e velocidade. No entanto, essa performance tem um custo alto em complexidade de implementação (compilação, cabeçalhos binários) e dificuldade de depuração.

3.  O **JSON** provou ser o balanço ideal entre os três. Ele oferece legibilidade humana (facilitando o debug), facilidade de implementação com bibliotecas nativas, e um formato estruturado que suporta tipos básicos (listas, números).