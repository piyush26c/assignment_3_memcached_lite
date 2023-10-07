import socket
import threading
import json
import os
import sys
from google.cloud import storage

class GoogleCloudStorageFileIO:
    def __init__(self, file_name, bucket_name="eccassignment") -> None:
        self.file_name = file_name
        self.bucket_name = bucket_name
         # Create a client for interacting with the GCP Storage API, using the ServiceAccount key file
        self.gcsclient = storage.Client.from_service_account_json('piyush-chaudhari-fall2023-9600b4eeb5b1.json')
        self.bucket = None
        self.blob = None
        
        # check first bucket exists and if yes, whether do file?
        self.bucket= self.gcsclient.get_bucket(self.bucket_name)
        if not self.bucket:
                self.bucket = self.gcsclient.create_bucket(self.bucket_name, location='US-EAST1')
                # Creates new blob object
                self.blob = self.bucket.blob(file_name)

                # Creates empty json file in blob storage
                with open(file_name, 'w') as f:
                    json.dump({}, f)

                with open(file_name, 'rb') as f:
                    contents = f.read()

                self.blob.upload_from_string(contents)
        else:
            self.bucket= self.gcsclient.get_bucket(self.bucket_name)
            # Check if the bucket contains the file
            if self.bucket.blob(self.file_name).exists():
                self.blob = self.bucket.get_blob(file_name)
            else:
                # Creates new blob object
                self.blob = self.bucket.blob(file_name)

                # Creates empty json file in blob storage
                with open(file_name, 'w') as f:
                    json.dump({}, f)

                with open(file_name, 'rb') as f:
                    contents = f.read()

                self.blob.upload_from_string(contents)

    def save_to_file(self, key, value):
        self.blob = self.bucket.get_blob(self.file_name)
        json_data_string = self.blob.download_as_string()
        json_data = json.loads(json_data_string.decode("utf-8"))
        json_data[key] = value
        
        #save to file in blob
        self.gcsclient.get_bucket(self.bucket_name).blob(self.file_name).upload_from_string(json.dumps(json_data, indent=4).encode("utf-8"))

    def read_from_file(self, to_get_key):
        self.blob = self.bucket.get_blob(self.file_name)
        json_data_string = self.blob.download_as_string()
        json_data = json.loads(json_data_string.decode("utf-8"))
        if to_get_key in json_data.keys():
            return json_data[to_get_key]
        
        return ""

class Server(GoogleCloudStorageFileIO):
    def __init__(self, port_no, bucket_name="eccassignment", file_name="key_value.json", max_clients=5, max_key_size_bytes=1024):
        self.port_no = port_no
        self.host_name = "0.0.0.0" #socket.gethostname()
        self.max_clients = max_clients
        self.file_name = file_name
        self.max_key_size_bytes = max_key_size_bytes
        self.GoogleCloudStorageFileIO = GoogleCloudStorageFileIO(file_name=file_name, bucket_name=bucket_name)
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
                    value = self.GoogleCloudStorageFileIO.read_from_file(key)
                    if len(value) > 0:
                        response = f"VALUE {key} {len(value)}\r\n{value}\r\nEND\r\n"
                    else:
                        response = "END\r\n"

            elif parts[0] == 'set':
                key = parts[1]
                value_size = int(parts[2])
                value = client_connection.recv(value_size).decode('utf-8').strip()
                with self.lock:
                    self.GoogleCloudStorageFileIO.save_to_file(key, value)
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
    if len(sys.argv) == 6:
        host_name = "0.0.0.0" #socket.gethostname()
        port_no = int(sys.argv[1])
        max_clients = int(sys.argv[2])
        file_name = str(sys.argv[3])
        max_key_size_bytes = int(sys.argv[4])
        bucket_name = str(sys.argv[5])
        server_obj = Server(port_no=port_no, file_name=file_name, max_clients=max_clients, max_key_size_bytes=max_key_size_bytes, bucket_name=bucket_name)
        server_obj.excecute_server()
    else:
        print("Inappropriate number of arguments (eg. python3 server_gcs.py <port_number> <max_clients_that_can_wait_in_queue_if_server_busy> <file_name> <max_key_size_in_bytes> <bucket_name>)")
    
# npx kill-port <port-no>