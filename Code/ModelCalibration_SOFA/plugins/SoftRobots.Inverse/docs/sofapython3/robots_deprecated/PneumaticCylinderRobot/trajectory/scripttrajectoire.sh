#!/bin/sh

#include<math.h>
x=0.0;
y=0.0;
angle=0.0;
t=0.0;
for t in `seq -w 0.0 0.01 0.5`;
do
	echo "T= $t\n  X= $x $y 110" >> ../../projet/Sofa/Build/trajectoire.ws
	x=$(echo "$x + 0.22" | bc -l);
done

for t in `seq -w 0.5 0.01 2.0`;
do
	echo "T= $t\n  X= $x $y 110" >> ../../projet/Sofa/Build/trajectoire.ws
	x=$(echo "c($angle)*13" | bc -l);
	y=$(echo "s($angle)*13" | bc -l);
	angle="$angle + 0.04906";
done

for t in `seq -w 2.01 0.01 3.5`;
do
	echo "T= $t\n  X= $x $y 110" >> ../../projet/Sofa/Build/trajectoire.ws
	x=$(echo "c($angle)*13" | bc -l);
	y=$(echo "s($angle)*13" | bc -l);
	angle="$angle + 0.04906";
done
