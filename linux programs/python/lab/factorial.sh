#!/bin/sh
echo "En/ter the number whosw factorial is to be found out"
read num
i=1
fact=1
while [ $i -le $num ]
do
fact=$(($fact*$i))
i=$(($i+1))
done 
echo $fact
