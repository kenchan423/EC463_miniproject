
"""
Example of scanning Bluetooth Low Energy (BLE) devices.
Requires a Linux computer due to gattlib underlying BLE scanning requiring Glib.
Made some modifications to allow for writing to text file
"""

import argparse
from bluetooth.ble import DiscoveryService

p = argparse.ArgumentParser(description="BLE scanner")
p.add_argument(
    "timeout",
    help="number of seconds to scan for BLE devices",
    nargs="?",
    type=int,
    default=5,
)
P = p.parse_args()

timeout = P.timeout

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
