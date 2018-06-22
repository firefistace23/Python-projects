#!/bin/bash

echo "Enter a Number "
read n
a=0
b=1
c=0
i=2
echo "Fibonacci Series"
echo -n $a" "$b" "
while [ $i -lt $n ]
do
c=$(($a+$b))
a=$b
b=$c
i=$(($i+1))
echo -n " "$c" "
done
echo ""
