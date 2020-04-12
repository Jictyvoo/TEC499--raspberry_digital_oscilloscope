from PyQt5 import QtWidgets, QtGui, QtCore


class OscilloscopeGraphic:
    def __init__(self, graphicsView, scene):
        self.__graphicsView = graphicsView
        self.__scene = scene
        self.__verticalScale = 1
        self.__horizontalScale = 1

    def setHorizontalScale(self, horizontalScale):
        self.__horizontalScale = horizontalScale

    def setVerticalScale(self, verticalScale):
        self.__verticalScale = verticalScale

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

    def drawChannelsCurves(self, channel_1=True, channel_2=False):
        print("draw")
