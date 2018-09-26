
import smbus as smbus
import time

class TrdCrobI2C(object):

    def __init__(self, spadic_version=20, i2c_bus=0, i2c_addr=0):
        '''
        SPADIC Version

        -----------------  SPADIC 2.0 ----------------------
        
                            FEB 1
        RESET
                  KEL40  Sch. net name     Bank   Direction
        Spadic 0   27     PWR_EN_1         IO0_7  Out
        Spadic 1   28     PWR_EN_4         IO0_4  Out
        Spadic 2   26     PWR_EN_3         IO0_5  Out
        Spadic 3   25     PWR_EN_2         IO0_6  Out

        POWERGOOD 
                  KEL40  Sch. net name     Bank   Direction
        Spadic 0   31     RES_N_SPADIC_1   I0O_3  In
        Spadic 1   32     RES_N_SPADIC_3   I0O_1  In
        Spadic 2   30     RES_N_SPADIC_4   IO0_0  In
        Spadic 3   29     RES_N_SPADIC_2   IO0_2  In

                            FEB 2
        RESET
                  KEL40  Sch. net name     Bank   Direction
        Spadic 0   27     PWR_EN_1         IO0_7  Out
        Spadic 1   28     PWR_EN_4         IO0_4  Out
        Spadic 2   26     PWR_EN_3         IO0_5  Out
        Spadic 3   25     PWR_EN_2         IO0_6  Out

        POWERGOOD 
                  KEL40  Sch. net name     Bank   Direction
        Spadic 0   31     RES_N_SPADIC_1   I0O_3  In
        Spadic 1   32     RES_N_SPADIC_3   I0O_1  In
        Spadic 2   30     RES_N_SPADIC_4   IO0_0  In
        Spadic 3   29     RES_N_SPADIC_2   IO0_2  In
        '''
        
        # Initiliaze the I2C on the given bus
        self.i2c = smbus.SMBus(i2c_bus)
        self.i2c_addr = i2c_addr
        self.i2c_bus = i2c_bus
        self.io0_write_reg = 0x8
        self.io1_write_reg = 0x9
        self.io2_write_reg = 0xa
        self.io3_write_reg = 0xb
        self.io4_write_reg = 0xc
        # Configure the Input output ports
        # FEB 1
        self.i2c.write_byte_data(0x21,0x18,0xf0)
        # Set in reset state the SPADICs
        # FEB 1
        self.i2c.write_byte_data(self.i2c_addr, self.io0_write_reg, 0x00)
        self.i2c.write_byte_data(self.i2c_addr, self.io1_write_reg, 0x00)
        self.i2c.write_byte_data(self.i2c_addr, self.io2_write_reg, 0x00)
        self.i2c.write_byte_data(self.i2c_addr, self.io3_write_reg, 0x00)
        self.i2c.write_byte_data(self.i2c_addr, self.io4_write_reg, 0x00)
        
            
        def test():
            while True:
                i2c.write_byte_data(self.i2c_addr,0x08,0x01)
                time.sleep(0.5)
                i2c.write_byte_data(self.i2c_addr,0x08,0x02)
                time.sleep(0.5)
                i2c.write_byte_data(self.i2c_addr,0x08,0x04)
                time.sleep(0.5)
                i2c.write_byte_data(self.i2c_addr,0x08,0x08)
                time.sleep(0.5)
