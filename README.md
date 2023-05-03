## Generating noisy audio samples




## Shazam Music Identification 

I am using the Shazamio which is a reverse engineered Shazam API


#### Single song query
To run Shazam on a single audio file (.wav, .mp3, etc.):
```
./run.py <path/to/audio_file>
```

example:
```
./shazam/run.py ./data/novacane/sample.wav
```


#### Test all noisy inputs for single song
To run Shazam on set of (1000) noisy data samples (this will take awhile):
```
./shazam/test_inputs.py <name of song folder in ./data (i.e. 'la_vie_en_rose')> <correct song name (i.e. 'La Vie En Rose')>
```

```
./shazam/test_inputs.py green_light 'Green Light'
```

If you want to change the number of samples it runs on change the START and/or END variables in test_inputs.py


#### Test all noisy inputs for all songs

To run Shazam on all noisy audio sets for all 8 songs (this will take a very very long while):

Run `./run_all_shazam.sh`


Results from each song are available in `./shazam/<song_name>_results.txt`


## ACRCloud Music Identification 

I am using the ACRCloud Python SDK (https://github.com/acrcloud/acrcloud_sdk_python)

I have a 2 week free trial, giving me enough audio recognition requests to identify 1000 samples for each of the 8 songs. I have left my access key and secret in the `run.py` and `test_inputs.py` so that you can test it, but if you try to run a large amount of queries, it will quickly run out. 

#### Single song query

To run ACRCloud on a single audio file:
```
./acr/run.py <path/to/audio_file>
```

#### Test all noisy inputs for single song

To run ACRCloud on set of (1000) noisy data samples (this will take awhile):
```
./acr/test_inputs.py <name of song folder in ./data (i.e. 'la_vie_en_rose')> <correct song name (i.e. 'La Vie En Rose')>
```

```
./acr/test_inputs.py green_light 'Green Light'
```

If you want to change the number of samples it runs on change the START and/or END variables in test_inputs.py



#### Test all noisy inputs for all songs

To run ACRCloud on all noisy audio sets for all 8 songs (this will take a very very long while):

Run `./run_all_acr.sh`


Results from each song are available in `./acr/<song_name>/results.txt`


## AcoustID


