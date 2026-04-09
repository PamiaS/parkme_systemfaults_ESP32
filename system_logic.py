#This gets the parking spots and system status(ethernet and serial) and Catogorizes it into sections for display.
def get_parking_status(spots):

    if spots is None:
        return "RED", "No Data"

    if spots >= 15:
        return "GREEN", "Plenty Available"

    elif spots > 0:
        return "YELLOW", "Limited Availability"

    else:
        return "RED", "Lot Full"


def get_system_status(ethernet_ok, serial_ok):

    if ethernet_ok:
        return "ONLINE"

    elif serial_ok:
        return "DEGRADED"

    else:
        return "FAULT"
