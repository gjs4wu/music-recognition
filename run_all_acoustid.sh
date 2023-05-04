#!/bin/bash

if [ $# -eq 0 ]; then
    >&2 echo "Number of tests to run not provided"
    exit 1
fi

./acoustid/test_inputs.py clair_de_lune 'Clair de lune' $1
./acoustid/test_inputs.py green_light 'Green Light' $1
./acoustid/test_inputs.py jolene Jolene $1
./acoustid/test_inputs.py la_vie_en_rose 'La Vie En Rose' $1
./acoustid/test_inputs.py money_machine 'money machine' $1
./acoustid/test_inputs.py novacane 'Novacane' $1
./acoustid/test_inputs.py rhyme_dust 'Rhyme Dust' $1
./acoustid/test_inputs.py the_chain 'The Chain' $1