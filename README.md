# Fuzzing Song Recognition Tools 

# Setup

To download all necessary packages and tools, run `setup.sh`. I used Python 3.10, but I think it should work with Python 3.8 and later


# Generating noisy audio samples

There are 8 songs for which I have generated samples, each of which has its own folder in the /data folder. Each song starts with 1 sample, a 15-second unmodified clip from the target song, which can be found at both sample.wav and /inputs/0000.wav in each song folder.  

## Generate samples for a songs
To generate modified, noisy audio samples, run from the /data folder:
```
./run.py <path/to/song_folder> <# of samples to generage>
```

example:
```
./run.py ./novacane/ 1000
```
For my evaluation I generated 1000 samples for each song, but for testing I don't recommend generating that many as it takes awhile.
<br></br>

There are 5 types of audio manipulations that are performed:
* Trim: Shorten the length of the sample by 1 second
* Quiet: Decrease the volume
* Loud: Increase the volume
* Echo: Add an echo to the sample
* Noise: Combine the audio sample with one of the real-world noise audio samples from /noises

The function picks a random sample from the /inputs folder and adds a random audio manipulation, then adds the new sample back to the /inputs folder, and repeats. This generates a large number of inputs with multiple audio modifications in different combinations. 

The series of modifications for each sample is recorded in results.txt in each song folder. The results from the evaluation of 1000 samples are in the results_1000.txt files.
<br></br>

#### *NOTE: For the first 20 audio samples, only the TRIM modification is performed. This is because if major modifications (adding very loud background noise) are added early on, then almost all generated samples will have that modification, decreasing the variety. If you are generating a much lower number of samples, decrease the FIRST_TRIM variable at the top of `data/run.py` to # of samples/50 *

<br></br>
If you wish to clear all generated noisy inputs for a song, run

```
clean_inputs.sh <path/to/folder>
```
<br></br>

# Shazam Music Identification 

I am using the Shazamio which is a reverse engineered Shazam API

## Single song query
To run Shazam on a single audio file (.wav, .mp3, etc.):
```
./run.py <path/to/audio_file>
```

example:
```
./shazam/run.py ./data/novacane/sample.wav
```

## Test all noisy inputs for single song
To run Shazam on set of noisy data samples:
```
./shazam/test_inputs.py <name of song folder in> <correct song name> <# of samples to test>
```

example:
```
./shazam/test_inputs.py green_light 'Green Light' 100
```

Pass in the number of noisy samples you generated for the song in the first section. 

*NOTE: If you are testing a low number of samples, Shazam may correctly identify all samples, depending on which song you are testing*


## Test all noisy inputs for all songs

To run Shazam on all noisy audio sets for all 8 songs:

```
./run_all_shazam.sh <# of samples to test for each>
```

*If runnning this make sure you have generated samples for all songs*

Results from each song are available in `./shazam/<song_name>_results.txt`
<br></br>


# ACRCloud Music Identification 

I am using the ACRCloud Python SDK (https://github.com/acrcloud/acrcloud_sdk_python)

I have a 2 week free trial, giving me enough audio recognition requests to identify 1000 samples for each of the 8 songs. I have left my access key and secret in the `run.py` and `test_inputs.py` so that you can test it, but if you try to run a large amount of queries, it will run out. 
<br></br>
## Single song query

To run ACRCloud on a single audio file:
```
./acr/run.py <path/to/audio_file>
```

## Test all noisy inputs for single song

To run ACRCloud on set of noisy data samples:
```
./acr/test_inputs.py <name of song folder> <correct song name> <# of samples to test>
```

example:
```
./acr/test_inputs.py green_light 'Green Light' 100
```

Pass in the number of noisy samples you generated for the song in the first section. 

*NOTE: If you are testing a low number of samples, ACR may correctly identify all samples, depending on which song you are testing*

## Test all noisy inputs for all songs

To run ACRCloud on all noisy audio sets for all 8 songs:

```
./run_all_acr.sh
```

*If runnning this make sure you have generated samples for all songs*

Results from each song are available in `./acr/<song_name>/results.txt`
<br></br>

# AcoustID

AcoustID is free and not rate-limited or query limited, so I have left my API key in the acoustID files so they should run without a problem. 

## Single song query

To run AcoustID on a single audio file:
```
./acoustid/run.py <path/to/audio_file>
```

## Test all noisy inputs for single song

To run ACRCloud on set of noisy data samples:
```
./acoustid/test_inputs.py <name of song folder> <correct song name> <# of samples to test>
```

example:
```
./acoustid/test_inputs.py green_light 'Green Light' 100
```

Pass in the number of noisy samples you generated for the song in the first section. 

## Test all noisy inputs for all songs

To run ACRCloud on all noisy audio sets for all 8 songs (this will take a very very long while):

```
./run_all_acoustid.sh
```

*If runnning this make sure you have generated samples for all songs*

Results from each song are available in `./acoustid/<song_name>_results.txt`
<br></br>


# Analysis

You can run the `data/analyze_mods.py` file to see how different audio modifications affect each tool (figure 3 in the report)

The song specific results are available in the results.txt files in the 3 tool folders. 
The sample modification logs are available in the results.txt files in the 8 song folders.