import threading

class EventHandler(threading.Thread):
    def __init__(self, ui, oscilloscopeGraphic, i2cThread):
        threading.Thread.__init__(self)

        self.__ui = ui
        self.__i2cThread = i2cThread
        self.__oscilloscopeGraphic = oscilloscopeGraphic
        self.__ui.channel_1_checkbox.stateChanged.connect(lambda: self.checkbox_state_changed(1))
        self.__ui.channel_2_checkbox.stateChanged.connect(lambda: self.checkbox_state_changed(2))

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
