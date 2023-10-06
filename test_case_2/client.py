import socket
import sys

if __name__ == '__main__':
    """
    Test case - 02:
    Check basic functionality of memcached_lit along with concurrency (here connecting two clients), you explicitly have to open two terminals and have to run this code.
    Here, I have added sleep time at server side before reading and writing (thus, changes done in code are on server side).
    """
    if len(sys.argv) == 3:
        host_name = str(sys.argv[2])
        port = int(sys.argv[1])
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host_name, port))

        while True:
            command = input('\nClient Input: ')
            if command.lower().strip() == "exit":
                break
            client_socket.send(command.encode('utf-8'))
            if command.split()[0] == "set":
                command = input('Client Input: ')
                client_socket.send(command.encode('utf-8'))
            
            response = client_socket.recv(1024).decode('utf-8')
            print("Server Response:\n" + response)

        client_socket.close()
    else:
        print("Inappropriate arguments passed. (eg. python3 client.py <port_number> <server_ip_address>)")
