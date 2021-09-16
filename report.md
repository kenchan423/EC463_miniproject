Following the miniproject github, we were able to set up our Raspberry Pi and run the bluetooth and wifi scripts successfully. 
We followed the instructions laid out in the miniproject github. While there was a little struggle with running wifi_scan.py, we successfully ran the scan after installing the proper module. After running wifi_scan.py for 15 minutes by setting the number of loops argument to a very large number (i.e., run python3 wifi_scan.py ~/ N 10000000), we saved the following data as a JSON file. In addition, we  logged the bluetooth scan onto a text file after editing ble_scan.py to store the printed scans. After obtaining data with the Raspberry Pi, we ran the wifi_plot.py script to plot the number of wifi devices over time. We also wrote a script to plot our bluetooth devices text file by examining the number of empty lines to see the number of devices in each scan iteration.

This is our wifi devices plotted over time.

![image](https://user-images.githubusercontent.com/55323049/133683114-b86bf0da-2cf2-4659-a2c7-9c53f4217fb3.png)

This is our bluetooth devices plotted over time.

![image](https://user-images.githubusercontent.com/55323049/133688468-50ad90ff-39d8-4817-a895-6651c7ac6f27.png)

