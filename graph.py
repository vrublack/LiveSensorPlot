import pyqtgraph
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from data_point import DataPoint
import sys


class Plot:
    def __init__(self, p, label, unit):

        # 3) Plot in chunks, adding one new plot curve for every 100 samples
        self.chunkSize = 100000
        # Remove chunks after we have 10
        self.maxChunks = 100
        self.last_time = -1

        self.plot = p
        self.plot.setLabel('bottom', label, unit)
        self.plot.setXRange(-10000, 0)
        self.curves = []
        self.data = np.empty((self.chunkSize + 1, 2))
        self.ptr = 0

    def update(self, x, y):
        for c in self.curves:
            c.setPos(-self.last_time, 0)

        i = self.ptr % self.chunkSize
        if i == 0:
            curve = self.plot.plot()
            self.curves.append(curve)
            last = self.data[-1]
            data5 = np.empty((self.chunkSize + 1, 2))
            data5[0] = last
            while len(self.curves) > self.maxChunks:
                c = self.curves.pop(0)
                self.plot.removeItem(c)
        else:
            curve = self.curves[-1]
        self.data[i, 0] = x
        self.data[i, 1] = y
        self.last_time = x
        curve.setData(x=self.data[:i + 1, 0], y=self.data[:i + 1, 1])
        self.ptr += 1


class Graph:
    def __init__(self, next_sample):
        self.win = pg.GraphicsWindow()
        self.win.setWindowTitle('HMI Sensors')
        self.next_sample = next_sample

        self.acc_x = Plot(self.win.addPlot(colspan=2), 'Acc x', 'g-force')
        self.win.nextRow()
        self.acc_y = Plot(self.win.addPlot(colspan=2), 'Acc y', 'g-force')
        self.win.nextRow()
        self.acc_z = Plot(self.win.addPlot(colspan=2), 'Acc z', 'g-force')

    # update all plots
    def update(self):
        sample = self.next_sample()
        self.acc_x.update(sample.time, sample.x)
        self.acc_y.update(sample.time, sample.y)
        self.acc_z.update(sample.time, sample.z)

    def start(self):
        timer = pg.QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(1)

        ## Start Qt event loop unless running in interactive mode or using pyside.
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()