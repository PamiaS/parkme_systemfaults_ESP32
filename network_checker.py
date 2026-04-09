import os

def ethernet_connected():
    response = os.system("ping -c 1 google.com > /dev/null 2>&1")
    return response == 0
