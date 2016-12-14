import numpy as np
import matplotlib.pyplot as plt
import sys

from data_point import DataPoint

fig = plt.figure(figsize=(15, 9))

axes = fig.add_subplot(111)
axes.set_title("Accelerometer")
axes.set_autoscaley_on(False)
axes.set_ylim([-1, 1])
axes.set_xlim([0, 100000])
plt.ion()

plt.show()


count = 0
for line in sys.stdin:
    p = DataPoint.from_str(line)
    if p is not None and p.sensor_type == 'acc':
        axes.scatter(p.time, p.x)
        if count % 100 == 0:
            plt.pause(0.05)
        count += 1

print('Done')