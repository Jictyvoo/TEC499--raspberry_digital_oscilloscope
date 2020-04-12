from PyQt5 import QtCore


class EventHandler():
    def __init__(self, ui, oscilloscopeGraphic, i2cThread):
        self.__ui = ui
        self.__i2cThread = i2cThread
        self.__oscilloscopeGraphic = oscilloscopeGraphic
        self.__ui.channel_1_checkbox.stateChanged.connect(
            lambda: self.checkbox_state_changed(1))
        self.__ui.channel_2_checkbox.stateChanged.connect(
            lambda: self.checkbox_state_changed(2))
        self.__timer = QtCore.QTimer()
        self.__timer.timeout.connect(self.update_values_draw)
        self.__timer.start(1000)

    def update_values_draw(self):
        channel_1, channel_2 = self.__i2cThread.get_voltage()
        self.__oscilloscopeGraphic.drawChannelsCurves(channel_1, channel_2)

    def checkbox_state_changed(self, channel_checkbox=1):
        if channel_checkbox == 1:
            if self.__ui.channel_1_checkbox.isChecked():
                print("Checked 1")
            else:
                print("Unchecked 1")
        elif channel_checkbox == 2:
            if self.__ui.channel_2_checkbox.isChecked():
                print("Checked 2")
            else:
                print("Unchecked 2")

    def run(self):
        self.__i2cThread.start()
        while True:
            # self.__oscilloscopeGraphic.draw_grid()
            break
