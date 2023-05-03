#!/bin/bash

if [ $# -eq 0 ]; then
    >&2 echo "Number of samples to generate not provided"
    exit 1
fi

./run.py clair_de_lune $1
./run.py green_light $1
./run.py jolene $1
./run.py la_vie_en_rose $1
./run.py money_machine $1
./run.py novacane $1
./run.py rhyme_dust $1
./run.py the_chain $1