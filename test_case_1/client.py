import socket
import sys

if __name__ == '__main__':
    """
    Test case - 01:
    Check basic functionality by connecting two clients, you explicitly have to open two terminals and have to run this code.
    """
    if len(sys.argv) == 2:
        # host_name = "34.134.39.121"
        host_name = socket.gethostname()
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
        print("Inappropriate arguments passed. (eg. python3 client.py <port_number>)")
