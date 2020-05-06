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
from PyQt5.QtCore import QTime, QTimer, Qt
from scipy import signal
from scipy.signal import find_peaks, peak_widths, chirp
import imagehash
from PIL import Image
from scipy.io.wavfile import write
import scipy.io.wavfile
from distutils.core import setup
from os import path
import py2exe
import shutil
import soundfile as sf

warnings.simplefilter("ignore", DeprecationWarning)


class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ApplicationWindow, self).__init__()
        path2 = "Generated Files"
        if(path.exists(path2)):
            shutil.rmtree(path2)
        os.makedirs(path2)
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
        self.similarityres = QtWidgets.QTableWidgetItem()
        self.similaritymix = str
        self.similarityresmix = QtWidgets.QTableWidgetItem()
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
        self.spectronum = 1
        self.spectrogram = 'specrogram_'+str(self.spectronum)+'.jpg'
        self.specpeaks = 'spectrogramPeaks_'+str(self.spectronum)+'.jpg'
        self.DB_num = 1
        self.DB_spectro = 'databaseSpectrogram_'+str(self.DB_num)+'.jpg'
        self.DB_peaks = 'databsePeaks'+str(self.DB_num)+'.jpg'
        self.sliderResult_1 = None
        self.sliderResult_2 = None
        self.songMixingResult = None
        self.hashMixed_1 = None
        self.hashMixed_2 = None

        self.recordedFilename = 'recorded.wav'
        self.ui.browseButton.clicked.connect(
            lambda: self.browse1('Sound Recognizer', self.filepath1, 1))
        self.ui.browseButton_2.clicked.connect(
            lambda: self.browse1('Mixing', self.mixerFilepath1, 2))
        self.ui.browseButton_3.clicked.connect(
            lambda: self.browse1('Mixing', self.mixerFilepath2, 3))

        self.ui.showResult.clicked.connect(
            lambda: self.iterationDatabase(value=1))
        self.ui.recordingButton.clicked.connect(self.record)
        self.ui.comboBox.activated.connect(lambda: self.getComboboxValue())
        self.ui.playButton.clicked.connect(self.playRecordedAudio)
        # self.ui.resultRecording.clicked.connect(self.iterationDatabase)
        self.stylingOutput(self.ui.soundRecogniserOuput_2)
        self.stylingOutput(self.ui.soundRecogniserOuput_3)
        self.ui.mixplaybutton.clicked.connect(self.mixing)
        self.ui.mixpausebutton.clicked.connect(self.pauseFunc)
        self.ui.mixstopbutton.clicked.connect(self.stopFunc)
        self.ui.showResult_2.clicked.connect(self.soundMixingInfo)
        self.ui.spectogrambutton.clicked.connect(self.goToPlottingTab)
        model = self.ui.soundRecogniserOuput_2
        model.setColumnCount(2)
        model.setSortingEnabled(True)
        model.sortItems(1, Qt.DescendingOrder)
        model.setHorizontalHeaderLabels(
            ['Song Name ', 'Similarity Percentage'])
        header = self.ui.soundRecogniserOuput_2.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        model2 = self.ui.soundRecogniserOuput_3
        model2.setColumnCount(2)
        model2.setSortingEnabled(True)
        model2.sortItems(1, Qt.DescendingOrder)
        model2.setHorizontalHeaderLabels(
            ['Song Name ', 'Similarity Percentage'])
        header2 = self.ui.soundRecogniserOuput_3.horizontalHeader()
        header2.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def browse1(self, mode, filepath, value):
        filepath = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                                               'DSP_Task4\Database', "Song files (*.wav *.mp3)")

        if value == 1:
            self.ui.soundRecogniserOuput_2.setRowCount(0)
        elif value == 2:
            self.ui.soundRecogniserOuput_3.setRowCount(0)
        elif value == 3:
            self.ui.soundRecogniserOuput_3.setRowCount(0)

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
            filename, extension = os.path.splitext(filepath[0])
            dst = str(filename) + ".wav"
            if extension == ".mp3":
                sound = AudioSegment.from_mp3(filepath[0])
                sound.export(dst, format="wav")

        if filepath[0] != '':
            if mode == 'Sound Recognizer' and value == 1:
                # self.ui.soundRecogniserOuput_2.clear()
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
                    dst, self.spectrogramArray_1, self.check_1, mode, value)
                self.filepath1 = dst
                print("Awel ESHTAAA")

            if mode == 'Mixing' and value == 2:
                self.mixerCheck_1 = True
                self.spectrogramFunc(
                    dst, self.mixerspectrogramArray1, self.mixerCheck_1, mode, value)
                self.mixerFilepath1 = dst
                print("Awel Mix ESHTAAA")

            if mode == 'Mixing' and value == 3:
                self.mixerCheck_2 = True
                self.spectrogramFunc(
                    dst, self.mixerspectrogramArray2, self.mixerCheck_2, mode, value)
                self.mixerFilepath2 = dst
                print("Tany Mix ESHTAAA")

    def soundMixingInfo(self):
        if self.mixerCheck_1 == True and self.mixerCheck_2 == True:
            soundData_1, fs_1 = self.getWaveInfo(self.mixerFilepath1)
            soundData_2, fs_2 = self.getWaveInfo(self.mixerFilepath2)
            soundData_1 = soundData_1[0:60 * fs_1]
            soundData_2 = soundData_2[0:60 * fs_2]

            sliderValue_1 = self.ui.horizontalSlider_1.value()
            sliderValue_2 = self.ui.horizontalSlider_2.value()

            self.sliderResult_1 = (sliderValue_1 / 100)
            self.sliderResult_2 = (1 - self.sliderResult_1)

            self.songMixingResult = np.add(np.multiply(
                soundData_1, self.sliderResult_1), np.multiply(soundData_2, self.sliderResult_2))
            write("Mixed Song.wav", 44100, self.songMixingResult)
            self.spectrogramFunc(
                'Mixed Song.wav', self.mixingspectrogramArray, check=True, mode='Mixing', value=4)
            self.iterationDatabase(value=2)

        if self.mixerCheck_1 == True and self.mixerCheck_2 == False:
            choice = QtWidgets.QMessageBox.question(
                self, 'Warning', "You don't choose second song, YOU WANT TO CHOOSE THE SECOND SONG?", QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Ok:
                self.browse1(mode='Mixing', filepath="Mixed Song.wav", value=4)

        if self.mixerCheck_1 == False and self.mixerCheck_2 == True:
            choice = QtWidgets.QMessageBox.question(
                self, 'Warning', "You don't choose first song, YOU WANT TO CHOOSE THE FIRST SONG?", QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Ok:
                self.browse1(mode='Mixing', filepath="Mixed Song.wav", value=4)

        if self.mixerCheck_1 == False and self.mixerCheck_2 == False:
            choice = QtWidgets.QMessageBox.question(
                self, 'Warning', "You don't choose two songs, PLEASE CHOOSE THE BOTH SONGS", QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Ok:
                self.browse1(mode='Mixing', filepath="Mixed Song.wav", value=4)

    def goToPlottingTab(self):
        self.ui.tabWidget.setCurrentIndex(3)

    def mixing(self):
        if self.mixerCheck_1 == True and self.mixerCheck_1 == True:
            if (self.first == 0):
                sound1 = AudioSegment.from_file(self.mixerFilepath1)
                sound2 = AudioSegment.from_file(self.mixerFilepath2)
                combined = sound1.overlay(sound2)
                mixedFilename = '/mixing.wav'
                combined.export(os.getcwd() + "/Generated Files" +
                                mixedFilename, format='wav')
                self.spectrogramFunc(
                    os.getcwd() + "/Generated Files"+mixedFilename, self.mixingspectrogramArray, check=True, mode='Mixing', value=4)
                self.playFunc()
                print("1")
            else:
                self.playFunc()
            return

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
            print("the filepath is :")
            print(filepath)
            frameRate, soundData = scipy.io.wavfile.read(filepath)
            self.spectrogram = 'specrogram_'+str(self.spectronum)+'.jpg'
            self.specpeaks = 'spectrogramPeaks_'+str(self.spectronum)+'.jpg'
            soundData = soundData[0:60*frameRate]
            plotting = pylab.subplot(111, frameon=False)
            plotting.get_xaxis().set_visible(False)
            plotting.get_yaxis().set_visible(False)
            soundData=np.asarray(soundData)
            soundData=soundData.flatten()
            print(soundData)
            spectrogramArray = pylab.specgram(soundData, Fs=frameRate)
            pylab.savefig(os.getcwd() + "/Generated Files"+'/' +
                          self.spectrogram, bbox_inches='tight')
            # hash_1 = imagehash.phash(Image.open(
            #     os.getcwd() + f"/Generated Files\{self.spectrogram}"))
            # self.hashResult1 = hash_1
            self.getPeaksData(spectrogramArray)
            pylab.savefig(os.getcwd() + "/Generated Files" +
                          f'/{self.specpeaks}', bbox_inches='tight')
            hash_1 = imagehash.phash(
                Image.open(os.getcwd() + f"/Generated Files\{self.specpeaks}"))
            self.hashResult1 = hash_1

            imgArr = cv2.imread(
                os.getcwd() + f"/Generated Files\{self.spectrogram}")
            img = pg.ImageItem(imgArr)
            img.rotate(270)
            self.spectronum += 1
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
        peaks, time_diff = find_peaks(
            spectrogramArray[0][0], height=0, width=0.5, distance=1.5)
        pylab.plot(spectrogramArray[0][0])
        pylab.plot(peaks, (spectrogramArray[0][0])[peaks], "x")
        pylab.plot(np.zeros_like(
            spectrogramArray[0][0]), "--", color="red")

    ######################## DATABASE #######################

    def spectrogramDatabase(self, file):
        sample_rate, sound_data = scipy.io.wavfile.read(file)
        sound_data = sound_data[0:60*sample_rate]
        pylab.figure(num=None, figsize=(19, 12))
        plotting = pylab.subplot(111, frameon=False)
        plotting.get_xaxis().set_visible(False)
        plotting.get_yaxis().set_visible(False)
        sound_data=np.asarray(sound_data)
        sound_data=sound_data.flatten()
        spectrogramArray = pylab.specgram(sound_data, Fs=sample_rate)
        self.DB_spectro = 'databaseSpectrogram_'+str(self.DB_num)+'.jpg'
        self.DB_peaks = 'databsePeaks'+str(self.DB_num)+'.jpg'
        pylab.savefig(os.getcwd() + "/Generated Files" +
                      f'/{self.DB_spectro}', bbox_inches='tight')
        # hash_1 = imagehash.phash(
        #     Image.open(os.getcwd() + f"/Generated Files\{self.DB_spectro}"))
        # self.hashDatabase = hash_1

        self.getPeaksData(spectrogramArray)
        pylab.savefig(os.getcwd() + "/Generated Files" +
                      f'/{self.DB_peaks}', bbox_inches='tight')
        hash_1 = imagehash.phash(Image.open(
            os.getcwd() + f"/Generated Files\{self.DB_peaks}"))
        self.hashDatabase = hash_1
        self.DB_num += 1

    def iterationDatabase(self, value):
        self.similarity = str
        self.similarityres = QtWidgets.QTableWidgetItem()
        self.similaritymix = str
        self.similarityresmix = QtWidgets.QTableWidgetItem()
        if value == 1:
            self.ui.soundRecogniserOuput_2.setRowCount(0)
        elif value == 2:
            self.ui.soundRecogniserOuput_3.setRowCount(0)
        self.counter = 0
        directory = os.getcwd() + '\Database'
        #directory = r'C:\Users\DELL\Desktop\Database Songs'

        for filename in os.listdir(directory):
            if filename.endswith(".wav") or filename.endswith(".mp3"):
                self.databaseSongs = os.path.join(directory, filename)
                filename, extension = os.path.splitext(filename)
                dst = directory + "\\" + str(filename) + ".wav"
                if extension == ".mp3":
                    sound = AudioSegment.from_mp3(self.databaseSongs)
                    sound.export(dst, format="wav")

                self.spectrogramDatabase(dst)
                self.counter = self.counter+1
                self.compare(filename, value)
            else:
                print('No Data required')
            self.tableadd(value)

    def compare(self, filename, value):
        if self.check_1 == True and value == 1:
            hashBrowse = self.hashResult1
            hashForDatabase = self.hashDatabase
            result = hashBrowse - hashForDatabase
            print("PEAKS COMPARE")
            print(filename)
            print("------")
            finalResult = 100 - result
            print("Final Result", finalResult)

            if (finalResult > 50.0):
                print(filename)
                print(finalResult)
                self.similarity = str
                self.similarityres = QtWidgets.QTableWidgetItem()
                self.similarity = filename
                self.similarityres.setData(Qt.EditRole, finalResult)
                print("TAMAM EL KALAM")
                print("-----")
            print("BROWSE")
            self.mixerCheck_1 = False

        if self.mixerCheck_1 == True and self.mixerCheck_2 == True and value == 2:
            self.check_1 = False
            hashBrowse = self.hashResult1
            hashForDatabase = self.hashDatabase
            result = hashBrowse - hashForDatabase
            print("PEAKS COMPARE")
            print(filename)
            print("------")
            finalResult = 100 - result
            print("Final Result", finalResult)
            print("MIXING")

            if (finalResult > 50.0):
                print(filename)
                print(finalResult)
                self.similaritymix = str
                self.similarityresmix = QtWidgets.QTableWidgetItem()
                self.similaritymix = filename
                self.similarityresmix.setData(Qt.EditRole, finalResult)
                print("TAMAM EL KALAM")
                print("-----")
            print("BROWSE")

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
            pygame.mixer_music.load(
                os.getcwd() + "/Generated Files"+"/mixing.wav")
            pygame.mixer_music.play()

    def tableadd(self, value):
        if value == 1:
            if len(str(self.similarity)) > 13:
                rowPosition = self.ui.soundRecogniserOuput_2.rowCount()
                self.ui.soundRecogniserOuput_2.insertRow(rowPosition)
                self.ui.soundRecogniserOuput_2.setItem(
                    rowPosition, 0, QtGui.QTableWidgetItem(self.similarity))
                self.ui.soundRecogniserOuput_2.setItem(
                    rowPosition, 1, self.similarityres)
            else:
                rowPosition11 = self.ui.soundRecogniserOuput_2.rowCount()
                self.ui.soundRecogniserOuput_2.insertRow(rowPosition11)
                self.ui.soundRecogniserOuput_2.setItem(
                    rowPosition, 0, QtGui.QTableWidgetItem("No Similar Music or Vocals"))
        else:
            if len(str(self.similaritymix)) > 13:
                rowPosition2 = self.ui.soundRecogniserOuput_3.rowCount()
                self.ui.soundRecogniserOuput_3.insertRow(rowPosition2)
                self.ui.soundRecogniserOuput_3.setItem(
                    rowPosition2, 0, QtGui.QTableWidgetItem(self.similaritymix))
                self.ui.soundRecogniserOuput_3.setItem(
                    rowPosition2, 1, self.similarityresmix)
            else:
                rowPosition22 = self.ui.soundRecogniserOuput_2.rowCount()
                self.ui.soundRecogniserOuput_2.insertRow(rowPosition22)
                self.ui.soundRecogniserOuput_3.setItem(
                    rowPosition22, 0, QtGui.QTableWidgetItem("No Similar Music or Vocals"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()