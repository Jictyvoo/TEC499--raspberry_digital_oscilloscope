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
        background_brush = QtGui.QBrush(QtGui.QColor(25, 25, 25), QtCore.Qt.SolidPattern)
        painter.fillRect(rect, background_brush)

        pen = QtGui.QPen(QtGui.QColor(255, 255, 255))
        pen.setWidth(2)
        painter.setPen(pen)
        cellsize = 32
        allLines = []
        horigin = int(rect.height() / -2)
        worigin = int(rect.width() / -2)
        for column in range(horigin, int(rect.height()), cellsize):
            line = QtCore.QLineF(horigin, column, int(rect.width()), column)
            allLines.append(line)
        for row in range(worigin, int(rect.width()), cellsize):
            line = QtCore.QLineF(row, worigin, row, int(rect.height()))
            allLines.append(line)

        painter.drawLines(allLines)

    '''def draw_grid(self):
        side = 20
        pen = QtGui.QPen(QtCore.Qt.black)
        for i in range(16):
            for j in range(16):
                rectangle = QtCore.QRectF(QtCore.QPointF(i*side, j*side), QtCore.QSizeF(side, side))
                self.__scene.addRect(rectangle, pen)'''
