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
from skimage.feature import peak_local_max
from playsound import playsound
import operator


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
        self.IDX_FREQ_I = 0
        self.IDX_TIME_J = 1
        self.MIN_HASH_TIME_DELTA = 0
        self.MAX_HASH_TIME_DELTA = 200
        self.DEFAULT_FAN_VALUE = 15

        self.check_1 = False
        self.check_2 = False

        self.iterationDatabase()

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
        print("Awel ESHTAAA")

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
        print("Tany ESHTAAA")

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

    def hash_file(self, peaks, fan_valu):
        for i in range(len(peaks)):
            for j in range(1, fan_value):
                if (i + j) < len(peaks):

                    freq1 = peaks[i][self.IDX_FREQ_I]
                    freq2 = peaks[i + j][self.IDX_FREQ_I]
                    t1 = peaks[i][self.IDX_TIME_J]
                    t2 = peaks[i + j][self.IDX_TIME_J]
                    t_delta = t2 - t1

                if t_delta >= self.MIN_HASH_TIME_DELTA and t_delta <= self.MAX_HASH_TIME_DELTA:
                    h = hashlib.sha1(
                        "%s|%s|%s" % (str(freq1), str(freq2), str(t_delta)))
                    yield (h.hexdigest()[0:FINGERPRINT_REDUCTION], t1)

    def get_wav_info(self, wav_file):
        wav = wave.open(wav_file, 'r')
        frames = wav.readframes(-1)
        sound_info = pylab.fromstring(frames, 'Int16')
        frame_rate = wav.getframerate()
        wav.close()
        return sound_info, frame_rate

    def spectrogramFunc(self):
        if self.check_1 == True:
            sound_info, frame_rate = self.get_wav_info(self.filepath1[0])
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
            sound_info, frame_rate = self.get_wav_info(self.filepath2[0])
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
            # sig, rate = librosa.load(
            #     self.filepath2[0], sr=None, offset=10, duration=15)
            # spectrogram = librosa.feature.melspectrogram(y=sig, sr=rate)
            # spec_shape = spectrogram.shape
            # fig = plt.figure(figsize=(spec_shape), dpi=8)
            # librosa.display.specshow(spectrogram.T)
            # plt.tight_layout()
            # plt.savefig("specttt.jpg")

    def getPeaksData(self, spectrogramArray):
        print("spectro-gram Array is:")
        print(spectrogramArray[0])
        peaks, time_diff = find_peaks(((spectrogramArray)[0])[
            0], distance=150)
        print("peaks are:")
        print(peaks)
        pylab.plot(((spectrogramArray)[0])[0])
        pylab.plot(peaks, (((spectrogramArray)[0])[0])[peaks], "x")
        pylab.plot(np.zeros_like(
            ((spectrogramArray)[0])[0]), "--", color="red")

        fingerprint = self.hash_file(peaks, self.DEFAULT_FAN_VALUE)
        print("fingerprint:")
        print("   ")
        print(fingerprint)

    def spectrogramDatabase(self, file):
        sound_info, frame_rate = self.get_wav_info(file)
        pylab.figure(num=None, figsize=(19, 12))
        pylab.style.use('dark_background')
        plotting = pylab.subplot(111, frameon=False)
        plotting.get_xaxis().set_visible(False)
        plotting.get_yaxis().set_visible(False)
        databaseSpecrtoArray = pylab.specgram(
            sound_info, Fs=frame_rate)
        self.getPeaksData(databaseSpecrtoArray)
        pylab.savefig('database.jpg', bbox_inches='tight')

    def iterationDatabase(self):
        directory = r'C:/Users/DELL/Desktop/DSP_Task4/Database/'
        for filename in os.listdir(directory):
            if filename.endswith(".wav") or filename.endswith(".mp3"):
                songs = os.path.join(directory, filename)
                print(songs)
                self.spectrogramDatabase(songs)
                return
                # haha = directory+filename
                # print(haha)
                # playsound(haha)
                # sorteArray = sorted(songs.items(),key=operator.itemgetter(1))
                # print(sort)
            else:
                print('No Data required')


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
