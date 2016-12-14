import numpy as np
import matplotlib.pyplot as plt
import sys

from data_point import DataPoint


def read_file(filename):
    acc = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:  # skip header
            p = DataPoint.from_str(line)
            if p is not None and p.sensor_type == 'acc':
                acc.append(p)
    return acc


acc = read_file(sys.argv[1])

acc_x = [s.x for s in acc]
acc_y = [s.time for s in acc]

fig = plt.figure(figsize=(15, 9))

axes = fig.add_subplot(111)
axes.set_title("Accelerometer")
axes.set_autoscaley_on(False)
axes.set_ylim([-1, 1])
axes.set_xlim([0, 1000])
axes.plot(acc_y, acc_x)

plt.show()
