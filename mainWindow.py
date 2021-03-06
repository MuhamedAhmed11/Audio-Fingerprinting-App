# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 821)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.showResult = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.showResult.setFont(font)
        self.showResult.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 255);\n"
"")
        self.showResult.setObjectName("showResult")
        self.gridLayout_8.addWidget(self.showResult, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1)
        self.browseButton = QtWidgets.QPushButton(self.tab)
        self.browseButton.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.browseButton.setFont(font)
        self.browseButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 255);\n"
"border-color: rgb(85, 85, 255);\n"
"gridline-color: rgb(85, 85, 255);\n"
"")
        self.browseButton.setObjectName("browseButton")
        self.gridLayout_7.addWidget(self.browseButton, 0, 1, 1, 1)
        self.soundRecogniserOuput = QtWidgets.QTextBrowser(self.tab)
        self.soundRecogniserOuput.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.soundRecogniserOuput.setStyleSheet("color: rgb(85, 85, 255);\n"
"border-color: rgb(85, 85, 255);")
        self.soundRecogniserOuput.setObjectName("soundRecogniserOuput")
        self.gridLayout_7.addWidget(self.soundRecogniserOuput, 1, 0, 2, 1)
        self.recordingButton = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recordingButton.setFont(font)
        self.recordingButton.setStyleSheet("background-color: rgb(255, 0, 4);\n"
"color: rgb(255, 255, 255);")
        self.recordingButton.setObjectName("recordingButton")
        self.gridLayout_7.addWidget(self.recordingButton, 1, 1, 1, 1)
        self.playButton = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.playButton.setObjectName("playButton")
        self.gridLayout_7.addWidget(self.playButton, 2, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.soundRecogniserOuput_2 = QtWidgets.QTableWidget(self.tab)
        self.soundRecogniserOuput_2.setObjectName("soundRecogniserOuput_2")
        self.soundRecogniserOuput_2.setColumnCount(0)
        self.soundRecogniserOuput_2.setRowCount(0)
        self.gridLayout_8.addWidget(self.soundRecogniserOuput_2, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.plottingGraph = PlotWidget(self.tab_3)
        self.plottingGraph.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.plottingGraph.setObjectName("plottingGraph")
        self.plottingGraph.hideAxis('bottom')
        self.plottingGraph.hideAxis('left')
        self.plottingGraph.setBackground('w')
        self.plottingGraph.setStyleSheet( "border:1px solid rgb(0, 0, 0);")
        self.gridLayout_4.addWidget(self.plottingGraph, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("color: rgb(85, 85, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_4.addWidget(self.comboBox, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.browseButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.browseButton_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.browseButton_2.setFont(font)
        self.browseButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 255);\n"
"border-color: rgb(85, 85, 255);\n"
"gridline-color: rgb(85, 85, 255);\n"
"")
        self.browseButton_2.setObjectName("browseButton_2")
        self.gridLayout_13.addWidget(self.browseButton_2, 0, 1, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.horizontalSlider_1 = QtWidgets.QSlider(self.tab_2)
        self.horizontalSlider_1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_1.setObjectName("horizontalSlider_1")
        self.horizontalSlider_1.setMaximum(100)
        self.gridLayout_11.addWidget(self.horizontalSlider_1, 1, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_13.setAlignment(QtCore.Qt.AlignRight)
        self.label_13.setObjectName("label_13")
        self.gridLayout_11.addWidget(self.label_13, 0, 1, 1, 1)
        self.songval = QtWidgets.QLabel(self.tab_2)
        self.songval.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.songval.setText("")
        self.songval.setObjectName("songval")
        self.gridLayout_11.addWidget(self.songval, 0, 2, 1, 1)
        # self.label_9 = QtWidgets.QLabel(self.tab_2)
        # self.label_9.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        # self.label_9.setObjectName("label_9")
        # self.gridLayout_11.addWidget(self.label_9, 0, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_11, 0, 0, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.spectogrambutton = QtWidgets.QPushButton(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.spectogrambutton.setFont(font)
        self.spectogrambutton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 255);\n"
"")
        self.spectogrambutton.setObjectName("spectogrambutton")
        self.gridLayout_10.addWidget(self.spectogrambutton, 2, 0, 1, 1)
        self.showResult_2 = QtWidgets.QPushButton(self.tab_2)
        
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.showResult_2.setFont(font)
        self.showResult_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 255);\n"
"")
        self.showResult_2.setObjectName("showResult_2")
        self.gridLayout_10.addWidget(self.showResult_2, 1, 0, 1, 1)
        self.soundRecogniserOuput_3 = QtWidgets.QTableWidget(self.tab)
        self.soundRecogniserOuput_3.setObjectName("soundRecogniserOuput_3")
        self.soundRecogniserOuput_3.setColumnCount(0)
        self.soundRecogniserOuput_3.setRowCount(0)
        self.gridLayout_10.addWidget(self.soundRecogniserOuput_3, 0, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_10, 4, 0, 1, 2)
        self.browseButton_3= QtWidgets.QPushButton(self.tab_2)
        self.browseButton_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.browseButton_3.setFont(font)
        self.browseButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 255);\n"
