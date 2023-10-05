import socket
import threading
import json
import os
import sys
import time

"""
    Test case - 06: 
    Trying for pymemcache compatibility
"""

class FileIO:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        # create empty JSON file, if not present on disk.
        if not os.path.isfile(file_name):
            with open(file_name, 'w') as f:
                json.dump({}, f)

    def save_to_file(self, key, value):
        try:
            data = None
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                data[key] = value
                
            with open(self.file_name, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as error:
            print("Error occured in saving data to file!", self.file_name)
            print("Error logs: \n", error)

    def read_from_file(self, to_get_key):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                if to_get_key in data.keys():
                    return data[to_get_key]
                return ""
        except IOError as error:
            print("Error occured while reading data from", self.file_name)
            print("Error logs: \n", error)
            return []

class Server(FileIO):
    def __init__(self, port_no, file_name="key_value.json", max_clients=5, max_key_size_bytes=1024):
        self.port_no = port_no
        self.host_name = socket.gethostname()
        self.max_clients = max_clients
        self.file_name = file_name
        self.max_key_size_bytes = max_key_size_bytes
        self.fileIO = FileIO(file_name=file_name)
        self.lock = threading.Lock()

    def connect_to_client(self, client_connection):
        while True:
            request = client_connection.recv(self.max_key_size_bytes).decode('utf-8').strip()           

            if not request:
                break

            parts = request.split()
                  
            if parts[0] == 'get':
                key = parts[1]
                with self.lock:
                    value = self.fileIO.read_from_file(key)
                    if len(value) > 0:
                        response = f"VALUE {key} {len(value)}\r\n{value}\r\nEND\r\n"
                    else:
                        response = "END\r\n"
            elif parts[0] == 'set':
                key = parts[1]
                value_size = int(parts[2])
                value = client_connection.recv(value_size).decode('utf-8').strip()
                with self.lock:
                    self.fileIO.save_to_file(key, value)
                response = "STORED\r\n"
            else:
                response = "NOT-STORED\r\n"

            client_connection.send(response.encode('utf-8'))

        client_connection.close()
    
    def excecute_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host_name, self.port_no))
        server_socket.listen(self.max_clients)

        # logg message (should be)
        print(f"Server listening on {self.host_name}:{self.port_no}")

        while True:
            client_socket, address = server_socket.accept()
            # logg message
            print(f"Accepted connection from {address}")
            client_thread = threading.Thread(target=self.connect_to_client, args=(client_socket,))
            client_thread.start()


if __name__ == '__main__':
    if len(sys.argv) == 5:
        host_name = socket.gethostname()
        port_no = int(sys.argv[1])
        max_clients = int(sys.argv[2])
        file_name = str(sys.argv[3])
        max_key_size_bytes = int(sys.argv[4])
        server_obj = Server(port_no=port_no, file_name=file_name, max_clients=max_clients, max_key_size_bytes=max_key_size_bytes)
        server_obj.excecute_server()
    else:
        print("Inappropriate number of arguments (eg. python3 server.py <port_number> <max_clients_that_can_wait_in_queue_if_server_busy> <file_name> <max_key_size_in_bytes>)")
    
# npx kill-port <port-no>