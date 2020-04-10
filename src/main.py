from PyQt5 import QtWidgets
from view.main_window import Ui_RaspDigitalOscilloscope
from models.I2CTreatment import I2CTreatment
import sys
import time

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_RaspDigitalOscilloscope()
        self.ui.setupUi(self)


def main():
    i2c = I2CTreatment()
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())
    print("Test")
    while True:
        i2c.write(0x51)
        time.sleep(0.7)
        lightlvl = i2c.lightlevel()
        rng = i2c.range()
        print(lightlvl)
        print(rng)

if __name__ == "__main__":
    main()
