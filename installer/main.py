import win32com.client
import re
import asyncio
from serial.tools.list_ports_common import ListPortInfo
from db.db import init_db
from db.models import Device, Company, Sector, Customer, EventLog, Order, Product


def extract_vid_pid(device_string):
    pattern = r"VID_([0-9A-Fa-f]{4})&PID_([0-9A-Fa-f]{4})"
    match = re.search(pattern, device_string)

    if match:
        vid = match.group(1)
        pid = match.group(2)
        return vid, pid
    else:
        return None, None


def monitor_devices():
    wmi = win32com.client.GetObject("winmgmts:")
    devices = wmi.InstancesOf("Win32_PnPEntity")

    connected_devices = {device.DeviceID for device in devices}

    print("Monitorando dispositivos")
    while True:
        devices = wmi.InstancesOf("Win32_PnPEntity")
        new_devices = {device.DeviceID for device in devices}

        added = new_devices - connected_devices

        if added:
            print("Dispositivo encontrado!")
            return added

        connected_devices = new_devices


def find_serial(product_id: int, vendor_id: int) -> ListPortInfo:
    from serial.tools import list_ports

    while True:
        ports = list_ports.comports()

        for port in ports:
            if (vendor_id in port.hwid) and (product_id in port.hwid):
                return port


async def read_serial_data(product_id: int, vendor_id: int, sector_id: str):
    try:
        from serial import Serial

        device_info = find_serial(product_id, vendor_id)

        device_serial_port = device_info.device
        device = Serial(device_serial_port, 9600, timeout=1)

        while True:
            try:
                if device.in_waiting > 0:
                    line = device.readline().decode("utf-8").strip()

                    product = await Product().get(code=line)

                    if not product:
                        print("Produto não encontrado!")
                        return

                    log = await EventLog().create(
                        sector_id=sector_id, product_id=product.id
                    )

                    print(f"Registro de setor criado: {log}")
            except KeyboardInterrupt:
                print("\nLeitura serial interrompida (Ctrl+C).")
                break
        device.close()
    except Exception as e:
        print(f"Erro ao ler dados do dispositivo: {e}")


def check_serial_device(product_id: int, vendor_id: int) -> ListPortInfo:
    try:
        from serial import Serial

        device_info = find_serial(product_id, vendor_id)

        device_serial_port = device_info.device
        device = Serial(device_serial_port, 9600, timeout=1)

        device.close()

        return device_info
    except Exception as e:
        print(f"Erro ao acessar o dispositivo: {e}")


async def main():
    await init_db()

    company = await Company.get_or_create(name="Empresa", cnpj="12837938462837")

    if company[1]:
        print(f"Empresa criada: {company[0]}")
    else:
        print(f"Empresa já existente: {company[0]}")

    sector = await Sector.get_or_create(name="LAPIDAÇÃO", company_id=company[0].id)
    print(f"Setor: {sector[0]}")

    if sector[1]:
        print(f"Setor criado: {sector[0]}")
    else:
        print(f"Setor já existente: {sector[0]}")

    customer = await Customer.get_or_create(name="Customer", document="112873923864")

    if customer[1]:
        print(f"Cliente criado: {customer[0]}")
    else:
        print(f"Cliente já existente: {customer[0]}")

    order = await Order.get_or_create(customer_id=customer[0].id, region=2)

    if order[1]:
        print(f"Pedido (OS) criada: {order[0]}")
    else:
        print(f"Pedido (OS) já existente: {order[0]}")

    product = await Product.get_or_create(
        name="PORTA CORRER VERDE 10MM TEMPERADO",
        width=716,
        height=2090,
        code="113037269020",
        order_id=order[0].id,
    )

    if product[1]:
        print(f"Produto criado: {product[0]}")
    else:
        print(f"Produto já existente: {product[0]}")

    devices = monitor_devices()

    if devices:
        vid, pid = extract_vid_pid(next(iter(devices)))
        device_info = check_serial_device(pid, vid)

        db_device = await Device.get_or_create(
            port=device_info.device,
            hwid=device_info.hwid,
            manufacturer=device_info.manufacturer,
            serial_number=device_info.serial_number,
            sector_id=sector[0].id,
        )

        if db_device[1]:
            print(f"Dispositivo criado! ID: {db_device[0].id}")
        else:
            print(f"Dispositivo já existente: {db_device[0]}")

        await read_serial_data(pid, vid, sector[0].id)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()

    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        loop.close()
    finally:
        print("Program finished")
