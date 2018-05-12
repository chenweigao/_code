#!/bin/bash
count=1
cat words.txt | while read line
do
    # echo "Line $count: $line"
    #count=$[ $count + 1 ]
    for word in $line
    do    
        echo $word
    done
done
