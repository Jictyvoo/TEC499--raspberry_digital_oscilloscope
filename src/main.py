from PyQt5 import QtWidgets
from view.OscilloscopeGraphic import OscilloscopeGraphic
from view.main_window import Ui_RaspDigitalOscilloscope
from controllers.I2CHandler import I2CHandler
from controllers.Observer import EventHandler
import sys


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_RaspDigitalOscilloscope()
        self.ui.setupUi(self)

        self.ui.channel_1_vertical_scale.setMinimum(1)
        self.ui.channel_1_vertical_scale.setMaximum(10)
        self.ui.channel_1_horizontal_scale.setMinimum(1)
        self.ui.channel_1_horizontal_scale.setMaximum(10)
        self.ui.channel_2_vertical_scale.setMinimum(1)
        self.ui.channel_2_vertical_scale.setMaximum(10)
        self.ui.channel_2_horizontal_scale.setMinimum(1)
        self.ui.channel_2_horizontal_scale.setMaximum(10)

        self.scene = QtWidgets.QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        self.oscilloscopeGraphic = OscilloscopeGraphic(
            self.ui.graphicsView, self.scene)
        self.ui.graphicsView.drawBackground = self.oscilloscopeGraphic.drawBackground


def execute_oscilloscope(app=QtWidgets.QApplication(sys.argv), application=ApplicationWindow()):
    # application.oscilloscopeGraphic.draw_grid()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    eventHandler = EventHandler(
        application.ui, application.oscilloscopeGraphic, I2CHandler())
    eventHandler.run()
    execute_oscilloscope(app, application)
