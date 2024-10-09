import pika
import os
import json
import time

# Função para converter JSON em uma tabela HTML
def json_to_html_table(data):
    html_content = """
    <html>
    <head><title>Dados JSON</title></head>
    <body>
    <h2>Dados Recebidos</h2>
    <table border="1" cellpadding="10">
      <thead>
        <tr>
          <th>Chave</th>
          <th>Valor</th>
        </tr>
      </thead>
      <tbody>
    """
    for key, value in data.items():
        html_content += f"<tr><td>{key}</td><td>{value}</td></tr>"
    
    html_content += """
      </tbody>
    </table>
    </body>
    </html>
    """
    return html_content

# Função para processar a mensagem PDF (simulação)
def pdf_process_function(msg):
    print("Processando PDF...")
    print(" [x] Mensagem recebida: " + str(msg))
    time.sleep(5)  # Simula o tempo de processamento
    print("Processamento de PDF finalizado")
    return

# Acessa a variável de ambiente CLOUDAMQP_URL ou utiliza localhost
url = os.environ.get('CLOUDAMQP_URL', 'amqps://ocykppqu:W8H4XXAHlsjWg_0LpD3lLE_hd-0ZCNWi@prawn.rmq.cloudamqp.com/ocykppqu')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()  # Inicia um canal
channel.queue_declare(queue='eventos_queue', durable=True)  # Declara a fila

# Função chamada ao receber mensagens
def callback(ch, method, properties, body):
    # Decodifica o corpo da mensagem de bytes para string e carrega o JSON
    data = json.loads(body.decode('utf-8'))
    print("Recebido:", data)

    # Converte o JSON para HTML
    html_output = json_to_html_table(data)
    print(html_output)  # Exibe o HTML no console ou salva em um arquivo

    # Simula processamento de PDF
    pdf_process_function(data)

# Configura a assinatura na fila
channel.basic_consume('eventos_queue', callback, auto_ack=True)

# Inicia o consumo (bloqueante)
print("Aguardando mensagens na fila...")
channel.start_consuming()

# Fecha a conexão
connection.close()
