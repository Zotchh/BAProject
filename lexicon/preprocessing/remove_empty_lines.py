#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os


# This is used to remove lines if any of src or tgt have empty lines
# Usage: python3 remove_empty_lines.py [src file] [tgt file]
# Return: 2 files in [path] folder, [src file].cleaned and [tgt file].cleaned

def remove_lines(source_input, target_input, source_output, target_output):
    df_src_input = open(source_input, "r")
    df_tgt_input = open(target_input, "r")
    df_src_output = open(source_output, "w+")
    df_tgt_output = open(target_output, "w+")

    for src_line, tgt_line in zip(df_src_input, df_tgt_input):
        if src_line.strip() and tgt_line.strip():
            df_src_output.write(src_line)
            df_tgt_output.write(tgt_line)

    df_tgt_input.close()
    df_src_input.close()
    df_src_output.close()
    df_tgt_output.close()


path = "/home/jerome/Bureau/BAProject/lexicon/"  # change path if needed

source_raw = sys.argv[1]
target_raw = sys.argv[2]
source_raw_name = os.path.basename(source_raw)
target_raw_name = os.path.basename(target_raw)
source_cleaned = path + source_raw_name + ".cleaned"
target_cleaned = path + target_raw_name + ".cleaned"

print("Source Dataset:", source_raw)
print("Target Dataset:", target_raw)

remove_lines(source_raw, target_raw, source_cleaned, target_cleaned)
