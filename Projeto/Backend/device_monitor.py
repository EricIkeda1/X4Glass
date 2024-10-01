import win32com.client
 
def monitor_devices():
    wmi = win32com.client.GetObject("winmgmts:")
    devices = wmi.InstancesOf("Win32_PnPEntity")
    
    connected_devices = {device.DeviceID for device in devices}
    
    while True:
        devices = wmi.InstancesOf("Win32_PnPEntity")
        new_devices = {device.DeviceID for device in devices}
        
        added = new_devices - connected_devices
        removed = connected_devices - new_devices
        
        if added:
            print(f"Dispositivos adicionados: {', '.join(added)}")
        if removed:
            print(f"Dispositivos removidos: {', '.join(removed)}")
        
        connected_devices = new_devices
 
if __name__ == "__main__":
    monitor_devices()