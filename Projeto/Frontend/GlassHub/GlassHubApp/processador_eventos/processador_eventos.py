import pika
import os
import json
import time
import requests

# Function to check if dashboard is online
def is_dashboard_online():
    try:
        response = requests.get('http://localhost:8000/dashbord/')  # URL do dashboard
        return response.status_code == 200
    except:
        return False

# Function to send data to Django view
def send_data_to_dashboard(data):
    url = 'http://localhost:8000/update_dashbord_data/'  # Nova URL para atualização de dados
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Dados enviados com sucesso ao dashboard")
        else:
            print(f"Erro ao enviar dados: {response.status_code}")
    except Exception as e:
        print(f"Erro ao conectar com o dashboard: {e}")

# Function to generate fake data if offline
def generate_fake_data():
    return {
        "sector": "SIMULADO",
        "product": "PORTA CORRER AZUL 8MM TEMPERADO",
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "max_idle": 3600
    }

def callback(ch, method, properties, body):
    data = json.loads(body.decode('utf-8'))
    print("Dados recebidos:", data)
    
    # Verificar se o dashboard está online
    if is_dashboard_online():
        send_data_to_dashboard(data)
    else:
        # Enviar dados fictícios caso esteja offline
        fake_data = generate_fake_data()
        print("Enviando dados fictícios:", fake_data)
        send_data_to_dashboard(fake_data)

# Setup RabbitMQ connection and queue
url = os.environ.get('CLOUDAMQP_URL', '')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='eventos_queue', durable=True)

channel.basic_consume('eventos_queue', callback, auto_ack=True)
channel.start_consuming()
connection.close()
