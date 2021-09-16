import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

fig = plt.figure()
ax = plt.axes()

bluetooth = open('ble_data.txt', 'r')
Lines = bluetooth.readlines()

count = 0

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

time_ble = 0
for line in Lines:
    if line == "\n":
        time_ble += 1

num_ble = [0] * (time_ble+1)

for line in Lines:
    num_ble[count] += 1
    if line == "\n":
        count += 1
        
num = len(num_ble)

plt.plot(num_ble)
plt.title('Bluetooth Devices across Scans')
plt.xlabel('Scan Iteration')
plt.ylabel('Number of Bluetooth Devices')
plt.show()
"""

for x in range(num):
    print(num_ble[x])


    count += 1
    print("Line{}: {}".format(count, line.strip()))


    
"""
