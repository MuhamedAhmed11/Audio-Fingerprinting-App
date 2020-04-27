from mainWindow import Ui_MainWindow
from pydub import AudioSegment
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime
import hashlib
import os
import sys
import wave
import winsound
import cv2
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pylab
import pyqtgraph as pg
import scipy
from scipy import signal
from scipy.io import wavfile
from scipy.signal import find_peaks
from skimage.feature import peak_local_max
from playsound import playsound
import pyaudio
import atexit
import threading
import operator
import ntpath
import contextlib
import time
import os
import threading
import time
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from mutagen.mp3 import MP3
import pygame
import warnings
warnings.simplefilter("ignore", DeprecationWarning)


class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.filepath1 = []
        self.mixerFilepath1 = []
        self.mixerFilepath2 = []
        self.samplerate = 47000.6
        self.xArray = []
        self.yArray = []
        self.spectrogramArray_1 = []
        self.mixerspectrogramArray1 = []
        self.mixerspectrogramArray2 = []
        self.IDX_FREQ_I = 0
        self.IDX_TIME_J = 1
        self.MIN_HASH_TIME_DELTA = 0
        self.MAX_HASH_TIME_DELTA = 200
        self.DEFAULT_FAN_VALUE = 15
        self.hashResult1 = None
        self.hashResult2 = None
        self.hashDatabase = None
        self.databaseSongs = []
        self.similarity = str
        self.songinfo = str
        self.counter = 0
        self.Result = []
        self.check_1 = False
        self.mixerCheck_1 = False
        self.mixerCheck_2 = False
        self.sound_info = None
        self.frame_rate = None
        self.recordedFilename = 'recorded.wav'
        self.ui.browseButton.clicked.connect(
            lambda: self.browse1('Sound Recognizer', self.filepath1, 1))
        self.ui.mixbrowse1.clicked.connect(
            lambda: self.browse1('Mixing', self.mixerFilepath1, 2))
        self.ui.mixbrowse2.clicked.connect(
            lambda: self.browse1('Mixing', self.mixerFilepath2, 3))
        self.ui.showResult.clicked.connect(self.iterationDatabase)
        self.ui.recordingButton.clicked.connect(self.record)
        self.ui.comboBox.activated.connect(lambda: self.plottingSpectrogram(
            self.filepath1, self.spectrogramArray_1, self.check_1, 'Sound Recognizer', 1))
        self.ui.playButton.clicked.connect(self.playRecordedAudio)
        # self.ui.resultRecording.clicked.connect(self.iterationDatabase)
        self.stylingOutput(self.ui.soundRecogniserOuput_2)
        self.pauseValue = False

    def browse1(self, mode, filepath, value):
        filepath = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                                               'DSP_Task4\Database', "Song files (*.wav *.mp3)")
        while filepath[0] == '':
            QtWidgets.QMessageBox.setStyleSheet(
                self, "background-color: rgb(255, 255, 255);")
            choice = QtWidgets.QMessageBox.question(
                self, 'WARNING!', "Please Choose file", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                self.browse1()
                sys.exit
            else:
                sys.exit

        if mode == 'Sound Recognizer' and value == 1:
            self.ui.soundRecogniserOuput_2.clear()
            # wav = wave.open(filepath[0], 'r')
            # frames = wav.(-1)
            # rate = wav.getframerate()
            # wav.close()
            # print(frames)
            self.songinfo = "Song Name: " + \
                str(ntpath.basename(filepath[0]))+"\n"
            self.ui.soundRecogniserOuput.setText(self.songinfo)
            self.stylingOutput(self.ui.soundRecogniserOuput)
            self.check_1 = True
            self.spectrogramFunc(
                filepath[0], self.spectrogramArray_1, self.check_1, mode, value)
            print("Awel ESHTAAA")

        if mode == 'Mixing' and value == 2:
            self.mixerCheck_1 = True
            self.spectrogramFunc(
                filepath[0], self.mixerspectrogramArray1, self.mixerCheck_1, mode, value)
            print("Awel Mix ESHTAAA")

        if mode == 'Mixing' and value == 3:
            self.mixerCheck_2 = True
            self.spectrogramFunc(
                filepath[0], self.mixerspectrogramArray2, self.mixerCheck_2, mode, value)
            print("Tany Mix ESHTAAA")

    def mixing(self):
        if self.mixerCheck_1 == True and self.mixerCheck_1 == True:
            sound1 = AudioSegment.from_file(self.mixerFilepath_1[0])
            sound2 = AudioSegment.from_file(self.mixerFilepath_2[0])
            combined = sound1.overlay(sound2)
            combined.export(
                r"C:\Users\DELL\Desktop\mixing.wav", format='wav')
            print("1")

            winsound.PlaySound(
                r"C:\Users\DELL\Desktop\mixing.wav", winsound.SND_FILENAME)
            return
        elif self.mixerCheck_1 == True and self.mixerCheck_2 == False:
            print("2")
            winsound.PlaySound(self.mixerFilepath_1[0], winsound.SND_FILENAME)
            return
        elif self.mixerCheck_1 == False and self.mixerCheck_2 == True:
            print("3")
            winsound.PlaySound(self.mixerFilepath_2[0], winsound.SND_FILENAME)
            return
        else:
            print("44")

    def hash_file(self, peaks):
        h1 = hashlib.sha1()
        if self.check_1:
            h1.update(peaks)
            self.hashResult1 = h1.hexdigest()

    def get_wav_info(self, wav_file):
        wav = wave.open(wav_file, 'r')
        frames = wav.readframes(-1)
        self.sound_info = pylab.fromstring(frames, 'Int16')
        self.frame_rate = wav.getframerate()
        wav.close()
        return self.sound_info, self.frame_rate

    def spectrogramFunc(self, filepath, spectrogramArray, check, mode, value):
        if check == True:
            self.sound_info, self.frame_rate = self.get_wav_info(
                filepath)
            self.sound_info = self.sound_info[0:60*self.frame_rate]
            self.plottingSpectrogram(
                filepath, spectrogramArray, check, mode, value)
        else:
            print("8LT YA 7OBY")

    def plottingSpectrogram(self, filepath, spectrogramArray, check, mode, value):
        if check == True:
            pylab.figure(num=None, figsize=(19, 12))
            # pylab.style.use('dark_background')
            plotting = pylab.subplot(111, frameon=False)
            plotting.get_xaxis().set_visible(False)
            plotting.get_yaxis().set_visible(False)
            spectrogramArray = pylab.specgram(
                self.sound_info, Fs=self.frame_rate)
            pylab.savefig('spectrogram_1.jpg', bbox_inches='tight')
            self.getPeaksData(spectrogramArray)
            imgArr = cv2.imread('spectrogram_1.jpg')
            img = pg.ImageItem(imgArr)
            img.rotate(270)
            if mode == 'Mixing':
                if value == 2:
                    self.ui.plottingGraph_2.clear()
                    self.ui.plottingGraph_2.addItem(img)
                if value == 3:
                    self.ui.plottingGraph_3.clear()
                    self.ui.plottingGraph_3.addItem(img)
            elif mode == 'Sound Recognizer':
                self.ui.plottingGraph.clear()
                if self.ui.comboBox.currentText() == "Browsed audio":
                    self.ui.plottingGraph.addItem(img)

                if self.ui.comboBox.currentText() == "Recorded Audio":
                    print("NOTHING")

        if check == False:
            choice = QtWidgets.QMessageBox.warning(
                self, 'Warning', "NOTHING TO  PRINT, PLEASE CHOOSE FILE", QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.No)

            if choice == QtWidgets.QMessageBox.Ok:
                self.browse1(mode, filepath, value)

    def getPeaksData(self, spectrogramArray):

        peaks, time_diff = find_peaks(((spectrogramArray)[0])[
            0], distance=150)
        pylab.plot(((spectrogramArray)[0])[0])
        pylab.plot(peaks, (((spectrogramArray)[0])[0])[peaks], "x")
        pylab.plot(np.zeros_like(
            ((spectrogramArray)[0])[0]), "--", color="red")

        fingerprint = self.hash_file(peaks)

    ######################## DATABASE #######################

    def hashFileDatabase(self, peaks):
        hashed = hashlib.sha1()
        hashed.update(peaks)
        self.hashDatabase = hashed.hexdigest()

    def getPeaksForDatabase(self, spectrogramArray):

        peaks, time_diff = find_peaks(((spectrogramArray)[0])[
            0], distance=150)

        pylab.plot(((spectrogramArray)[0])[0])
        pylab.plot(peaks, (((spectrogramArray)[0])[0])[peaks], "x")
        pylab.plot(np.zeros_like(
            ((spectrogramArray)[0])[0]), "--", color="red")
        fingerprint = self.hashFileDatabase(peaks)

    def spectrogramDatabase(self, file):
        sound_info, frame_rate = self.get_wav_info(file)
        pylab.figure(num=None, figsize=(19, 12))
        pylab.style.use('dark_background')
        plotting = pylab.subplot(111, frameon=False)
        plotting.get_xaxis().set_visible(False)
        plotting.get_yaxis().set_visible(False)
        databaseSpecrtoArray = pylab.specgram(
            sound_info, Fs=frame_rate)
        self.getPeaksForDatabase(databaseSpecrtoArray)
        # pylab.savefig('database.jpg', bbox_inches='tight')

    def iterationDatabase(self):
        self.similarity = str
        self.counter = 0
        directory = os.getcwd() + '\Database'
        for filename in os.listdir(directory):
            if filename.endswith(".wav") or filename.endswith(".mp3"):
                self.databaseSongs = os.path.join(directory, filename)
                self.spectrogramDatabase(self.databaseSongs)
                self.counter = self.counter+1
                self.compare(filename)
            else:
                print('No Data required')

    def compare(self, filename):
        hashBrowse = int(self.hashResult1, 16)
        hashForDatabase = int(self.hashDatabase, 16)
        result = ((hashForDatabase / hashBrowse)*100)
        if (result >= 80.0):
            print(filename)
            self.similarity = str(self.similarity)+"\n"+str(self.counter) + \
                ".  " + filename+"    Similarity Percentage: " + str(result)
            print("TAMAM EL KALAM")
            print("-----")

            return
        else:
            print("-----")
            print(filename)
            print("Msh TMAM")
            print("-----")

        self.ui.soundRecogniserOuput_2.setText(
            self.similarity[13:len(self.similarity)])

    def stylingOutput(self, outputBrowser):
        outputBrowser.setStyleSheet(
            "color: rgb(85, 85, 255);")
        outputBrowser.setFont(
            QtGui.QFont("Times", 15, QtGui.QFont.Bold))

    def record(self):
        # the file name output you want to record into
        self.recordedFilename = "recorded.wav"
        # set the chunk size of 1024 samples
        chunk = 1024
        # sample format
        FORMAT = pyaudio.paInt16
        # mono, change to 2 if you want stereo
        channels = 1
        # 44100 samples per second
        sample_rate = 44100
        record_seconds = 4
        # initialize PyAudio object
        p = pyaudio.PyAudio()
        # open stream object as input & output
        stream = p.open(format=FORMAT,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        output=True,
                        frames_per_buffer=chunk)
        frames = []
        print("Recording...")
        for i in range(int(44100 / chunk * record_seconds)):
            data = stream.read(chunk)
            # if you want to hear your voice while recording
            # stream.write(data)
            frames.append(data)
        print("Finished recording.")
        # stop and close stream
        stream.stop_stream()
        stream.close()
        # terminate pyaudio object
        p.terminate()
        # save audio file
        # open the file in 'write bytes' mode
        wf = wave.open(self.recordedFilename, "wb")
        # set the channels
        wf.setnchannels(channels)
        # set the sample format
        wf.setsampwidth(p.get_sample_size(FORMAT))
        # set the sample rate
        wf.setframerate(sample_rate)
        # write the frames as bytes
        wf.writeframes(b"".join(frames))
        # close the file
        wf.close()

    def playRecordedAudio(self):
        playsound(self.recordedFilename)

    def pauseFunc(self):
        self.pauseValue == True
        if self.pauseValue == True:
            pygame.init()
            pygame.mixer_music.pause()


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
