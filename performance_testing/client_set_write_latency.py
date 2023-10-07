import socket
import sys
import time

if __name__ == '__main__':
    """
    Performance Test case - 01:
    Clocking in the time required for get and set using Google Cloud Storage service for files (having 1, 10, 100, 1000, 10000, 100000 number of key-value pairs)
    Also, the key and value sizes are in range(min_key/value_size, max_key/value_size)
    
    THIS CLIENT CODE CLOCKS SET (WRITE) TIMINGS.
    """
    if len(sys.argv) == 3:
        host_name = str(sys.argv[2])
        port = int(sys.argv[1])
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host_name, port))
        time1 = time2 = 0
        while True:
            command = input('\nClient Input: ')
            if command.lower().strip() == "exit":
                break
            client_socket.send(command.encode('utf-8'))
            if command.split()[0] == "set":
                command = input('Client Input: ')
                time1 = time.time()
                client_socket.send(command.encode('utf-8'))
            
            response = client_socket.recv(9000).decode('utf-8')
            time2 = time.time()
            print("Server Response:\n" + response)
            print("WRITE LATENCY (SET command):", time2 - time1)
        client_socket.close()
    else:
        print("Inappropriate arguments passed. (eg. python3 client.py <port_number> <server_ip_address>)")
