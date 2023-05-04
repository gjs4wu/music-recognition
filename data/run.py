#!/usr/bin/env python3

import sys
import sox
import random
import os

FIRST_TRIM = 20

num_samples = 1
actions = [""]
tfm = sox.Transformer()
cmb = sox.Combiner()
song = sys.argv[1]
new_samples = int(sys.argv[2])


def get_filename(index: int):
    return song + "/inputs/" + str(index).zfill(4) + ".wav"


def write(base: int, action: str):
    all_actions = actions[base] + action

    actions.insert(num_samples, all_actions)


def trim(base: int):
    global num_samples
    tfm.clear_effects()

    filename = get_filename(base)
    length = float(sox.core.soxi(filename, "D"))

    if length < 2:
        print("file too short to trim")
        return -1

    if random.choice([0, 1]):
        tfm.trim(0, length - 1)
    else:
        tfm.trim(1)

    print(base, "trimmed to length", length - 1)

    tfm.build_file(filename, get_filename(num_samples))

    write(base, "trim, ")

    num_samples += 1


def quiet(base: int):
    global num_samples
    tfm.clear_effects()

    tfm.vol(0.5)

    filename = get_filename(base)
    print(base, "volume decreased")

    tfm.build_file(filename, get_filename(num_samples))

    write(base, "quiet, ")

    num_samples += 1


def loud(base: int):
    global num_samples
    tfm.clear_effects()
    tfm.vol(2)

    filename = get_filename(base)
    print(base, "volume increased")

    tfm.build_file(filename, get_filename(num_samples))

    write(base, "loud, ")

    num_samples += 1


def real_noise(base: int):
    global num_samples
    cmb.clear_effects()
    filename = get_filename(base)
    noise = random.choice(os.listdir("noises"))
    noise_file = "noises/" + noise
    print(base, "added real noise", noise)

    length = float(sox.core.soxi(filename, "D"))

    cmb.trim(0, length)
    cmb.build([filename, noise_file], get_filename(num_samples), "mix")



    write(base, noise + ", ")

    num_samples += 1

def echo(base: int):
    global num_samples
    tfm.clear_effects()

    filename = get_filename(base)
    tfm.echo()

    print(base, "echo added")

    tfm.build_file(filename, get_filename(num_samples))

    write(base, "echo, ")

    num_samples += 1


def new_sample(base: int):
    rand = random.randint(0, 4)
    if base < FIRST_TRIM:
        rand = 0

    if rand == 0:
        trim(base)

    elif rand == 1:
        quiet(base)

    elif rand == 2:
        loud(base)

    elif rand == 3:
        real_noise(base)

    elif rand == 4:
        echo(base)


if __name__ == "__main__":

    counts = [0] * new_samples

    for i in range(new_samples - 1):
        base = random.randint(0, num_samples - 1)
        
        while counts[base] > 3:
            base = random.randint(0, num_samples - 1)
        
        if (base != 0):
            counts[base] += 1

        new_sample(base)

    results = open(song + "/results.txt", "w")
    for i in range(len(actions)):
        results.write(str(i) + ": " + str(actions[i]) + "\n")
