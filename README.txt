Name: Piyush Rajendra Chaudhari
EmailID: piyrchau@iu.edu

File Structure
~/assignment_3_memcached_lite$ 
.
├── gcstorage_poc.py
├── install_requirements.sh
├── performance_testing
│   ├── client_get_read_latency.py
│   ├── client_set_write_latency.py
│   ├── data_generator.py
│   ├── google_key_value_store_lite_read_latency.png
│   ├── google_key_value_store_lite_write_latency.png
│   ├── memcached_lite_read_latency.png
│   ├── memcached_lite_write_latency.png
│   └── performance_graph.ipynb
├── piyush-chaudhari-fall2023-9600b4eeb5b1.json
├── README.txt
├── requirements.txt
├── server_gcs.py
├── server.py
├── setup_environment.py
├── test_case_1
│   └── client.py
├── test_case_2
│   ├── client.py
│   ├── inputs.txt
│   └── key_value.json
├── test_case_3
│   ├── client.py
│   ├── inputs.txt
│   └── key_value.json
└── test_case_4
    └── client.py

5 directories, 24 files



Note: If on particular port number, server seems to be busy. Use following command to free that port.
$npx kill-port <port-no>

Important: At first sight before I created any VMs, I executed following commands that setup firewall rules

gcloud compute networks create default

gcloud compute firewall-rules create default-allow --network default --allow tcp,udp,icmp --source-ranges 0.0.0.0/0