#!/bin/bash

echo "Program to find factorial of  number"
echo -n "Enter a number :"
read num
n=$num
fact=1
while [ $n -gt 0 ]
do
fact=$(($fact*$n))
n=$(($n-1))
done
echo -n "Factorial of $num = $fact"
echo " "
