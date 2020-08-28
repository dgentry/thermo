# A Super Simple and Lightweight Temperature Recording System

I wrote this because I couldn't find a very simple temperature recording and displaying system.  Everything else required big software installs, typically a database, and/or heavyweight graphical display software.

There are two parts:

- Reading and Saving Temperatures.
This is done on a Raspberry Pi (although most cheap single-board computers running GNU/Linux will work fine) using a cheap digital sensor, a DS18B20.  The emperature is taken and recorded every 10 minutes, and saved to a daily file.  New daily files are started just after midnight.  The program that does this is `thermo-daemon.py`, which you should leave running continuously.  If it dies (say, due to a power outage), you can safely start a new instance and it'll append to the correct daily data file.

- Displaying them on a graph
The graphing program reads all the daily files and plots them using plotly, which lets you zoom in on particular ranges such as a single day.  This program is `plot-many-days.py`.

It's currently GPLv3 licensed, but that's mainly because it was handy.  I'd consider an attribution-only license as well.

I welcome suggestions.
