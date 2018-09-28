#!/usr/bin/env python
import smbus as smbus
import time
from TrdCrobI2C import TrdCrobI2C

i2c = smbus.SMBus(1)
i2c.write_byte_data(0x21,0x18,0x00)
#crob_i2c.test()

#while True:
i2c.write_byte_data(0x21,0x08,0xf0)
time.sleep(0.5)
i2c.write_byte_data(0x21,0x08,0x00)
time.sleep(0.5)
i2c.write_byte_data(0x21,0x08,0xf0)
exit(1)
