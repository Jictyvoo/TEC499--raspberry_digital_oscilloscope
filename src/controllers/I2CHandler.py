from models.I2CTreatment import I2CTreatment
import threading
import time


class I2CHandler(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.__i2c = I2CTreatment()

    def run(self):
        while True:
            self.__i2c.write(0x51)
            time.sleep(0.7)
            lightlvl = self.__i2c.getVoltage()
            rng = self.__i2c.range()
            print("Voltage", lightlvl)
            print("rng", rng)
