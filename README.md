# Network Automation & Programmibility 
Network Programmibility &amp; Automation Labs with Python3, Jinja2, CSV File, Cisco, &amp; Netmiko

> The code in this repository is a modification of [Jedadiah Casey](https://neckercube.com/posts/2018-04-19-automating-labs-with-python-jinja2-and-netmiko/).

## Hands On Lab
This demo use Ubuntu 18.04 for Python & GNS3 for Dynampis Cisco Router 

## Video Demo
Video demo : https://www.youtube.com/watch?v=1Nhvj5D8pmg

## Setting Up the Ubuntu Machine
1. Clone the code repo

    ```bash
    git clone https://github.com/assyafii/python_networking.git
    cd python_networking
    ```

2. Setup Python & Install Requirements  

    ```bash
    sudo apt update && sudo apt install python3 python3-pip
    pip3 install -r requirements.txt
    ```


## Cisco Router Configuration
This configuration below is used so that the router can be accessed using the ssh protocol by ubuntu machine (python) and this demo network runs on [Cisco Router Series 7200]().  

1. Router Command Configuration on Router 1  & Router 2

    ```bash
    #Router 1
    R1enable
    R1conf t
    R1(config)username r1admin privilege 15 password 12345
    R1(config)ip domain name example.com
    R1(config)crypto key generate rsa modulus 1024
    R1(config)line vty 0 4
    R1(config-line)transport input SSH
    R1(config-line)login local
    R1(config-line)exit
    R1(config)interface fa0/0
    R1(config-if)ip add
    R1(config-if)ip address 10.10.10.10 255.255.255.0
    R1(config-if)no sh
    R1(config-if)exit
    R1(config)exit
    R1sh ip ssh
    R1copy run start


    #Router2
    R2enable
    R2conf t
    R2(config)username admin privilege 15 password admin
    R2(config)ip domain name example.com
    R2(config)crypto key generate rsa modulus 1024
    R2(config)line vty 0 4
    R2(config-line)transport input SSH
    R2(config-line)login local
    R2(config-line)exit
    R2(config)interface fa0/0
    R2(config-if)ip add
    R2(config-if)ip address 10.10.10.20 255.255.255.0
    R2(config-if)no sh
    R2(config-if)exit
    R2(config)exit
    R2sh ip ssh
    R2copy run start
    ```
     * *Note: make sure **Ubuntu and cisco** access are **connected** via ssh and can **ping** the router's IP address


## Running Code
make sure **Ubuntu and cisco** access are **connected** using SSH and can **ping** the router's IP address

1. Running Code

    ```bash
    python3 net3.py
    ```

