A Super Simple Temperature Recording System

There are two parts:

# Reading and Saving Temperatures.
This is currently done on a Raspberry Pi using a cheap digital sensor, a DS18B20.  A temperature is taken and recorded every 10 minutes, and saved to a daily file.  New daily files are started just after midnight.  This is `thermo-daemon.py`


# Displaying them on a graph
The graphing program reads all the daily files and plots them using plotly, which lets you zoom in on particular ranges such as a single day.  This is `plot-many-days.py`.

It's currently GPLv3 licensed, but that's mainly because it was handy.  I'd consider an attribution-only license as well.

I welcome suggestions.
