#!/usr/bin/env python

from __future__ import print_function
import glob
import os
import time
from datetime import datetime

save_data_dir = '/mnt/media/temps'

# These may not be right as of late 2020, but they don't seem to hurt
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    """Example device output:
    $ cat /sys/bus/w1/devices/28-0000013afdee/w1_slave
    ef 00 4b 46 7f ff 01 10 c8 : crc=c8 YES
    ef 00 4b 46 7f ff 01 10 c8 t=14937"""
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f


def mydate():
    return datetime.now().strftime("%y-%m-%d")


while True:
    start_date = mydate()
    filename = os.path.join(save_data_dir, f"thermo-{start_date}.dat")
    file_already_existed = os.path.isfile(filename)
    with open(filename, 'a') as fd:
        # We only want a header on the first line
        if not file_already_existed:
            print("Date,C,F")
        date = mydate()
        while date == start_date:
            # There is a race condition -- now() can change after we
            # checked the date.  I don't care.
            c, f = read_temp()
            print(c, f)
            now = str(datetime.now())[0:19]
            csv = f'{now}, {c}, {f}'
            print(csv)
            print(csv, file=fd)
            fd.flush()
            time.sleep(30)
            date = mydate()
