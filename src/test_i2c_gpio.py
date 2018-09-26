#!/usr/bin/env python
import smbus as smbus
import time
from TrdCrobI2C import TrdCrobI2C

#i2c = smbus.SMBus(1)
#i2c.write_byte_data(0x21,0x18,0x00)
#crob_i2c.test()
#while True:
#    i2c.write_byte_data(0x21,0x08,0x01)
#    time.sleep(0.5)
#    i2c.write_byte_data(0x21,0x08,0x02)
#    time.sleep(0.5)
#    i2c.write_byte_data(0x21,0x08,0x04)
#    time.sleep(0.5)
#    i2c.write_byte_data(0x21,0x08,0x08)
#    time.sleep(0.5)
#ReadData = MyBus.read_byte_data(0x6b,0x05)
#print ReadData

i2c = TrdCrobI2C(20, 1, 0x21)

