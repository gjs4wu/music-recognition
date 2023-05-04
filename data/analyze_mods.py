#!/usr/bin/env python3

filenames = [ "clair_de_lune", "green_light", "jolene", "la_vie_en_rose", "money_machine", "novacane", "rhyme_dust", "the_chain"]

file_logs : dict[str, dict[int, list[str]]] = {
    "clair_de_lune": {}, 
    "green_light": {}, 
    "jolene": {}, 
    "la_vie_en_rose": {}, 
    "money_machine": {}, 
    "novacane": {}, 
    "rhyme_dust": {}, 
    "the_chain": {}, 
    }

trim = {"correct": 0, "incorrect": 0, "none": 0}
quiet = {"correct": 0, "incorrect": 0, "none": 0}
loud = {"correct": 0, "incorrect": 0, "none": 0}
echo = {"correct": 0, "incorrect": 0, "none": 0}
noise = {"correct": 0,"incorrect": 0, "none": 0}

noises : dict[str, dict[str : int]] = {}

def parse_data_log():
    for filename in filenames:
        with open("data/" + filename + "/results_1000.txt") as f:
            lines = f.readlines()

            i = 0
            for line in lines:
                mods = line.split(":")[1].replace(" ", "").replace("\n", "").split(",")
                mods.remove("")
                
                file_logs[filename][i] = mods
                i += 1

def count_mods():

    for tool in range(2):

        for filename, log in file_logs.items():

            if tool == 0:
                path = "shazam/" + filename + "_results.txt"
            else:
                path = "acr/" + filename + "/results.txt"
            with open(path) as f:
                lines = f.readlines()

                correct_str = lines[0].split("[")[1].split("]")[0].replace(" ", "").split(",")
                correct : list[int] = [0] * len(correct_str)
                for i in range(len(correct_str)):
                    correct[i] = int(correct_str[i])

                incorrect_str = lines[1].split("[")[1].split("]")[0].replace(" ", "").split(",")
                incorrect : list[int] = [0] * len(incorrect_str)
                for i in range(len(incorrect_str)):
                    incorrect[i] = int(incorrect_str[i])

                no_song_str = lines[2].split("[")[1].split("]")[0].replace(" ", "").split(",")
                try:
                    no_song_str.remove("")
                except:
                    ""
                no_song : list[int] = [0] * len(no_song_str)
                for i in range(len(no_song_str)):
                    no_song[i] = int(no_song_str[i])


                for result, arr in [["correct", correct], ["incorrect", incorrect], ["none", no_song]]:
                    for i in arr:
                        mods = log[i]

                        if mods.count("trim") > 0 :
                            trim[result] += 1
                        if mods.count("quiet") > 0:
                            quiet[result] += 1
                        if mods.count("loud") > 0:
                            loud[result] += 1
                        if mods.count("echo") > 0:
                            echo[result] += 1
                        
                        wav = False
                        for mod in mods:
                            if mod.find(".wav") != -1:
                                if not wav:
                                    noise[result] += 1
                                    wav = True
                                                
                                curr = noises.get(mod)
                                if curr == None:
                                    new = {"correct": 0,"incorrect": 0, "none": 0}
                                    new[result] += 1
                                    noises.update({mod: new})
                                else:
                                    curr[result] += 1
                                    noises.update({mod: curr})

        


parse_data_log()
count_mods()

print(trim)
print(quiet)
print(loud)
print(echo)
print(noise)
for key, val in noises.items():
    print(key, val["correct"], val["incorrect"], val["none"])
