#This file acts as the brain for central logic and gets data from the other files to fill display with accurate data and data source.
#Checks Eternet first and if ethernet is down, it switches automatically to P2P(ESP32)
import time
from serial_reader import get_serial_data
from system_logic import get_parking_status
from network_checker import ethernet_connected

# Optional: track display state
display_active = False

while True:
    # --- Check Ethernet first ---
    if ethernet_connected():
        if display_active:
            print("Ethernet online → Turning P2P display OFF")
            display_active = False
        else:
            print("Ethernet online → Display remains OFF")
        time.sleep(1)
        continue  # skip P2P display updates

    # --- Ethernet is offline, check P2P (ESP32) ---
    serial_data = get_serial_data()

    if serial_data is not None:
        spots = serial_data
        parking_status, message = get_parking_status(spots)

        if not display_active:
            print("P2P connection detected → Turning display ON")
            display_active = True

        # --- Update display ---
        print("P2P Display Active")
        print("Parking Status:", parking_status)
        print("Spots Available:", spots)
        print("Message:", message)
        print("--------------------------")

    else:
        # P2P disconnected or no data
        if display_active:
            print("P2P display ON but ESP32 disconnected → Turning display OFF")
            display_active = False
        else:
            print("No P2P data. Display remains OFF.")

    time.sleep(1)
