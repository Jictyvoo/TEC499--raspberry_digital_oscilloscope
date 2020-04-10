import threading

class EventHandler(threading.Thread):
    def __init__(self, ui, oscilloscopeGraphic, i2cThread):
        threading.Thread.__init__(self)

        self.__ui = ui
        self.__i2cThread = i2cThread
        self.__oscilloscopeGraphic = oscilloscopeGraphic

    def run(self):
        self.__i2cThread.start()
        while True:
            # self.__oscilloscopeGraphic.draw_grid()
            break
