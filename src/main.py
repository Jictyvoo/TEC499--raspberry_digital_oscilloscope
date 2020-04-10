from PyQt5 import QtWidgets
from view.main_window import Ui_RaspDigitalOscilloscope
import sys

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_RaspDigitalOscilloscope()
        self.ui.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
