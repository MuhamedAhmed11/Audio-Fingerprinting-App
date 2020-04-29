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
        self.recordedspectrogramArray = []
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
        self.recorded_counter = 0
        self.check_1 = False
        self.checkRecording = False
        self.mixerCheck_1 = False
        self.mixerCheck_2 = False
        self.resultArr = []
        # self.sound_info = None
        # self.frame_rate = None
        self.recordedFilename = 'recorded.wav'
        self.ui.browseButton.clicked.connect(
            lambda: self.browse1('Sound Recognizer', self.filepath1, 1))
        self.ui.mixbrowse1.clicked.connect(
            lambda: self.browse1('Mixing', self.mixerFilepath1, 2))
        self.ui.mixbrowse2.clicked.connect(
            lambda: self.browse1('Mixing', self.mixerFilepath2, 3))
        self.ui.showResult.clicked.connect(self.iterationDatabase)
        self.ui.recordingButton.clicked.connect(self.record)
        self.ui.comboBox.activated.connect(lambda: self.getComboboxValue())
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

    def getWaveInfo(self, wav_file):
        wav = wave.open(wav_file, 'r')
        frames = wav.readframes(-1)
        soundData = pylab.fromstring(frames, 'Int16')
        frameRate = wav.getframerate()
        wav.close()
        return soundData, frameRate

    def spectrogramFunc(self, filepath, spectrogramArray, check, mode, value):
        if check == True:
            pylab.figure(num=None, figsize=(19, 12))
            soundData, frameRate = self.getWaveInfo(
                filepath)
            soundData = soundData[0:60*frameRate]
            plotting = pylab.subplot(111, frameon=False)
            plotting.get_xaxis().set_visible(False)
            plotting.get_yaxis().set_visible(False)
            spectrogramArray = pylab.specgram(soundData, Fs=frameRate)
            pylab.savefig('spectrogram_1.jpg', bbox_inches='tight')
            hash_1 = imagehash.phash(Image.open('spectrogram_1.jpg'))
            self.hashResult1 = hash_1
            print("HASH 1 :", self.hashResult1)
            self.getPeaksData(spectrogramArray)
            pylab.savefig('spectrogramPeaks_1.jpg', bbox_inches='tight')
            hash_2 = imagehash.phash(Image.open('spectrogramPeaks_1.jpg'))
            self.hashResult2 = hash_2
            print('Hash 2 :', self.hashResult2)
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
                if self.ui.comboBox.currentText() == "Browsed audio":
                    self.ui.plottingGraph.clear()
                    self.ui.plottingGraph.addItem(img)

                if self.ui.comboBox.currentText() == "Recorded Audio":
                    self.ui.plottingGraph.clear()
                    self.ui.plottingGraph.addItem(img)

        if check == False and (value == 1 or value == 2 or value == 3 or value == 4):
            choice = QtWidgets.QMessageBox.warning(
                self, 'Warning', "NOTHING TO  PRINT, PLEASE CHOOSE FILE", QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Ok:
                self.browse1(mode=mode, filepath=filepath, value=value)
        if check == False and value == 5:
            self.ui.tabWidget.setCurrentIndex(0)

    def getPeaksData(self, spectrogramArray):

        peaks, time_diff = find_peaks(((spectrogramArray)[0])[
            0], distance=150)
        pylab.plot(((spectrogramArray)[0])[0])
        pylab.plot(peaks, (((spectrogramArray)[0])[0])[peaks], "x")
        pylab.plot(np.zeros_like(
            ((spectrogramArray)[0])[0]), "--", color="red")

    ######################## DATABASE #######################

    def getPeaksForDatabase(self, spectrogramArray):
        peaks, time_diff = find_peaks(((spectrogramArray)[0])[
            0], distance=150)
        pylab.plot(((spectrogramArray)[0])[0])
        pylab.plot(peaks, (((spectrogramArray)[0])[0])[peaks], "x")
        pylab.plot(np.zeros_like(
            ((spectrogramArray)[0])[0]), "--", color="red")

    def spectrogramDatabase(self, file):
        sound_data, sample_rate = self.getWaveInfo(file)
        sound_data = sound_data[0:60*sample_rate]
        pylab.figure(num=None, figsize=(19, 12))
        plotting = pylab.subplot(111, frameon=False)
        plotting.get_xaxis().set_visible(False)
        plotting.get_yaxis().set_visible(False)
        spectrogramArray = pylab.specgram(sound_data, Fs=sample_rate)

        pylab.savefig('databaseSpectrogram_1.jpg', bbox_inches='tight')
        hash_1 = imagehash.phash(Image.open('databaseSpectrogram_1.jpg'))
        self.hashDatabase = hash_1

        self.getPeaksData(spectrogramArray)
        pylab.savefig('databasePeaks.jpg', bbox_inches='tight')
        hash_2 = imagehash.phash(Image.open('databasePeaks.jpg'))
        self.hashDatabase2 = hash_2

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
        if len(str(self.similarity)) > 13:        
            self.ui.soundRecogniserOuput_2.setText(self.similarity[13:len(self.similarity)]) 
        else:
            self.ui.soundRecogniserOuput_2.setText("No Similar Music or Vocals")

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

        finalResult = (int(result1) + int(result2))
        print("Final Result", finalResult)
        print('------')

        if (finalResult < 30.0):
            print(filename)
            print(finalResult)
            self.similarity =str(self.similarity) +"\n"+str(self.counter) + "." + filename+ "Similarity Percentage: " + str(finalResult)
            print("TAMAM EL KALAM")
            print("-----")

     

    def stylingOutput(self, outputBrowser):
        outputBrowser.setStyleSheet(
            "color: rgb(85, 85, 255);")
        outputBrowser.setFont(
            QtGui.QFont("Times", 15, QtGui.QFont.Bold))

    def record(self):

        # the file name output you want to record into
        self.recordedFilename = "recorded"+str(self.recorded_counter)+".wav"
        # set the chunk size of 1024 samples
        chunk = 1024
        # sample format
        FORMAT = pyaudio.paInt16
        # mono, change to 2 if you want stereo
        channels = 1
        # 44100 samples per second
        sample_rate = 44100
        record_seconds = 20
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
        self.checkRecording = True
        self.spectrogramFunc(self.recordedFilename, self.recordedspectrogramArray,
                             self.checkRecording, 'Sound Recognizer', 5)
        self.recorded_counter += 1

    def getComboboxValue(self):
        if self.ui.comboBox.currentText() == 'Browsed audio':
            self.spectrogramFunc(
                self.filepath1, self.spectrogramArray_1, self.check_1, 'Sound Recognizer', 1)
        if self.ui.comboBox.currentText() == "Recorded Audio":
            print(self.recordedFilename)
            print(self.recordedspectrogramArray)
            print(self.checkRecording)
            self.spectrogramFunc(
                self.recordedFilename, self.recordedspectrogramArray, self.checkRecording, 'Sound Recognizer', 5)

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
