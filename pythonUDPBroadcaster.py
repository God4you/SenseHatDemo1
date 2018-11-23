from sense_hat import SenseHat
from time import sleep
import socket
sense = SenseHat()
sense.clear()

def setup_udp_socket():
    # Setup UDP socket for broadcasting
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Set a timeout so the socket does not block
    # indefinitely when trying to receive data.
    s.settimeout(0.2)

    #socket.bind(("", 44444))
    return s

s = setup_udp_socket()


while True:
    bg = (0,0,0)
    temp = str(sense.get_temperature())

    # Broadcast byte encoded message to port 37020 via UDP Socket
    # .encode() converts message to bytes for udp to broadcast
    s.sendto(temp.encode(), ('<broadcast>', 37020))

    sense.show_message(temp, scroll_speed=0.05, back_colour=bg)
    sleep(1)