"border-color: rgb(85, 85, 255);\n"
"gridline-color: rgb(85, 85, 255);\n"
"")
        self.browseButton_3.setObjectName("browseButton_3")
        self.gridLayout_13.addWidget(self.browseButton_3, 2, 1, 2, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout_12.addWidget(self.label_10, 0, 2, 1, 1)
        # self.label_11 = QtWidgets.QLabel(self.tab_2)
        # self.label_11.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        # self.label_11.setObjectName("label_11")
        # self.gridLayout_12.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_12.addWidget(self.label_14, 0, 1, 1, 1)
        self.horizontalSlider_2 = QtWidgets.QLabel(self.tab_2)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout_12.addWidget(self.horizontalSlider_2, 1, 2, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_12, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_9.addWidget(self.label_5, 0, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.plottingGraph_2 = PlotWidget(self.tab_4)
        self.plottingGraph_2.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.plottingGraph_2.setObjectName("plottingGraph_2")
        self.plottingGraph_2.hideAxis('bottom')
        self.plottingGraph_2.hideAxis('left')
        self.plottingGraph_2.setBackground('w')
        self.plottingGraph_2.setStyleSheet( "border:1px solid rgb(0, 0, 0);")
        self.gridLayout.addWidget(self.plottingGraph_2, 1, 0, 1, 1)
        self.plottingGraph_3 = PlotWidget(self.tab_4)
        self.plottingGraph_3.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.plottingGraph_3.setObjectName("plottingGraph_3")
        self.plottingGraph_3.hideAxis('bottom')
        self.plottingGraph_3.hideAxis('left')
        self.plottingGraph_3.setBackground('w')
        self.plottingGraph_3.setStyleSheet( "border:1px solid rgb(0, 0, 0);")
        self.gridLayout.addWidget(self.plottingGraph_3, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout, 1, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_9.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mixpausebutton = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mixpausebutton.setFont(font)
        self.mixpausebutton.setStyleSheet("background-color: rgb(255, 214, 62);\n"
"\n"
"color: rgb(255, 255, 255);")
        self.mixpausebutton.setObjectName("mixpausebutton")
        self.gridLayout_2.addWidget(self.mixpausebutton, 0, 0, 1, 1)
        self.mixplaybutton = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mixplaybutton.setFont(font)
        self.mixplaybutton.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.mixplaybutton.setObjectName("mixplaybutton")
        self.gridLayout_2.addWidget(self.mixplaybutton, 0, 1, 1, 1)
        self.mixstopbutton = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mixstopbutton.setFont(font)
        self.mixstopbutton.setStyleSheet("background-color: rgb(255, 0, 4);\n"
"color: rgb(255, 255, 255);")
        self.mixstopbutton.setObjectName("mixstopbutton")
        self.gridLayout_2.addWidget(self.mixstopbutton, 0, 2, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_2, 3, 0, 1, 3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.plottingGraph_4 = PlotWidget(self.tab_4)
        self.plottingGraph_4.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.plottingGraph_4.setObjectName("plottingGraph_4")
        self.plottingGraph_4.hideAxis('bottom')
        self.plottingGraph_4.hideAxis('left')
        self.plottingGraph_4.setBackground('w')
        self.plottingGraph_4.setStyleSheet( "border:1px solid rgb(0, 0, 0);")
        self.gridLayout_3.addWidget(self.plottingGraph_4, 1, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_3, 2, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_9.addWidget(self.label, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout_6.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.showResult.setText(_translate("MainWindow", "Show Result"))
        self.label_3.setText(_translate("MainWindow", "SIMILAR SONGS"))
        self.label_2.setText(_translate("MainWindow", "SONG INFO:"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.recordingButton.setText(_translate("MainWindow", "Record"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Sound Recogniser"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Choose Spectrogram"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Browsed audio"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Recorded Audio"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Spectrogram"))
        self.browseButton_2.setText(_translate("MainWindow", "SONG 1 Browse"))
        self.label_13.setText(_translate("MainWindow", "Mixing Slider Value:"))
        # self.label_9.setText(_translate("MainWindow", "SONG 1"))
        self.spectogrambutton.setText(_translate("MainWindow", "Spectogram"))
        self.showResult_2.setText(_translate("MainWindow", "Show Result"))
        self.browseButton_3.setText(_translate("MainWindow", "SONG 2 Browse"))
        # self.label_11.setText(_translate("MainWindow", "SONG 2"))
        self.label_14.setText(_translate("MainWindow", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Mixer"))
        self.label_8.setText(_translate("MainWindow", "SONG 2 SPECTOGRAM"))
        self.label_7.setText(_translate("MainWindow", "SONG 1 SPECTOGRAM"))
        self.mixpausebutton.setText(_translate("MainWindow", "PAUSE"))
        self.mixplaybutton.setText(_translate("MainWindow", "PLAY"))
        self.mixstopbutton.setText(_translate("MainWindow", "STOP"))
        self.label_6.setText(_translate("MainWindow", "MIXED SPECTROGRAM"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Mixer Spectogram"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
