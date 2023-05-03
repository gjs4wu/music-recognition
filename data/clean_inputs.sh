#!/bin/bash

if [ $# -eq 0 ]; then
    >&2 echo "No arguments provided"
    exit 1
fi



rm $1/inputs/*
cp $1/sample.wav $1/inputs/0000.wav