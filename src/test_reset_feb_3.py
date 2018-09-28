#!/usr/bin/env python
import smbus as smbus
import time
from TrdCrobI2C import TrdCrobI2C

i2c = smbus.SMBus(1)
ADDR = 0x21

# BANK 3
# 1 = i-put
# 0 = Output
# Reset lines from IO3-0 to IO3-3
REG_CONF_IO=0x1B
REG_WR=0xB
REG_RD=0x3
# Configure the bank
i2c.write_byte_data(ADDR,REG_CONF_IO,0xf0)
# Perform reset
i2c.write_byte_data(ADDR,REG_WR,0xf)
time.sleep(1)
i2c.write_byte_data(ADDR,REG_WR,0x0)
time.sleep(0.5)
i2c.write_byte_data(ADDR,REG_WR,0xf)

print "PowerGood status: 0x%x" % i2c.read_byte_data(ADDR, 0x3)

exit(1)
