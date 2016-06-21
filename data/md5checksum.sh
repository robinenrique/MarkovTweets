#!/bin/bash

i = 0

	while read line
do
	((line+4))
	echo $line
done < $1
