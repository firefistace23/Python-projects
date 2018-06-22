#!/bin/bash
echo "Sample array program "
echo "Input three names"
for (( i = 0 ; i < 3 ; i++ ))
do
read students[$i]
done

echo -n  ${students[*]} " "

