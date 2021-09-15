
#!/usr/bin/env python3
"""
Example of scanning Bluetooth Low Energy (BLE) devices.
Requires a Linux computer due to gattlib underlying BLE scanning requiring Glib.
Edited the file to make sure it wrote the data in a for loop
"""
from __future__ import annotations
import argparse
import pprint
import re
import logging
import subprocess
import argparse
import datetime
import json
import time
from pathlib import Path
from bluetooth.ble import DiscoveryService

p = argparse.ArgumentParser(description="BLE scanner")
p.add_argument(
    "timeout", help="number of seconds to scan for BLE devices", nargs="?", type=int, default=5
)
p.add_argument(
    'logpath', help="directory to write JSON output to", default="."
    )

P = p.parse_args()

timeout = P.timeout
logpath = P.logpath

print(f"Scanning BLE devices for {timeout} seconds")

file1 = open("ble_scan.txt", "w")

svc = DiscoveryService()
ble_devs = svc.discover(timeout)

for _ in range(5):
    
    for u, n in ble_devs.items():
    
        print(u, n)

        file1.write(u + n + "\n")
        
    file1.write("\n")

file1.close()
