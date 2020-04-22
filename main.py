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
        self.filepath1 = QtWidgets.QFileDialog.getOpenFileName()
        self.ui.graphicsView.clear()
        for i in self.filepath1:
            ext = os.path.splitext(i)[-1].lower()
            print(ext)
            if ext == ".wav":
                samplerate, self.y = wavfile.read(self.filepath1[0])
                self.x = np.arange(len(self.y))/float(samplerate)

                noise_power = 0.01 * (self.samplerate) / 2
                mod = 500*np.cos(2*np.pi*0.25*(self.x))
                carrier = np.sin(2*np.pi*3e3*(self.x) + mod)
                noise = np.random.normal(scale=np.sqrt(
                    noise_power), size=(self.x).shape)
                noise *= np.exp(-(self.x)/5)
                x_axis = carrier + noise
                f, t, Sxx = signal.spectrogram(x_axis, self.samplerate)

                # Item for displaying image data
                img = pyqtgraph.ImageItem()
                self.ui.graphicsView.addItem(img)
                hist = pyqtgraph.HistogramLUTItem()
                hist.setImageItem(img)
                self.ui.graphicsView.addItem(hist)
                self.ui.graphicsView.show()
                hist.setLevels(np.min(Sxx), np.max(Sxx))
                hist.gradient.restoreState(
                    {'mode': 'rgb',
                     'ticks': [(0.5, (0, 182, 188, 255)),
                               (1.0, (246, 111, 0, 255)),
                               (0.0, (75, 0, 113, 255))]})
                img.setImage(Sxx)
                img.scale(t[-1]/np.size(Sxx, axis=1),
                          f[-1]/np.size(Sxx, axis=0))
                self.ui.graphicsView.setLimits(
                    xMin=0, xMax=t[-1], yMin=0, yMax=f[-1])
                self.ui.graphicsView.setLabel('bottom', "Time", units='s')
                self.ui.graphicsView.setLabel('left', "Frequency", units='Hz')
                print("ESHTAA")

    def browse2(self):
        self.filepath2 = QtWidgets.QFileDialog.getOpenFileName()

    def play1(self):
        winsound.PlaySound(self.filepath1[0], winsound.SND_FILENAME)
        # winsound.PlaySound(self.filepath2[0], winsound.SND_FILENAME)

    def spectrogramFunc(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
