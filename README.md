# A Super Simple and Lightweight Temperature Recording System

I wrote this because I couldn't find a very simple temperature recording and displaying system.  Everything else required big software installs, typically a database, and/or heavyweight graphical display software.

There are two parts:

- Reading and Saving Temperatures: `thermo-daemon.py`

This is done on a Raspberry Pi (although most cheap single-board
computers running GNU/Linux will work fine) using a cheap digital
sensor, a DS18B20.  The temperature is taken and recorded every 10
minutes, and saved to a daily file.  New daily files are started just
after midnight.  Simplye leave `thermo-daemon.py` running
continuously.  If it dies (say, due to a power outage), you can safely
start a new instance and it'll append to the correct daily data file.

- Displaying Temperature History on a Graph: `plot-many-days.py`

The graphing program reads all the daily files and plots them using
plotly, which lets you zoom in on particular ranges such as a single
day.

It's currently GPLv3 licensed, because it was handy.  I'd consider an
attribution-only license as well.

I welcome suggestions.
