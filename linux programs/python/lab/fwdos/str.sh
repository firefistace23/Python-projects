#!/bin/bash
echo "Panlidrome check "
echo -n "Enter a word "
read word
echo -n "Reverse of the word :"
reverse=$(($word | rev))
echo $reverse

