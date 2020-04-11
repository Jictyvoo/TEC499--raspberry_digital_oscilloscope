import RPi_emu.GPIO as GPIO
import time
import random #random is used to provide a random number as light level

class I2CTreatment:
    def __init__(self):
        self.__address = 0x70
        self.__smbus = GPIO.SMBus(1)
        random.seed()
        GPIO.add_autoreply(self.__address, 2, 5)
        GPIO.add_autoreply(self.__address, 3, 1)

    def write(self, value):
        self.__smbus.write_byte_data(self.__address, 0, value)
        #provide a random number to register 1 (light level)
        temporary = random.randrange(0, 255, 1)
        # print(temporary)
        GPIO.add_autoreply(self.__address, 1, temporary)
        return -1

    def lightlevel(self):
        light = self.__smbus.read_byte_data(self.__address, 1)
        return light

    def range(self):
        range_1 = self.__smbus.read_byte_data(self.__address, 2)
        range_2 = self.__smbus.read_byte_data(self.__address, 3)
        range_3 = (range_1 << 8) + range_2
        return range_3
