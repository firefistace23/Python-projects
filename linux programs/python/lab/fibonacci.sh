#!/bin/sh
echo "Fibonacci series"
i=0
j=1
echo $i
echo $j
k=0
m=10
while [ $k -le $m ]
do
k=$(($i+$j))
echo $k
i=$j
j=$k
done
