#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import re


# This is used to remove lines with special tokens or special char from a token of a target file
# Usage: python3 remove_special_token.py [tgt file] [tgt GT file]
# Return: a file in [path] folder, [tgt file].normalized and [tgt GT file].normalized

def remove_special_token(target_input, target_output, target_gt_input, target_gt_output):
    df_input = open(target_input, "r")
    df_output = open(target_output, "w+")
    df_gt_input = open(target_gt_input, "r")
    df_gt_output = open(target_gt_output, "w+")

    for line, gt_line in zip(df_input, df_gt_input):
        # Remove end of sentences character
        if line.endswith((".\n", ",\n", ";\n", ":\n")):
            line = line[:-2] + "\n"
        if gt_line.endswith((".\n", ",\n", ";\n", ":\n")):
            gt_line = gt_line[:-2] + "\n"

        # Remove parenthesis
        line = line.replace("(", "")
        line = line.replace(")", "")
        gt_line = gt_line.replace("(", "")
        gt_line = gt_line.replace(")", "")

        # Remove brackets
        line = line.replace("[", "")
        line = line.replace("]", "")
        gt_line = gt_line.replace("[", "")
        gt_line = gt_line.replace("]", "")

        # Remove apostrophes
        line = line.replace("’", "")
        line = line.replace("‘", "")
        line = line.replace("'", "")
        gt_line = gt_line.replace("’", "")
        gt_line = gt_line.replace("‘", "")
        gt_line = gt_line.replace("'", "")

        # if the line contains digits or is only a roman number, drop it
        if bool(re.match(r'\w*\d\w*', line)) is False and \
                bool(re.match('^(?=[mdclxvi])m*(c[md]|d?c*)(x[cl]|l?x*)(i[xv]|v?i*)$', line)) is False:
            df_output.write(line)
            df_gt_output.write(gt_line)

    df_input.close()
    df_output.close()


path = "/home/jerome/Bureau/BAProject/lexicon/"  # change path if needed

target_raw = sys.argv[1]
target_raw_name = os.path.basename(target_raw)
target_normalized = path + target_raw_name + ".normalized"

target_gt_raw = sys.argv[2]
target_gt_raw_name = os.path.basename(target_gt_raw)
target_gt_normalized = path + target_gt_raw_name + ".normalized"

print("Target Dataset: ", target_raw)
print("Tagret GT: ", target_gt_raw_name)

remove_special_token(target_raw, target_normalized, target_gt_raw, target_gt_normalized)
