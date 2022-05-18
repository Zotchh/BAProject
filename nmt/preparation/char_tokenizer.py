#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import pyonmttok


# This is used to tokenize src and tgt files lines at character level
# Usage: python3 char_tokenizer.py [src file] [tgt file]
# Return: 2 files in [path] folder, [src file].tokenized and [tgt file].tokenized

path = "/home/jerome/Bureau/BAProject/nmt/"     # change path if needed

source_raw = sys.argv[1]
target_raw = sys.argv[2]
source_raw_name = os.path.basename(source_raw)
target_raw_name = os.path.basename(target_raw)
source_tokenized = path + source_raw_name + ".tokenized"
target_tokenized = path + target_raw_name + ".tokenized"

print("Source Dataset:", source_raw)
print("Target Dataset:", target_raw)

tokenizer = pyonmttok.Tokenizer("char",
                                no_substitution=False,
                                with_separators=False,
                                case_feature=False)

with open(source_raw) as source, open(source_tokenized, "w+") as source_tokenized:
    for line in source:
        line = line.strip()
        line = tokenizer(line)
        # line = ['<s>'] + line + ['</s>']    # Not sure if needed
        line = " ".join([token for token in line])
        source_tokenized.write(line + "\n")

print("Done tokenizing the source file! Output:", source_tokenized)

with open(target_raw) as target, open(target_tokenized, "w+") as target_tokenized:
    for line in target:
        line = line.strip()
        line = tokenizer(line)
        # line = ['<s>'] + line + ['</s>']    # Not sure if needed
        line = " ".join([token for token in line])
        target_tokenized.write(line + "\n")

print("Done tokenizing the target file! Output:", target_tokenized)
