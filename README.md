# LiveSensorPlot
Plots data from stdin using PyQtGraph. This can be used in conjunction with https://github.com/vrublack/GY-85.

# Usage on same system as sensors
For example, we can tell the GY-85 script to write every 10th sample to stdout and then pipe that to the live plot:
```
python GY-85/main.py --stdout -nth 10 |python LiveSensorPlot/main.py
```

# Usage with sensors on remote host
If the sensors are read on a remote host, like a Raspberry Pi, you can use SSH to pipe the data into the live plot:
```
ssh [user:host] 'python GY-85/main.py --stdout -nth 10' |python LiveSensorPlot/main.py
```
