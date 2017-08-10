#!/usr/bin/env python
import usb

dev = usb.core.find(idVendor=0x0416, idProduct=0x511c)
print(dev)
print("ahlo")
