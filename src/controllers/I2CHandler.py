from models.I2CTreatment import I2CTreatment
import threading
import time


class I2CHandler(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.__i2c = I2CTreatment()
        self.__voltages = ([], [])
        self.__indexes = [0, 0]
        self.__max_index = 40

    def __update_voltage(self, channel=0, value=5):
        self.__voltages[channel].append(value)
        if len(self.__voltages[channel]) >= self.__max_index:
            self.__voltages[channel].remove(self.__voltages[channel][0])

    def _update_voltage_list(self):
        self.__i2c.write(0x51)
        time.sleep(0.5)
        channel_1 = self.__i2c.getVoltage()
        self.__update_voltage(0, channel_1)
        self.__i2c.write(0x51)
        # time.sleep(0.7)
        channel_2 = self.__i2c.getVoltage()
        self.__update_voltage(1, channel_2)
        # print("channel_1", channel_1, "channel_2", channel_2)

    def get_voltage(self):
        return tuple(self.__voltages[0]), tuple(self.__voltages[1])

    def run(self):
        while True:
            self.__i2c.write(0x51)
            self._update_voltage_list()
            # rng = self.__i2c.range(); print("rng", rng)
