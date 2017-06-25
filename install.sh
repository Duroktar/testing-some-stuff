#!/usr/bin/env bash

for dir in `ls ${PWD##*/}`;
do
    for subdir in `ls ${PWD##*/}/$dir`;
    do
      npm install;
    done
done
