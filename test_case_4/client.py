import socket
import sys
import threading

def connect_to_client(client_id, host_name, port):
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host_name, port))
    set_command = f"set key_{client_id} {len(str(client_id))}"
    client_socket.send(set_command.encode('utf-8'))
    client_socket.send(f"{str(client_id)}".encode('utf-8'))
    response = client_socket.recv(9000).decode('utf-8')
    get_command = f"get key_{client_id}"
    client_socket.send(get_command.encode('utf-8'))
    response = client_socket.recv(9000).decode('utf-8')
    print(f"Client {client_id} received response: {response}")
    
    


if __name__ == '__main__':
    """
    Test case - 04:
    Check what maximum number of clients can be connected to server.
    """
    if len(sys.argv) == 4:
        host_name = str(sys.argv[2])
        port = int(sys.argv[1])
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host_name, port))

        number_of_clients = int(sys.argv[3])
        threads = []

        for i in range(number_of_clients):
            client_thread_instance = threading.Thread(target=connect_to_client, args=(i, host_name, port))
            threads.append(client_thread_instance)

        # Start all client threads
        for thread in threads:
            thread.start()

        # Wait for all client threads to finish
        for thread in threads:
            thread.join()
        client_socket.close()
    else:
        print("Inappropriate arguments passed. (eg. python3 client.py <port_number> <server_ip_address> <number_of_clients_connect_to_server>)")
