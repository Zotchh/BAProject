#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import re


# This is used to remove hyphen from a target file
# Usage: python3 dehyphenate.py [tgt file]
# Return: a file in [path] folder, [tgt file].dehypenate

def dehyphenate(target_input, target_output):
    tgt_input = open(target_input, "r")
    tgt_output = open(target_output, "w+")

    hyphen_before = False
    buffer = ""

    for line in tgt_input:
        if hyphen_before:
            tgt_output.write(buffer + line)
            hyphen_before = False
            buffer = ""
        elif line.endswith("-\n") and bool(re.match('^[,;.: ]+$', line[-3])) is False:
            hyphen_before = True
            buffer = line[:-2]
        else:
            tgt_output.write(line)

    tgt_input.close()
    tgt_output.close()


path = "/home/jerome/Bureau/BAProject/nmt/"  # change path if needed

target_raw = sys.argv[1]
target_raw_name = os.path.basename(target_raw)
target_dehyphenate = path + target_raw_name + ".dehyphenate"

print("Target Dataset:", target_raw)

dehyphenate(target_raw, target_dehyphenate)
