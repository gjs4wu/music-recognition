#!/usr/bin/env python3.10

filenames = [ "clair_de_lune", "green_light", "jolene", "la_vie_en_rose", "money_machine", "novacane", "rhyme_dust", "the_chain"]

shazam : dict[str, dict[int, list[int]]] = {
    "clair_de_lune": {"correct": [], "incorrect": [], "none": []}, 
    "green_light": {"correct": [], "incorrect": [], "none": []}, 
    "jolene": {"correct": [], "incorrect": [], "none": []}, 
    "la_vie_en_rose": {"correct": [], "incorrect": [], "none": []}, 
    "money_machine": {"correct": [], "incorrect": [], "none": []}, 
    "novacane": {"correct": [], "incorrect": [], "none": []}, 
    "rhyme_dust": {"correct": [], "incorrect": [], "none": []}, 
    "the_chain": {"correct": [], "incorrect": [], "none": []}, 
    }

acr : dict[str, dict[int, list[int]]] = {
    "clair_de_lune": {"correct": [], "incorrect": [], "none": []}, 
    "green_light": {"correct": [], "incorrect": [], "none": []}, 
    "jolene": {"correct": [], "incorrect": [], "none": []}, 
    "la_vie_en_rose": {"correct": [], "incorrect": [], "none": []}, 
    "money_machine": {"correct": [], "incorrect": [], "none": []}, 
    "novacane": {"correct": [], "incorrect": [], "none": []}, 
    "rhyme_dust": {"correct": [], "incorrect": [], "none": []}, 
    "the_chain": {"correct": [], "incorrect": [], "none": []}, 
    }

results : dict[str, dict[str, list[int]]] = {
    "clair_de_lune": {"shazam": [], "acr": []}, 
    "green_light": {"shazam": [], "acr": []}, 
    "jolene": {"shazam": [], "acr": []}, 
    "la_vie_en_rose": {"shazam": [], "acr": []}, 
    "money_machine": {"shazam": [], "acr": []}, 
    "novacane": {"shazam": [], "acr": []}, 
    "rhyme_dust": {"shazam": [], "acr": []}, 
    "the_chain": {"shazam": [], "acr": []}, 
}

def parse_results():

    for filename in filenames:
        path = "shazam/" + filename + "_results.txt"

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
        
        shazam[filename]["correct"] = correct
        shazam[filename]["incorrect"] = incorrect
        shazam[filename]["none"] = no_song
    

    for filename in filenames:
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
        
        acr[filename]["correct"] = correct
        acr[filename]["incorrect"] = incorrect
        acr[filename]["none"] = no_song
        

def compare_results():
    num_shazam = 0
    num_acr = 0
    for filename in filenames:
        for correct in shazam[filename]["correct"]:
            if acr[filename]["incorrect"].count(correct) != 0:
                num_shazam += 1
                results[filename]["shazam"].append(correct)
            if acr[filename]["none"].count(correct) != 0:
                num_shazam += 1
                results[filename]["shazam"].append(correct)
    
    for filename in filenames:
        for correct in acr[filename]["correct"]:
            if shazam[filename]["incorrect"].count(correct) != 0:
                num_acr += 1
                results[filename]["acr"].append(correct)
            if shazam[filename]["none"].count(correct) != 0:
                num_acr += 1
                results[filename]["acr"].append(correct)

    return num_shazam, num_acr



parse_results()
compare_results()

for song, counts in results.items():
    print("-------------------")
    print(song)
    print("Shazam:", counts["shazam"])
    print("ACR:", counts["acr"])