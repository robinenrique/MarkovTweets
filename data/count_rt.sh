#!/bin/bash

while read p; do
    cat $2 | grep -i $p | wc -l
done <$1

