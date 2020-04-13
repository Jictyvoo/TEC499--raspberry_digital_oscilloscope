# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_frame.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RaspDigitalOscilloscope(object):
    def setupUi(self, RaspDigitalOscilloscope):
        RaspDigitalOscilloscope.setObjectName("RaspDigitalOscilloscope")
        RaspDigitalOscilloscope.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(RaspDigitalOscilloscope)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.canvas_hlayout = QtWidgets.QHBoxLayout()
        self.canvas_hlayout.setObjectName("canvas_hlayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setObjectName("graphicsView")
        self.canvas_hlayout.addWidget(self.graphicsView)
        self.verticalLayout_3.addLayout(self.canvas_hlayout)
        self.commands_hlayout = QtWidgets.QHBoxLayout()
        self.commands_hlayout.setObjectName("commands_hlayout")
        self.channels_config_vlayout = QtWidgets.QVBoxLayout()
        self.channels_config_vlayout.setObjectName("channels_config_vlayout")
        self.channel_scales_hlayout = QtWidgets.QHBoxLayout()
        self.channel_scales_hlayout.setObjectName("channel_scales_hlayout")
        self.channel_1_scales_vlayout = QtWidgets.QVBoxLayout()
        self.channel_1_scales_vlayout.setObjectName("channel_1_scales_vlayout")
        self.channel_1_label = QtWidgets.QLabel(self.frame)
        self.channel_1_label.setObjectName("channel_1_label")
        self.channel_1_scales_vlayout.addWidget(self.channel_1_label)
        self.channel_1_vscale_hlayout = QtWidgets.QHBoxLayout()
        self.channel_1_vscale_hlayout.setObjectName("channel_1_vscale_hlayout")
        self.channel_1_vscale_label = QtWidgets.QLabel(self.frame)
        self.channel_1_vscale_label.setObjectName("channel_1_vscale_label")
        self.channel_1_vscale_hlayout.addWidget(self.channel_1_vscale_label)
        self.channel_1_vertical_scale = QtWidgets.QSlider(self.frame)
        self.channel_1_vertical_scale.setMinimum(6)
        self.channel_1_vertical_scale.setMaximum(10)
        self.channel_1_vertical_scale.setOrientation(QtCore.Qt.Horizontal)
        self.channel_1_vertical_scale.setObjectName("channel_1_vertical_scale")
        self.channel_1_vscale_hlayout.addWidget(self.channel_1_vertical_scale)
        self.channel_1_scales_vlayout.addLayout(self.channel_1_vscale_hlayout)
        self.channel_1_hscale_hlayout = QtWidgets.QHBoxLayout()
        self.channel_1_hscale_hlayout.setObjectName("channel_1_hscale_hlayout")
        self.channel_1_hscale_label = QtWidgets.QLabel(self.frame)
        self.channel_1_hscale_label.setObjectName("channel_1_hscale_label")
        self.channel_1_hscale_hlayout.addWidget(self.channel_1_hscale_label)
        self.channel_1_horizontal_scale = QtWidgets.QSlider(self.frame)
        self.channel_1_horizontal_scale.setMinimum(1)
        self.channel_1_horizontal_scale.setMaximum(10)
        self.channel_1_horizontal_scale.setOrientation(QtCore.Qt.Horizontal)
        self.channel_1_horizontal_scale.setObjectName("channel_1_horizontal_scale")
        self.channel_1_hscale_hlayout.addWidget(self.channel_1_horizontal_scale)
        self.channel_1_scales_vlayout.addLayout(self.channel_1_hscale_hlayout)
        self.channel_scales_hlayout.addLayout(self.channel_1_scales_vlayout)
        self.channel_2_scales_vlayout = QtWidgets.QVBoxLayout()
        self.channel_2_scales_vlayout.setObjectName("channel_2_scales_vlayout")
        self.channel_2_label = QtWidgets.QLabel(self.frame)
        self.channel_2_label.setObjectName("channel_2_label")
        self.channel_2_scales_vlayout.addWidget(self.channel_2_label)
        self.channel_2_vscale_hlayout = QtWidgets.QHBoxLayout()
        self.channel_2_vscale_hlayout.setObjectName("channel_2_vscale_hlayout")
        self.channel_2_vscale_label = QtWidgets.QLabel(self.frame)
        self.channel_2_vscale_label.setObjectName("channel_2_vscale_label")
        self.channel_2_vscale_hlayout.addWidget(self.channel_2_vscale_label)
        self.channel_2_vertical_scale = QtWidgets.QSlider(self.frame)
        self.channel_2_vertical_scale.setMinimum(6)
        self.channel_2_vertical_scale.setMaximum(10)
        self.channel_2_vertical_scale.setOrientation(QtCore.Qt.Horizontal)
        self.channel_2_vertical_scale.setObjectName("channel_2_vertical_scale")
        self.channel_2_vscale_hlayout.addWidget(self.channel_2_vertical_scale)
        self.channel_2_scales_vlayout.addLayout(self.channel_2_vscale_hlayout)
        self.channel_2_hscale_hlayout = QtWidgets.QHBoxLayout()
        self.channel_2_hscale_hlayout.setObjectName("channel_2_hscale_hlayout")
        self.channel_2_hscale_label = QtWidgets.QLabel(self.frame)
        self.channel_2_hscale_label.setObjectName("channel_2_hscale_label")
        self.channel_2_hscale_hlayout.addWidget(self.channel_2_hscale_label)
        self.channel_2_horizontal_scale = QtWidgets.QSlider(self.frame)
        self.channel_2_horizontal_scale.setMinimum(1)
        self.channel_2_horizontal_scale.setMaximum(10)
        self.channel_2_horizontal_scale.setOrientation(QtCore.Qt.Horizontal)
        self.channel_2_horizontal_scale.setObjectName("channel_2_horizontal_scale")
        self.channel_2_hscale_hlayout.addWidget(self.channel_2_horizontal_scale)
        self.channel_2_scales_vlayout.addLayout(self.channel_2_hscale_hlayout)
        self.channel_scales_hlayout.addLayout(self.channel_2_scales_vlayout)
        self.channels_config_vlayout.addLayout(self.channel_scales_hlayout)
        self.channels_checkbox_hlayout = QtWidgets.QHBoxLayout()
        self.channels_checkbox_hlayout.setObjectName("channels_checkbox_hlayout")
        self.channel_1_checkbox = QtWidgets.QCheckBox(self.frame)
        self.channel_1_checkbox.setObjectName("channel_1_checkbox")
        self.channels_checkbox_hlayout.addWidget(self.channel_1_checkbox)
        self.channel_2_checkbox = QtWidgets.QCheckBox(self.frame)
        self.channel_2_checkbox.setObjectName("channel_2_checkbox")
        self.channels_checkbox_hlayout.addWidget(self.channel_2_checkbox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.synchronization_delay_label = QtWidgets.QLabel(self.frame)
        self.synchronization_delay_label.setObjectName("synchronization_delay_label")
        self.horizontalLayout.addWidget(self.synchronization_delay_label)
        self.synchronization_delay_input = QtWidgets.QDoubleSpinBox(self.frame)
        self.synchronization_delay_input.setPrefix("")
        self.synchronization_delay_input.setMaximum(2.0)
        self.synchronization_delay_input.setSingleStep(0.01)
        self.synchronization_delay_input.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.synchronization_delay_input.setProperty("value", 0.5)
        self.synchronization_delay_input.setObjectName("synchronization_delay_input")
        self.horizontalLayout.addWidget(self.synchronization_delay_input)
        self.channels_checkbox_hlayout.addLayout(self.horizontalLayout)
        self.channels_config_vlayout.addLayout(self.channels_checkbox_hlayout)
        self.commands_hlayout.addLayout(self.channels_config_vlayout)
        self.verticalLayout_3.addLayout(self.commands_hlayout)
        self.verticalLayout.addWidget(self.frame)
        RaspDigitalOscilloscope.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RaspDigitalOscilloscope)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        RaspDigitalOscilloscope.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RaspDigitalOscilloscope)
        self.statusbar.setObjectName("statusbar")
        RaspDigitalOscilloscope.setStatusBar(self.statusbar)

        self.retranslateUi(RaspDigitalOscilloscope)
        QtCore.QMetaObject.connectSlotsByName(RaspDigitalOscilloscope)

    def retranslateUi(self, RaspDigitalOscilloscope):
        _translate = QtCore.QCoreApplication.translate
        RaspDigitalOscilloscope.setWindowTitle(_translate("RaspDigitalOscilloscope", "RaspDigitalOscilloscope"))
        self.channel_1_label.setText(_translate("RaspDigitalOscilloscope", "Channel 1"))
        self.channel_1_vscale_label.setText(_translate("RaspDigitalOscilloscope", "Vertical Scale(V/div)"))
        self.channel_1_hscale_label.setText(_translate("RaspDigitalOscilloscope", "Horizontal Scale(s/div)"))
        self.channel_2_label.setText(_translate("RaspDigitalOscilloscope", "Channel 2"))
        self.channel_2_vscale_label.setText(_translate("RaspDigitalOscilloscope", "Vertical Scale(V/div)"))
        self.channel_2_hscale_label.setText(_translate("RaspDigitalOscilloscope", "Horizontal Scale(s/div)"))
        self.channel_1_checkbox.setText(_translate("RaspDigitalOscilloscope", "Channel 1 - Green"))
        self.channel_2_checkbox.setText(_translate("RaspDigitalOscilloscope", "Channel 2 - Yellow"))
        self.synchronization_delay_label.setText(_translate("RaspDigitalOscilloscope", "Synchronization Delay"))
        self.synchronization_delay_input.setSuffix(_translate("RaspDigitalOscilloscope", "s"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RaspDigitalOscilloscope = QtWidgets.QMainWindow()
    ui = Ui_RaspDigitalOscilloscope()
    ui.setupUi(RaspDigitalOscilloscope)
    RaspDigitalOscilloscope.show()
    sys.exit(app.exec_())
