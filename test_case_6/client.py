import socket
import sys

from pymemcache.client.base import Client

if __name__ == '__main__':
    """
    Test case - 06: Trying for pymemcache compatibility
    """
    if len(sys.argv) == 2:
        host_name = socket.gethostname()
        port = int(sys.argv[1])

        client = Client((host_name, port))
        g = client.set('my_key', 'my_value')
        print(g)
        value = client.get('my_key')
        # print(f'Value for my_key: {value.decode("utf-8")}')
        client.close()
    else:
        print("Inappropriate arguments passed. (eg. python3 client.py <port_number>)")
