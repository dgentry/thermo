set terminal dumb
set xrange [0:20]
set yrange [0:400]
plot "/mnt/media/temps/thermo-2020-08-25.dat" using 1:2 with lines
pause 1
reread
