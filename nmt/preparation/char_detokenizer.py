#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import pyonmttok


# This is used to detokenize src and tgt files lines at character level
# Usage: python3 char_detokenizer.py [src file] [tgt file]
# Return: 2 files in [path] folder, [src file].detokenized and [tgt file].detokenized

path = "/home/jerome/Bureau/BAProject/nmt/"     # change path if needed

source_raw = sys.argv[1]
target_raw = sys.argv[2]
source_raw_name = os.path.basename(source_raw)
target_raw_name = os.path.basename(target_raw)
if "tokenized" in source_raw_name:
    source_detokenized = path + source_raw_name.replace("tokenized", "detokenized")
else:
    source_detokenized = path + source_raw_name + ".detokenized"
if "tokenized" in target_raw_name:
    target_detokenized = path + target_raw_name.replace("tokenized", "detokenized")
else:
    target_detokenized = path + target_raw_name + ".detokenized"

print("Source Dataset:", source_raw)
print("Target Dataset:", target_raw)

tokenizer = pyonmttok.Tokenizer("char",
                                no_substitution=False,
                                with_separators=False,
                                case_feature=False)

with open(source_raw) as source, open(source_detokenized, "w+") as source_detokenized:
    for line in source:
        line = line.split()
        line = " ".join(line)
        line = line.replace(" ", "")
        source_detokenized.write(line + "\n")

print("Done detokenizing the source file! Output:", source_detokenized)

with open(target_raw) as target, open(target_detokenized, "w+") as target_detokenized:
    for line in target:
        line = line.split()
        line = " ".join(line)
        line = line.replace(" ", "")
        target_detokenized.write(line + "\n")

print("Done detokenizing the target file! Output:", target_detokenized)
