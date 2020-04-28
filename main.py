from mainWindow import Ui_MainWindow
import hashlib
import ntpath
import os
import sys
import tkinter.messagebox
import warnings
import wave
import winsound
from tkinter import *
from tkinter import filedialog, ttk
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pyaudio
import pygame
import pylab
import pyqtgraph as pg
import scipy
from mutagen.mp3 import MP3
from playsound import playsound
from pydub import AudioSegment
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QTime, QTimer
from scipy import signal
from scipy.signal import find_peaks
import imagehash
from PIL import Image


warnings.simplefilter("ignore", DeprecationWarning)


class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.filepath1 = []
        self.mixerFilepath1 = []
        self.mixerFilepath2 = []
        self.spectrogramArray_1 = []
        self.mixerspectrogramArray1 = []
        self.mixerspectrogramArray2 = []
        self.mixingspectrogramArray = []
        self.hashResult1 = None
        self.hashResult2 = None
        self.hashDatabase = None
        self.hashDatabase2 = None
        self.databaseSongs = []
        self.similarity = str
        self.songinfo = str
        self.counter = 0
        self.Result = []
        self.paused = 0
        self.first = 0
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
        self.ui.mixplaybutton.clicked.connect(self.mixing)
        self.ui.mixpausebutton.clicked.connect(self.pauseFunc)
        self.ui.mixstopbutton.clicked.connect(self.stopFunc)

    def browse1(self, mode, filepath, value):
        filepath = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                                               'DSP_Task4\Database', "Song files (*.wav *.mp3)")
        self.ui.soundRecogniserOuput_2.clear()
        if filepath[0] == '':
            QtWidgets.QMessageBox.setStyleSheet(
                self, "background-color: rgb(255, 255, 255);")
            choice = QtWidgets.QMessageBox.question(
                self, 'WARNING!', "Please Choose file", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                filepath = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                                                 'DSP_Task4\Database', "Song files (*.wav *.mp3)")
                sys.exit
            else:
                sys.exit
        if filepath[0] != '':
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
                self.filepath1 = filepath[0]
                print("Awel ESHTAAA")

            if mode == 'Mixing' and value == 2:
                self.mixerCheck_1 = True
                self.spectrogramFunc(
                    filepath[0], self.mixerspectrogramArray1, self.mixerCheck_1, mode, value)
                self.mixerFilepath1 = filepath[0]
                print("Awel Mix ESHTAAA")

            if mode == 'Mixing' and value == 3:
                self.mixerCheck_2 = True
                self.spectrogramFunc(
                    filepath[0], self.mixerspectrogramArray2, self.mixerCheck_2, mode, value)
                self.mixerFilepath2 = filepath[0]
                print("Tany Mix ESHTAAA")

    def mixing(self):
        print("Mixer 1 check", self.mixerCheck_1)
        print("Mixer 2 check", self.mixerCheck_2)
        print("Mixer 1 check", self.mixerFilepath1)
        print("Mixer 2 check", self.mixerFilepath2)
        if self.mixerCheck_1 == True and self.mixerCheck_1 == True:
            if (self.first == 0):
                sound1 = AudioSegment.from_file(self.mixerFilepath1)
                sound2 = AudioSegment.from_file(self.mixerFilepath2)
                combined = sound1.overlay(sound2)
                mixedFilename = os.getcwd() + '\mixing.wav'
                combined.export(mixedFilename, format='wav')
                self.spectrogramFunc(
                    mixedFilename, self.mixingspectrogramArray, check=True, mode='Mixing', value=4)
                self.playFunc()
                print("1")
            else:
                self.playFunc()
            return
        elif self.mixerCheck_1 == True and self.mixerCheck_2 == False:
            print("2")
            winsound.PlaySound(self.mixerFilepath1, winsound.SND_FILENAME)
            return
        elif self.mixerCheck_1 == False and self.mixerCheck_2 == True:
            print("3")
            winsound.PlaySound(self.mixerFilepath2, winsound.SND_FILENAME)
            return
        else:
            print("44")

    def hash_file(self, peaks):
        h1 = hashlib.sha1()
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
            hash_1 = imagehash.phash(Image.open('spectrogram_1.jpg'))
            self.hashResult1 = hash_1
            ################### HERE #####################
            peaks, time_diff = find_peaks(
                ((spectrogramArray)[0])[0], distance=150)
            pylab.plot(((spectrogramArray)[0])[0])
            pylab.plot(peaks, (((spectrogramArray)[0])[0])[peaks], "x")
            pylab.plot(np.zeros_like(
                ((spectrogramArray)[0])[0]), "--", color="red")

            pylab.savefig('spectrogramPeaks_1.jpg', bbox_inches='tight')
            hash_2 = imagehash.phash(Image.open('spectrogramPeaks_1.jpg'))
            self.hashResult2 = hash_2
            # self.getPeaksData(spectrogramArray)
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
                if value == 4:
                    self.ui.plottingGraph_4.clear()
                    self.ui.plottingGraph_4.addItem(img)

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
                self.browse1(mode=mode, filepath=filepath, value=value)

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

    def waveInfo(self, file):
        wav = wave.open(file, 'r')
        frames = wav.readframes(-1)
        sound_data = pylab.fromstring(frames, 'Int16')
        sample_rate = wav.getframerate()
        wav.close()
        return sound_data, sample_rate

    def spectrogramDatabase(self, file):
        sound_data, sample_rate = self.waveInfo(file)
        sound_data = sound_data[0:60*sample_rate]
        databaseSpecrtoArray = pylab.specgram(sound_data, Fs=sample_rate)

        pylab.figure(num=None, figsize=(19, 12))
        # pylab.style.use('dark_background')
        plotting = pylab.subplot(111, frameon=False)
        plotting.get_xaxis().set_visible(False)
        plotting.get_yaxis().set_visible(False)
        spectrogramArray = pylab.specgram(
            sound_data, Fs=sample_rate)

        pylab.savefig('databaseSpectrogram_1.jpg', bbox_inches='tight')
        hash_1 = imagehash.phash(Image.open('databaseSpectrogram_1.jpg'))
        self.hashDatabase = hash_1
        ################### HERE #####################
        peaks, time_diff = find_peaks(
            ((spectrogramArray)[0])[0], distance=150)
        pylab.plot(((spectrogramArray)[0])[0])
        pylab.plot(peaks, (((spectrogramArray)[0])[0])[peaks], "x")
        pylab.plot(np.zeros_like(
            ((spectrogramArray)[0])[0]), "--", color="red")

        pylab.savefig('databasePeaks.jpg', bbox_inches='tight')
        hash_2 = imagehash.phash(Image.open('databasePeaks.jpg'))
        self.hashDatabase2 = hash_2
        # self.getPeaksForDatabase(databaseSpecrtoArray)
        # pylab.savefig('database.jpg', bbox_inches='tight')

    def iterationDatabase(self):
        self.similarity = str
        self.counter = 0
        directory = r'C:\Users\DELL\Desktop\Database Songs'
        for filename in os.listdir(directory):
            if filename.endswith(".wav") or filename.endswith(".mp3"):
                self.databaseSongs = os.path.join(directory, filename)
                self.spectrogramDatabase(self.databaseSongs)
                self.counter = self.counter+1
                self.compare(filename)
            else:
                print('No Data required')

    def compare(self, filename):
        hashBrowse_1 = self.hashResult1
        hashForDatabase_1 = self.hashDatabase
        result1 = (hashBrowse_1 - hashForDatabase_1)
        print("SONG:", filename)
        print("SPECTROGRAM COMPARE")
        print(result1)
        print("------")
        hashBrowse_2 = self.hashResult2
        hashForDatabase_2 = self.hashDatabase2
        result2 = hashBrowse_2 - hashForDatabase_2
        print("PEAKS COMPARE")
        print(result2)
        print("------")
        print("------")

        # if (result >= 80.0):
        #     print(filename)
        #     print(result)
        #     self.similarity = str(self.similarity)+"\n"+str(self.counter) + \
        #         ".  " + filename+"    Similarity Percentage: " + str(result)
        #     print("TAMAM EL KALAM")
        #     print("-----")

        #     return
        # else:
        #     print("-----")
        #     print(filename)
        #     print(result)
        #     print("Msh TMAM")
        #     print("-----")

        # self.ui.soundRecogniserOuput_2.setText(
        #     self.similarity[13:len(self.similarity)])

        # self.ui.soundRecogniserOuput_2.setText(
        #     self.similarity[13:len(self.similarity)])
        # # self.DTW()

        # self.ui.soundRecogniserOuput_2.setText(
        #     self.similarity[13:len(self.similarity)])
        # self.DTW()

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
        self.paused = 1
        pygame.mixer_music.pause()
        print("345435")

    def stopFunc(self):
        pygame.mixer_music.stop()
        self.paused = 0
        print('9699')

    def playFunc(self):
        self.first = 1
        if (self.paused == 1):
            pygame.mixer_music.unpause()
            self.paused = 0
        else:
            pygame.init()
            pygame.mixer_music.load("mixing.wav")
            pygame.mixer_music.play()


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
