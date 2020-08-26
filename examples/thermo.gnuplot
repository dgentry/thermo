#set term png
#set output '| open png:-'

set term dumb

set datafile separator ","
set title "Temperature"
set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor rgb"grey" behind
set ylabel "ºF"
set xdata time
set timefmt "%s"
set format x "%H:%M"
#set timefmt "%m/%d/%y %H:%M"
set key left top
set grid
plot "thermo.dat" using ($1+(-7*3600)):2 with lines lw 2 lt 3 title 'temperature'
pause 1
reread
