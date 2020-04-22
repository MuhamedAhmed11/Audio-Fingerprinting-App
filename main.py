from PyQt5 import QtWidgets
from mainWindow import Ui_MainWindow
import sys
import winsound
from scipy import signal
from scipy.fftpack import fftshift
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.io import wavfile
import pyqtgraph
import os
from pydub import AudioSegment
import hashlib
import librosa
import librosa.display
import wave
import pylab


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.playButton.clicked.connect(self.play1)
        self.filepath1 = []
        self.filepath2 = []
        self.ui.browseButton.clicked.connect(self.browse1)
        self.ui.browseButton2.clicked.connect(self.browse2)
        self.ui.pushButton.clicked.connect(self.spectrogramFunc)
        self.samplerate = 47000.6
        self.x = []
        self.y = []

    def browse1(self):
        self.filepath1 = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                                               'DSP_Task4\Database', "Song files (*.wav *.mp3)")
        self.ui.graphicsView.clear()
        self.hash_file()
        self.spectrogramFunc()

        # y, sr = librosa.load(self.filepath1[0],
        #                      offset=10, duration=15)
        # chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr,
        #                                           n_chroma=12, n_fft=4096)
        # chroma_cq = librosa.feature.chroma_cqt(y=y, sr=sr)
        # hehe = np.asfortranarray(chroma_stft)
        # librosa.display.specshow(chroma_stft, y_axis='chroma', x_axis='time')
        # plt.colorbar()
        # plt.tight_layout()
        # plt.show()

        # self.ui.graphicsView.plotItem(haha)

        # for i in self.filepath1:
        #     ext = os.path.splitext(i)[-1].lower()
        #     print(ext)
        #     if ext == ".wav":
        #         samplerate, self.y = wavfile.read(self.filepath1[0])
        #         self.x = np.arange(len(self.y))/float(samplerate)

        #         noise_power = 0.01 * (self.samplerate) / 2
        #         mod = 500*np.cos(2*np.pi*0.25*(self.x))
        #         carrier = np.sin(2*np.pi*3e3*(self.x) + mod)
        #         noise = np.random.normal(scale=np.sqrt(
        #             noise_power), size=(self.x).shape)
        #         noise *= np.exp(-(self.x)/5)
        #         x_axis = carrier + noise
        #         f, t, Sxx = signal.spectrogram(x_axis, self.samplerate)

        #         # Item for displaying image data
        #         img = pyqtgraph.ImageItem()
        #         self.ui.graphicsView.addItem(img)
        #         hist = pyqtgraph.HistogramLUTItem()
        #         hist.setImageItem(img)
        #         self.ui.graphicsView.addItem(hist)
        #         self.ui.graphicsView.show()
        #         hist.setLevels(np.min(Sxx), np.max(Sxx))
        #         hist.gradient.restoreState(
        #             {'mode': 'rgb',
        #              'ticks': [(0.5, (0, 182, 188, 255)),
        #                        (1.0, (246, 111, 0, 255)),
        #                        (0.0, (75, 0, 113, 255))]})
        #         img.setImage(Sxx)
        #         img.scale(t[-1]/np.size(Sxx, axis=1),
        #                   f[-1]/np.size(Sxx, axis=0))
        #         self.ui.graphicsView.setLimits(
        #             xMin=0, xMax=t[-1], yMin=0, yMax=f[-1])
        #         self.ui.graphicsView.setLabel('bottom', "Time", units='s')
        #         self.ui.graphicsView.setLabel('left', "Frequency", units='Hz')
        print("ESHTAAA")

    def browse2(self):
        self.filepath2 = QtWidgets.QFileDialog.getOpenFileName()

    def play1(self):
        sound1 = AudioSegment.from_file(self.filepath1[0])
        sound2 = AudioSegment.from_file(self.filepath2[0])
        combined = sound1.overlay(sound2)
        combined.export(r"C:\Users\DELL\Desktop\combined2.wav", format='wav')
        winsound.PlaySound(
            r"C:\Users\DELL\Desktop\combined2.wav", winsound.SND_FILENAME)

    def hash_file(self):

        # make a hash object
        h = hashlib.sha1()

        # open file for reading in binary mode
        with open(self.filepath1[0], 'rb') as file:
            # loop till the end of the file
            chunk = 0
            while chunk != b'':
                # read only 1024 bytes at a time
                chunk = file.read(1024)
                h.update(chunk)

        # return the hex representation of digest
        hashResult = h.hexdigest()
        print(hashResult)

    def spectrogramFunc(self):
        sound_info, frame_rate = self.get_wav_info(self.filepath1[0])
        pylab.figure(num=None, figsize=(19, 12))
        pylab.subplot(111)
        spect = pylab.specgram(sound_info, Fs=frame_rate)
        pylab.savefig('spectrogram.png')

        print(spect)
        print(spect[0])

    def get_wav_info(self, wav_file):
        wav = wave.open(wav_file, 'r')
        frames = wav.readframes(-10)
        sound_info = pylab.fromstring(frames, 'Int16')
        frame_rate = wav.getframerate()
        wav.close()
        return sound_info, frame_rate


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
