from PyQt5 import QtWidgets, QtGui, QtCore


class OscilloscopeGraphic:
    def __init__(self, graphicsView, scene):
        self.__graphicsView = graphicsView
        self.__scene = scene
        self.__pens = (
            QtGui.QPen(QtGui.QColor(156, 234, 157)),
            QtGui.QPen(QtGui.QColor(234, 228, 156))
        )
        self.__channels_settings = (
            {
                "scale": {"vertical": 1, "horizontal": 1},
                "visible": False
            },
            {
                "scale": {"vertical": 1, "horizontal": 1},
                "visible": False
            }
        )

    def setHorizontalScale(self, newScale=1, channel=0):
        settings = self.__channels_settings[channel]
        settings.get("scale").update({"horizontal": newScale})

    def setVerticalScale(self, newScale=1, channel=0):
        settings = self.__channels_settings[channel]
        settings.get("scale").update({"vertical": newScale})

    def setChannelVisible(self, channel=0, visible=True):
        self.__channels_settings[channel].update({"visible": visible})
        print(self.__channels_settings[channel])

    def drawBackground(self, painter, rect):
        background_brush = QtGui.QBrush(
            QtGui.QColor(40, 40, 40), QtCore.Qt.SolidPattern)
        painter.fillRect(rect, background_brush)

        pen = QtGui.QPen(QtGui.QColor(255, 255, 255))
        pen.setWidth(1)
        painter.setPen(pen)
        cellsize = 32
        allLines = []
        horigin = int(rect.height() / -2)
        worigin = int(rect.width() / -2)
        '''Drawing columns to right and to left'''
        for column in range(0, int(rect.height()), cellsize):
            line = QtCore.QLineF(worigin, column, int(rect.width()), column)
            allLines.append(line)
        for column in range(0, horigin, cellsize * -1):
            line = QtCore.QLineF(worigin, column, int(rect.width()), column)
            allLines.append(line)

        '''Drawing rows to up and to down'''
        for row in range(0, int(rect.width()), cellsize):
            line = QtCore.QLineF(row, horigin, row, int(rect.height()))
            allLines.append(line)
        for row in range(0, worigin, cellsize * -1):
            line = QtCore.QLineF(row, horigin, row, int(rect.height()))
            allLines.append(line)
        painter.drawLines(allLines)

        '''Drawing center lines'''
        pen.setWidth(5)
        painter.setPen(pen)
        line_1 = QtCore.QLineF(0, horigin, 0, int(rect.height()))
        line_2 = QtCore.QLineF(worigin, 0, int(rect.width()), 0)
        painter.drawLines([line_1, line_2])

    def __voltageValueToPoint(self, value=5):
        return QtGui.QPoint(0, 0)

    def _drawSingleCurve(self, selected_pen=QtGui.QPen(QtGui.QColor(255, 255, 255)), values=[]):
        selected_pen.setWidth(3)
        path = QtGui.QPainterPath()
        path.moveTo(0, 0)
        path.cubicTo(99, 0,  50, 50,  99, 99)
        path.cubicTo(0, 99,  50, 50,  0, 0)
        path.moveTo(0, 0)
        self.__scene.addPath(path, selected_pen)

    def drawChannelsCurves(self, channel_1=[], channel_2=[]):
        if self.__channels_settings[0].get("visible"):
            self._drawSingleCurve(self.__pens[0], channel_1)
        if self.__channels_settings[1].get("visible"):
            self._drawSingleCurve(self.__pens[1], channel_2)
