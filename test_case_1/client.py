import socket
import sys

if __name__ == '__main__':
    """
    Test case - 01:
    Check basic functionality by connecting two clients, you explicitly have to open two terminals and have to run this code.
    """
    if len(sys.argv) == 2:
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
            elif command.split()[0] == "get":
                final_response = ""
                response1 = client_socket.recv(1024).decode('utf-8')
                if response1.strip() == "END":
                    final_response = response1
                else:
                    final_response = response1
                    response2 = client_socket.recv(int(response1.split(" ")[2].strip())).decode('utf-8')
                    final_response += response2

                print("Server Response:\n" + final_response)

        client_socket.close()
    else:
        print("Inappropriate arguments passed. (eg. python3 client.py <port_number>)")
