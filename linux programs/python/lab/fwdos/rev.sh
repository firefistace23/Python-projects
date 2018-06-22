#!/bin/bash
echo "Palindrome check"
echo -n "Input number :"
read num
n=$num
rev=0
while [ $n -gt 0 ]
do
rem=$(($n%10))
rev=$(($rev*10+rem))
n=$(($n/10))
done
echo $rev
if [ $num -eq $rev ]
then
echo Palindrome
else
echo No
fi
