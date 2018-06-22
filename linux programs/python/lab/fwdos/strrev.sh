#!/bin/bash
st="shaun"
echo ${st:1:1}
len=${#st}
for (( i=$len-1 ; i>=0 ; i--))
do
reverse="$reverse${st:$i:1}"
done
echo $reverse
