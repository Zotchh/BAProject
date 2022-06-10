#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os


# This is used to lowercase a target file
# Usage: python3 lowercase.py [tgt file]
# Return: a file in [path] folder, [tgt file].lowercased

def lowercase(target_input, target_output):
    tgt_input = open(target_input, "r")
    tgt_output = open(target_output, "w+")

    for line in tgt_input:
        tgt_output.write(line.lower())

    tgt_input.close()
    tgt_output.close()


path = "/home/jerome/Bureau/BAProject/lexicon/"  # change path if needed

target_raw = sys.argv[1]
target_raw_name = os.path.basename(target_raw)
target_lowercased = path + target_raw_name + ".lowercased"

print("Target Dataset:", target_raw)

lowercase(target_raw, target_lowercased)
