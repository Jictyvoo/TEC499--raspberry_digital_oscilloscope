from PyQt5 import QtWidgets, QtGui, QtCore


class OscilloscopeGraphic:
    def __init__(self, graphicsView, scene):
        self.__graphicsView = graphicsView
        self.__scene = scene
        self.__pens = (
            QtGui.QPen(QtGui.QColor(156, 234, 157)),
            QtGui.QPen(QtGui.QColor(234, 228, 156))
        )
        self.__paths = (
            QtGui.QPainterPath(),
            QtGui.QPainterPath()
        )
        self.__channels_settings = (
            {
                "scale": {"vertical": 0.6, "horizontal": 0.1},
                "visible": False
            },
            {
                "scale": {"vertical": 0.6, "horizontal": 0.1},
                "visible": False
            }
        )
        self.__screen_size = {
            "width": 0,
            "height": 0,
            "cellsize": 32
        }

    def setHorizontalScale(self, newScale=1, channel=0):
        settings = self.__channels_settings[channel]
        settings.get("scale").update({"horizontal": newScale / 10})

    def setVerticalScale(self, newScale=1, channel=0):
        settings = self.__channels_settings[channel]
        settings.get("scale").update({"vertical": newScale / 10})

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
        allLines = []
        horigin = int(rect.height() / -1)
        worigin = int(rect.width() / -1)
        self.__screen_size.update(
            {"width": rect.width(), "height": rect.height()})
        '''Drawing columns to right and to left'''
        for column in range(0, int(rect.height()), self.__screen_size.get("cellsize")):
            line = QtCore.QLineF(worigin, column, int(rect.width()), column)
            allLines.append(line)
        for column in range(0, horigin, self.__screen_size.get("cellsize") * -1):
            line = QtCore.QLineF(worigin, column, int(rect.width()), column)
            allLines.append(line)

        '''Drawing rows to up and to down'''
        for row in range(0, int(rect.width()), self.__screen_size.get("cellsize")):
            line = QtCore.QLineF(row, horigin, row, int(rect.height()))
            allLines.append(line)
        for row in range(0, worigin, self.__screen_size.get("cellsize") * -1):
            line = QtCore.QLineF(row, horigin, row, int(rect.height()))
            allLines.append(line)
        painter.drawLines(allLines)

        '''Drawing center lines'''
        pen.setWidth(5)
        painter.setPen(pen)
        line_1 = QtCore.QLineF(0, horigin, 0, int(rect.height()))
        line_2 = QtCore.QLineF(worigin, 0, int(rect.width()), 0)
        painter.drawLines([line_1, line_2])

    def __voltageValueToPoint(self, value=5, read_time=0, channel=0):
        total_height = self.__screen_size.get("height")
        temp_voltage = value - 2.5
        yPosition = (temp_voltage * total_height) / 2.5
        scale_x = self.__channels_settings[channel].get(
            "scale").get("horizontal")
        scale_y = self.__channels_settings[channel].get(
            "scale").get("vertical")
        return QtCore.QPointF(read_time * scale_x, yPosition * scale_y)

    def _drawSingleCurve(self, selected_pen=0, values=[]):
        self.__paths[selected_pen].clear()
        pen = self.__pens[selected_pen]
        pen.setWidth(3)
        path = self.__paths[selected_pen]
        path.moveTo(0, 0)
        previous_last_point = self.__voltageValueToPoint(
            values[0], 0, selected_pen)
        for counter in range(1, len(values), 2):
            if len(values) > counter + 1:
                read_time = counter * self.__screen_size.get("cellsize")
                voltage_1, voltage_2 = values[counter], values[counter + 1]
                control_point_1 = previous_last_point
                control_point_2 = self.__voltageValueToPoint(
                    voltage_1, read_time, selected_pen)
                read_time = (counter + 1) * self.__screen_size.get("cellsize")
                end_point = self.__voltageValueToPoint(
                    voltage_2, read_time, selected_pen)
                path.cubicTo(control_point_1, control_point_2, end_point)
                previous_last_point = end_point
        self.__scene.addPath(path, pen)

    def drawChannelsCurves(self, channel_1=[], channel_2=[]):
        self.__scene.clear()
        if self.__channels_settings[0].get("visible"):
            self._drawSingleCurve(0, channel_1)
        if self.__channels_settings[1].get("visible"):
            self._drawSingleCurve(1, channel_2)
