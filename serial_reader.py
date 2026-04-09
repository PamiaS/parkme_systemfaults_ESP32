#P2P input
import serial

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

def get_serial_data():
    if ser.in_waiting:
        try:
            return int(ser.readline().decode().strip())
        except:
            return None
    return None
