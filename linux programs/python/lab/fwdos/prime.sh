#!/bin/bash

echo "Prime check"
echo -n "Enter the number:" 
read num
j=$num/2
flag=1
for (( i=2 ; i <= $j ; i++ ))
do
if [ $(($num % $i)) -eq 0 ]
then
flag=0
fi
done
if [ $flag -eq 1 ]
then
echo "Prime"
else
echo "Not Prime"
fi

