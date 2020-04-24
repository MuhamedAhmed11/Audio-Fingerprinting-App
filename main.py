from PyQt5 import QtWidgets, QtGui
from mainWindow import Ui_MainWindow
import sys
import winsound
from scipy import signal
from scipy.signal import find_peaks
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.io import wavfile
import pyqtgraph as pg
import os
from pydub import AudioSegment
import hashlib
import librosa
import librosa.display
import wave
import pylab
import cv2


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.playButton.clicked.connect(self.playSound)
        self.filepath1 = []
        self.filepath2 = []
        self.ui.browseButton.clicked.connect(self.browse1)
        self.ui.browseButton2.clicked.connect(self.browse2)
        self.ui.pushButton.clicked.connect(self.spectrogramFunc)
        self.samplerate = 47000.6
        self.xArray = []
        self.yArray = []
        self.spectrogramArray_1 = []
        self.spectrogramArray_2 = []
        self.chroma_stftArray_1 = []
        self.chroma_cqArray_1 = []
        self.chroma_stftArray_2 = []
        self.chroma_cqArray_2 = []
        self.check_1 = False
        self.check_2 = False

    def browse1(self):
        self.filepath1 = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                                               'DSP_Task4\Database', "Song files (*.wav *.mp3)")

        while self.filepath1[0] == '':
            choice = QtWidgets.QMessageBox.question(
                self, 'WARNING!', "Please Choose file", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                self.filepath1 = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                                                       'DSP_Task4\Database', "Song files (*.wav *.mp3)")
                sys.exit
            else:
                print("HEHE")
                sys.exit

        self.ui.graphicsView.clear()
        self.check_1 = True
        self.spectrogramFunc()
        print("ESHTAAA")

    def browse2(self):
        self.filepath2 = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open file', 'DSP_Task4\Database', "Song files (*.wav *.mp3)")
        while self.filepath2[0] == '':
            choice = QtWidgets.QMessageBox.question(
                self, 'WARNING!', "Please Choose file", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                self.filepath2 = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                                                       'DSP_Task4\Database', "Song files (*.wav *.mp3)")
                sys.exit
            else:
                print("HEHE")
                sys.exit

        self.check_2 = True
        self.spectrogramFunc()

    def playSound(self):
        if self.check_1 == True and self.check_2 == True:
            sound1 = AudioSegment.from_file(self.filepath1[0])
            sound2 = AudioSegment.from_file(self.filepath2[0])
            combined = sound1.overlay(sound2)
            self.hash_file()
            combined.export(
                r"C:\Users\DELL\Desktop\combined2.wav", format='wav')
            winsound.PlaySound(
                r"C:\Users\DELL\Desktop\combined2.wav", winsound.SND_FILENAME)
            return
        elif self.check_1 == True and self.check_2 == False:
            winsound.PlaySound(self.filepath1[0], winsound.SND_FILENAME)
            return
        elif self.check_1 == False and self.check_2 == True:
            winsound.PlaySound(self.filepath2[0], winsound.SND_FILENAME)
            return

    def hash_file(self):
        # make a hash object
        h1 = hashlib.sha1()
        h2 = hashlib.sha1()
        # open file for reading in binary mode
        with open(self.filepath1[0], 'rb') as file:
            # loop till the end of the file
            chunk1 = 0
            while chunk1 != b'':
                # read only 1024 bytes at a time
                chunk1 = file.read(1024)
                h1.update(chunk1)
        # return the hex representation of digest
        with open(self.filepath2[0], 'rb') as file:
            # loop till the end of the file
            chunk2 = 0
            while chunk2 != b'':
                # read only 1024 bytes at a time
                chunk2 = file.read(1024)
                h2.update(chunk2)
        # return the hex representation of digest
        hashResult1 = h1.hexdigest()
        hashResult2 = h2.hexdigest()
        print(hashResult1)
        print(hashResult2)
        print(hashResult1=hashResult2)

    def spectrogramFunc(self):
        if self.check_1 == True:
            sound_info, frame_rate = self.getWaveInfo(self.filepath1[0])
            pylab.figure(num=None, figsize=(19, 12))
            pylab.style.use('dark_background')
            plotting = pylab.subplot(111, frameon=False)
            plotting.get_xaxis().set_visible(False)
            plotting.get_yaxis().set_visible(False)
            self.spectrogramArray_1 = pylab.specgram(
                sound_info, Fs=frame_rate)

            self.getPeaksData(self.spectrogramArray_1)
            pylab.savefig('spectrogram_1.jpg', bbox_inches='tight')
            imgArr = cv2.imread('spectrogram_1.jpg')
            img = pg.ImageItem(imgArr)
            img.rotate(270)
            self.ui.graphicsView.addItem(img)

        if self.check_2 == True:
            sound_info, frame_rate = self.getWaveInfo(self.filepath2[0])
            pylab.figure(num=None, figsize=(19, 12))
            pylab.style.use('dark_background')
            plotting = pylab.subplot(111, frameon=False)
            plotting.get_xaxis().set_visible(False)
            plotting.get_yaxis().set_visible(False)
            self.spectrogramArray_2 = pylab.specgram(
                sound_info, Fs=frame_rate)  # , cmap=cmap, vmin=vmin)
            self.getPeaksData(self.spectrogramArray_2)
            pylab.savefig('spectrogram_2.jpg', bbox_inches='tight')
            imgArr = cv2.imread('spectrogram_2.jpg')
            img = pg.ImageItem(imgArr)
            img.rotate(270)
            self.ui.graphicsView_2.addItem(img)

    def getWaveInfo(self, wavFile):
        wav = wave.open(wavFile, 'r')
        frames = wav.readframes(-1)
        sound_info = pylab.fromstring(frames, 'Int16')
        frame_rate = wav.getframerate()
        wav.close()
        return sound_info, frame_rate

    def getPeaksData(self, spectrogramArray):
        peaks, _ = find_peaks(((spectrogramArray)[0])[
            0], distance=150)
        pylab.plot(((spectrogramArray)[0])[0])
        pylab.plot(peaks, (((spectrogramArray)[0])[0])[peaks], "x")
        pylab.plot(np.zeros_like(
            ((spectrogramArray)[0])[0]), "--", color="gray")


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
