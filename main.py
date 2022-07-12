#!/usr/bin/env python3
import sys, sqlite3, time
from datetime import datetime
import bluetooth._bluetooth as bluez
import unicornhat as uh

from py_bluetooth_utils.bluetooth_utils import (toggle_device, enable_le_scan,
                             parse_le_advertising_events,
                             disable_le_scan, raw_packet_to_str)
 

# Use 0 for hci0
dev_id = 0
toggle_device(dev_id, True)
uh.set_layout(uh.PHAT)
uh.brightness(0.5)

sampleFreq = 0.5 # time in seconds

 
try:
    sock = bluez.hci_open_dev(dev_id)
except:
    print("Cannot open bluetooth device %i" % dev_id)
    raise

# Set filter to "True" to see only one packet per device
enable_le_scan(sock, filter_duplicates=False)
 
try:

    def setColor(temp):
        if temp <= 10:
            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 0, 221, 255)
            uh.show()

        elif temp <= 15:
            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 0, 140, 255)
            uh.show()

        elif temp <= 20:
            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 240, 201, 26)
            uh.show()
        
        elif temp <= 25:
            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 242, 138, 27)
            uh.show()

        elif temp <= 30:
            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 242, 120, 27)
            uh.show()

        elif temp <= 35:
            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 242, 99, 27)
            uh.show()

        elif temp <= 40:
            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 242, 77, 27)
            uh.show()

        elif temp <= 45:
            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 242, 70, 27)
            uh.show()

        elif temp <= 50:
            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 242, 38, 27)
            uh.show()


    def le_advertise_packet_handler(mac, adv_type, data, rssi):
        global temp
        data_str = raw_packet_to_str(data)
        # Check for ATC preamble
        if data_str[6:10] == '1a18':
            temp = int(data_str[22:26], 16) / 10
            if mac == "A4:C1:38:19:B4:32":
                name = "In Portacom"
                #print(name, temp, hum, batt)
                print("%s - Device: %s Temp: %sc" % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name, temp))
                uh.clear()
                setColor(temp)
        
        time.sleep(sampleFreq)


    

 
    # Called on new LE packet
    parse_le_advertising_events(sock, handler=le_advertise_packet_handler, debug=False)

# Scan until Ctrl-C
except KeyboardInterrupt:
    disable_le_scan(sock)
