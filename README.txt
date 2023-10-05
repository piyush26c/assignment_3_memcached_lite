Name: Piyush Rajendra Chaudhari
EmailID: piyrchau@iu.edu

File Structure
~/assignment_1_memcached_lite$ 
.
├── server.py
├── test_case_1
│   └── client.py
├── test_case_2
│   ├── client.py
│   ├── key_value.json
│   └── server.py
├── test_case_3
│   ├── client.py
│   ├── inputs.txt
│   ├── key_value.json
│   └── server.py
├── test_case_4
│   ├── client.py
│   ├── inputs.txt
│   ├── key_value.json
│   └── server.py
└── test_case_5
    ├── client.py
    ├── key_value.json
    └── server.py

5 directories, 16 files



Note: If on particular port number, server seems to be busy. Use following command to free that port.
$npx kill-port <port-no>

Folling are the command to execute testcases.

I have made few changes (introducing sleep etc.) in server / client code, thus, I thought it would be good idea to include those specific
files in particular test case folder.

Note: At start you should be in root directory (here root directory is ~/assignment_1_memcached_lite)

------------------------------------------------------------------
For test-case-01:
To execute server:
$ python3 server.py 5000 5 "key_value.json" 1024

To execute client-1:
Open new terminal, get directory to root.
$ cd test_case_1
$ python3 client.py 5000

To execute client-2:
Open new terminal, get directory to root.
$ cd test_case_1
$ python3 client.py 5000

------------------------------------------------------------------
------------------------------------------------------------------
For test-case-02:
To execute server:
$ cd test_case_2
$ python3 server.py 5000 5 "key_value.json" 1024

To execute client-1:
Open new terminal, get directory to root.
$ cd test_case_2
$ python3 client.py 5000

To execute client-2:
Open new terminal, get directory to root.
$ cd test_case_2
$ python3 client.py 5000

------------------------------------------------------------------
------------------------------------------------------------------
For test-case-03:
To execute server:
$ cd test_case_3
$ python3 server.py 5000 5 "key_value.json" 9000

To execute client-1:
Open new terminal, get directory to root.
$ cd test_case_3
$ python3 client.py 5000

------------------------------------------------------------------
------------------------------------------------------------------
For test-case-04:
To execute server:
$ cd test_case_4
$ python3 server.py 5000 5 "key_value.json" 9000

To execute client-1:
Open new terminal, get directory to root.
$ cd test_case_4
$ python3 client.py 5000

------------------------------------------------------------------
------------------------------------------------------------------
For test-case-05:
To execute server:
$ cd test_case_5
$ python3 server.py 5000 5 "key_value.json" 9000

To execute client-1:
Open new terminal, get directory to root.
$ cd test_case_5
$ python3 client.py 5000 500

------------------------------------------------------------------