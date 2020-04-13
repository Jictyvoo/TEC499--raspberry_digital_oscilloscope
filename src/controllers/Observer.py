from PyQt5 import QtCore


class EventHandler():
    def __init__(self, ui, oscilloscopeGraphic, i2cThread):
        self.__ui = ui
        self.__i2cThread = i2cThread
        self.__oscilloscopeGraphic = oscilloscopeGraphic
        # Add callback to checkbox event
        self.__ui.channel_1_checkbox.stateChanged.connect(
            lambda: self.checkbox_state_changed(1))
        self.__ui.channel_2_checkbox.stateChanged.connect(
            lambda: self.checkbox_state_changed(2))
        # Add callback to slider event
        self.__ui.channel_1_vertical_scale.valueChanged.connect(
            lambda: self.__scale_change(self.__ui.channel_1_vertical_scale, False, 0))
        self.__ui.channel_1_horizontal_scale.valueChanged.connect(
            lambda: self.__scale_change(self.__ui.channel_1_horizontal_scale, True, 0))
        self.__ui.channel_2_vertical_scale.valueChanged.connect(
            lambda: self.__scale_change(self.__ui.channel_2_vertical_scale, False, 1))
        self.__ui.channel_2_horizontal_scale.valueChanged.connect(
            lambda: self.__scale_change(self.__ui.channel_2_horizontal_scale, True, 1))
        self.__timer = QtCore.QTimer()
        self.__timer.timeout.connect(self.update_values_draw)
        self.__timer.start(50)

    def __scale_change(self, slider, scale_type=False, channel=0):
        if scale_type:
            self.__oscilloscopeGraphic.setHorizontalScale(
                slider.value(), channel)
        else:
            self.__oscilloscopeGraphic.setVerticalScale(
                slider.value(), channel)

    def update_values_draw(self):
        channel_1, channel_2 = self.__i2cThread.get_voltage()
        self.__oscilloscopeGraphic.drawChannelsCurves(channel_1, channel_2)

    def checkbox_state_changed(self, channel_checkbox=1):
        if channel_checkbox == 1:
            if self.__ui.channel_1_checkbox.isChecked():
                self.__oscilloscopeGraphic.setChannelVisible(
                    0, True)  # print("Checked 1")
            else:
                self.__oscilloscopeGraphic.setChannelVisible(
                    0, False)  # print("Unchecked 1")
        elif channel_checkbox == 2:
            if self.__ui.channel_2_checkbox.isChecked():
                self.__oscilloscopeGraphic.setChannelVisible(
                    1, True)  # print("Checked 2")
            else:
                self.__oscilloscopeGraphic.setChannelVisible(
                    1, False)  # print("Unchecked 2")

    def run(self):
        self.__i2cThread.start()
