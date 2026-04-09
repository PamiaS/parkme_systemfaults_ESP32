#This file gets data from the other files to fill display with accurate data and data source
import time
from serial_reader import get_serial_data
from system_logic import get_parking_status, get_system_status
from network_checker import ethernet_connected

while True:

    ethernet_ok = ethernet_connected()
    serial_data = get_serial_data()

    # Determine system status FIRST
    system_status = get_system_status(ethernet_ok, serial_data is not None)


# Choose data source
    if ethernet_ok:
        spots = 40  # simulated network value
        mode = "ETHERNET"
    else:
        spots = serial_data
        mode = "P2P"

    # Determine parking color separately
    parking_status, message = get_parking_status(spots)

    print("Mode:", mode)
    print("System Status:", system_status)
    print("Parking Status:", parking_status)
    print("Spots:", spots)
    print("Message:", message)
    print("--------------------------")

    time.sleep(1)
