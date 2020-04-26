from Window import Ui_MainWindow
from pydub import AudioSegment
from PyQt5 import QtGui, QtWidgets

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
import warnings
warnings.simplefilter("ignore", DeprecationWarning)


class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.filepath1 = []
        self.filepath2 = []
        # self.ui.browseButton2.clicked.connect(self.browse2)
        self.samplerate = 47000.6
        self.xArray = []
        self.yArray = []
        self.spectrogramArray_1 = []
        self.spectrogramArray_2 = []
        self.IDX_FREQ_I = 0
        self.IDX_TIME_J = 1
        self.MIN_HASH_TIME_DELTA = 0
        self.MAX_HASH_TIME_DELTA = 200
        self.DEFAULT_FAN_VALUE = 15
        self.hashResult1 = None
        self.hashResult2 = None
        self.hashDatabase = None
        self.databaseSongs = []
        self.check_1 = False
        self.check_2 = False
        self.sound_info = None
        self.frame_rate = None
        self.recordedFilename = 'recorded.wav'
        self.ui.browseButton.clicked.connect(self.browse1)
        self.ui.showResult.clicked.connect(self.iterationDatabase)
        self.ui.recordingButton.clicked.connect(self.record)
        self.ui.comboBox.activated.connect(self.plottingSpectrogram)
        self.ui.playButton.clicked.connect(self.playRecordedAudio)
        self.ui.resultRecording.clicked.connect(self.iterationDatabase)

    def browse1(self):
        self.filepath1 = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                                               'DSP_Task4\Database', "Song files (*.wav *.mp3)")

        while self.filepath1[0] == '':
            QtWidgets.QMessageBox.setStyleSheet(
                self, "background-color: rgb(255, 255, 255);")
            choice = QtWidgets.QMessageBox.question(
                self, 'WARNING!', "Please Choose file", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                self.filepath1 = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                                                       'DSP_Task4\Database', "Song files (*.wav *.mp3)")
                sys.exit
            else:
                self.close()
                sys.exit

        self.check_1 = True
        self.check_2 = False
        self.spectrogramFunc()
        print("Awel ESHTAAA")

    def playSound(self):
        if self.check_1 == True and self.check_2 == True:
            sound1 = AudioSegment.from_file(self.filepath1[0])
            sound2 = AudioSegment.from_file(self.filepath2[0])
            combined = sound1.overlay(sound2)
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

    def hash_file(self, peaks):

        h1 = hashlib.sha1()
        h2 = hashlib.sha1()

        if self.check_1:
            h1.update(peaks)
            self.hashResult1 = h1.hexdigest()

        if self.check_2:
            h2.update(peaks)
            self.hashResult2 = h2.hexdigest()

        if self.hashResult1 and self.hashResult2:
            if self.hashResult1 == self.hashResult2:
                print("Both songs are the same")
                m = int(self.hashResult1, 16)
                n = int(self.hashResult2, 16)
                resutlt = (n / m) * 100
                print('\nHash:', resutlt)
            else:
                print("Two different songs")
                m = int(self.hashResult1, 16)
                n = int(self.hashResult2, 16)
                resutlt = (n / m) * 100
                print('\nHash:', resutlt)

    def get_wav_info(self, wav_file):
        wav = wave.open(wav_file, 'r')
        frames = wav.readframes(-1)
        self.sound_info = pylab.fromstring(frames, 'Int16')
        self.frame_rate = wav.getframerate()
        wav.close()
        return self.sound_info, self.frame_rate

    def spectrogramFunc(self):
        if self.check_1 == True:
            self.sound_info, self.frame_rate = self.get_wav_info(
                self.filepath1[0])
            self.sound_info = self.sound_info[0:60*self.frame_rate]
            self.spectrogramArray_1 = pylab.specgram(
                self.sound_info, Fs=self.frame_rate)
            self.plottingSpectrogram(self.spectrogramArray_1)
            self.getPeaksData(self.spectrogramArray_1)

    def plottingSpectrogram(self, spectrogramArray):
        pylab.figure(num=None, figsize=(19, 12))
        pylab.style.use('dark_background')
        plotting = pylab.subplot(111, frameon=False)
        plotting.get_xaxis().set_visible(False)
        plotting.get_yaxis().set_visible(False)
        spectrogramArray = pylab.specgram(
            self.sound_info, Fs=self.frame_rate)
        pylab.savefig('spectrogram_1.jpg', bbox_inches='tight')
        imgArr = cv2.imread('spectrogram_1.jpg')
        img = pg.ImageItem(imgArr)
        img.rotate(270)
        self.ui.plottingGraph.clear()
        if self.ui.comboBox.currentText() == "Browsed audio":
            self.ui.plottingGraph.addItem(img)

        if self.ui.comboBox.currentText() == "Recorded Audio":
            print("NOTHING")

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
        directory = os.getcwd() + '\Database'
        for filename in os.listdir(directory):
            if filename.endswith(".wav") or filename.endswith(".mp3"):
                self.databaseSongs = os.path.join(directory, filename)
                self.spectrogramDatabase(self.databaseSongs)
                self.compare(filename)
            else:
                print('No Data required')

    def compare(self, filename):
        hashBrowse = int(self.hashResult1, 16)
        hashForDatabase = int(self.hashDatabase, 16)
        result = (hashForDatabase / hashBrowse)*100
        if (result >= 70.0):
            print("-----")
            print(filename)
            print("Hash:", result)
            self.ui.soundRecogniserOuput.setText(filename)
            self.stylingOutput(self.ui.soundRecogniserOuput)
            self.ui.soundRecogniserOuput_2.setText(str(result))
            self.stylingOutput(self.ui.soundRecogniserOuput_2)
            print("TAMAM EL KALAM")
            print("-----")
            return
        else:
            print("-----")
            print(filename)
            print("Hash:", result)
            print("Msh TMAM")
            print("-----")

    def stylingOutput(self, outputBrowser):
        outputBrowser.setStyleSheet(
            "color:rgb(255, 255, 255);")
        outputBrowser.setFont(
            QtGui.QFont("Times", 50, QtGui.QFont.Bold))

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


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
