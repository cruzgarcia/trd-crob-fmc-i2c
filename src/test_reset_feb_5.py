#!/usr/bin/env python
import smbus as smbus
import time
from TrdCrobI2C import TrdCrobI2C

i2c = smbus.SMBus(1)
ADDR = 0x22

i2c.write_byte_data(ADDR,0x1a,0xf0)

i2c.write_byte_data(ADDR,0xa,0xf)
time.sleep(1)
i2c.write_byte_data(ADDR,0xa,0x0)
time.sleep(0.5)
i2c.write_byte_data(ADDR,0xa,0xf)

print "PowerGood status: 0x%x" % i2c.read_byte_data(ADDR, 0x2)

exit(1)
