import usb.core
import usb.util
import serial
import socket
import bluetooth
 
def detect_device_type(device_id):
    # Esta função deve ser implementada para detectar o tipo de dispositivo
    # Exemplo simples: Assume USB e Serial para demonstrar
    if device_id.startswith('USB'):
        return 'USB'
    elif device_id.startswith('SERIAL'):
        return 'SERIAL'
    # Adicione outros tipos conforme necessário
    return 'UNKNOWN'
 
def handle_usb_device(vendor_id, product_id):
    device = usb.core.find(idVendor=vendor_id, idProduct=product_id)
    if device is None:
        raise ValueError('Dispositivo USB não encontrado')
 
    device.set_configuration()
    endpoint = device[0][(0,0)][0]
 
    while True:
        try:
            data = device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
            print('Dados USB recebidos:', data)
        except usb.core.USBError as e:
            if e.args == ('Operation timed out',):
                continue
 
def handle_serial_device(port, baud_rate):
    with serial.Serial(port, baud_rate, timeout=1) as ser:
        while True:
            if ser.in_waiting > 0:
                data = ser.read(ser.in_waiting).decode('utf-8')
                print('Dados Serial recebidos:', data)
 
def handle_bluetooth_device(address):
    service_matches = bluetooth.find_service(address=address)
    if not service_matches:
        print("Serviço Bluetooth não encontrado.")
        return
 
    first_match = service_matches[0]
    port = first_match['port']
    host = first_match['host']
 
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((host, port))
 
    try:
        while True:
            data = sock.recv(1024)
            print('Dados Bluetooth recebidos:', data.decode('utf-8'))
    except bluetooth.BluetoothError as e:
        print(f'Erro Bluetooth: {e}')
    finally:
        sock.close()
 
def handle_network_device(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            data = s.recv(1024)
            if not data:
                break
            print('Dados de Rede recebidos:', data.decode('utf-8'))
 
def main():
    device_id = 'USB\VID_24EA&PID_0197'  
    device_type = detect_device_type(device_id)
 
    if device_type == 'USB':
        vendor_id = 0x24EA
        product_id = 0x0197
        handle_usb_device(vendor_id, product_id)
    elif device_type == 'SERIAL':
        port = 'COM3'
        baud_rate = 9600
        handle_serial_device(port, baud_rate)
    elif device_type == 'BLUETOOTH':
        address = '00:11:22:33:44:55'
        handle_bluetooth_device(address)
    elif device_type == 'NETWORK':
        host = '192.168.1.100'
        port = 12345
        handle_network_device(host, port)
    else:
        print('Tipo de dispositivo desconhecido.')
 
if __name__ == "__main__":
    main()