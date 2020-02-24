#!/usr/bin/env python3

import csv
import jinja2
import time
from netmiko import Netmiko

csv_file = 'net3.csv'
jinja_template = 'net3.j2'

inventory = {}
inv_list = []

with open(csv_file) as f:
    read_csv = csv.DictReader(f)
    for vals in read_csv:

        inventory['device'] = vals['Device']
        inventory['ip'] = vals['IP Address']
        inventory['username'] = vals['Username']
        inventory['password'] = vals['Password']
        inventory['port'] = vals['Port']
        inventory['gigabitethernet10'] = vals['GigabitEthernet1/0']
        inventory['g10_netmask'] = vals['G1/0 Netmask']
        inventory['gigabitethernet20'] = vals['GigabitEthernet2/0']
        inventory['g20_netmask'] = vals['G2/0 Netmask']
        inventory['device_type'] = vals['Device type']

        inv_list.append(inventory.copy())

for items in inv_list:
    print('\nCurrent device: ' + items['device'])

    with open(jinja_template) as f:
        tfile = f.read()
    template = jinja2.Template(tfile)
    cfg_list = template.render(items).split('\n')  

    conn = Netmiko(host=items['ip'], device_type=items['device_type'], username=items['username'],password=items['password'],port=items['port'])

    conn.write_channel("\n")
    time.sleep(1)
    output = conn.read_channel()
    if 'initial configuration dialog' in output:
        conn.write_channel('no\n')
        time.sleep(1)

    output = conn.enable()
    output = conn.send_config_set(cfg_list)

    print(output)

    conn.disconnect()