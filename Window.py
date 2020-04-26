# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1023, 718)
        MainWindow.setStyleSheet("background-color: rgb(184, 63, 158);\n"
"background-color: rgb(133, 133, 200);\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.browseButton = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.browseButton.setFont(font)
        self.browseButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(98, 0, 147);\n"
"")
        self.browseButton.setObjectName("browseButton")
        self.verticalLayout.addWidget(self.browseButton)
        self.soundRecogniserOuput = QtWidgets.QTextBrowser(self.tab)
        self.soundRecogniserOuput.setObjectName("soundRecogniserOuput")
        self.verticalLayout.addWidget(self.soundRecogniserOuput)
        self.soundRecogniserOuput_2 = QtWidgets.QTextBrowser(self.tab)
        self.soundRecogniserOuput_2.setObjectName("soundRecogniserOuput_2")
        self.verticalLayout.addWidget(self.soundRecogniserOuput_2)
        self.showResult = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.showResult.setFont(font)
        self.showResult.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(98, 0, 147);\n"
"")
        self.showResult.setObjectName("showResult")
        self.verticalLayout.addWidget(self.showResult)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.RecordingOutput = QtWidgets.QTextBrowser(self.tab_2)
        self.RecordingOutput.setObjectName("RecordingOutput")
        self.gridLayout_2.addWidget(self.RecordingOutput, 0, 0, 1, 1)
        self.RecordingOutput_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.RecordingOutput_2.setObjectName("RecordingOutput_2")
        self.gridLayout_2.addWidget(self.RecordingOutput_2, 1, 0, 1, 1)
        self.resultRecording = QtWidgets.QPushButton(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.resultRecording.setFont(font)
        self.resultRecording.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(98, 0, 147);")
        self.resultRecording.setObjectName("resultRecording")
        self.gridLayout_2.addWidget(self.resultRecording, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.recordingButton = QtWidgets.QPushButton(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recordingButton.setFont(font)
        self.recordingButton.setStyleSheet("background-color: rgb(255, 0, 4);\n"
"color: rgb(255, 255, 255);")
        self.recordingButton.setObjectName("recordingButton")
        self.gridLayout_3.addWidget(self.recordingButton, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(107, 0, 161);\n"
"color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_4.addWidget(self.comboBox, 0, 0, 1, 1)
        self.plottingGraph = PlotWidget(self.tab_3)
        self.plottingGraph.setObjectName("plottingGraph")
        self.gridLayout_4.addWidget(self.plottingGraph, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
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
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.showResult.setText(_translate("MainWindow", "Show Result"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Sound Recogniser"))
        self.resultRecording.setText(_translate("MainWindow", "Result"))
        self.recordingButton.setText(_translate("MainWindow", "Record"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Recording"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Choose Spectrogram"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Browsed audio"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Recorded Audio"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Spectrogram"))
from pyqtgraph import PlotWidget
