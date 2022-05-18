#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
import os


# This is used to get a source and target file from a json list
# with (source, target) tuples.
# Usage: python3 fromJSON.py [JSON file]
# Return: 2 files in [path] folder, [JSON file].source and [JSON file].target

def json_to_nmt_format(json_file, source_file, target_file):
    df_json = open(json_file, "r")
    df_source = open(source_file, "w+")
    df_target = open(target_file, "w+")

    data_json = json.load(df_json)

    for token in data_json:
        df_source.write(token[1] + "\n")
        df_target.write(token[0] + "\n")

    df_target.close()
    df_source.close()
    df_json.close()


path = "/home/jerome/Bureau/BAProject/nmt/"  # change if needed

json_file = sys.argv[1]  # path to json file
file_name = os.path.basename(json_file)
file_name = file_name.replace(".json", "")

source_file = path + file_name + ".source"  # path to source file
target_file = path + file_name + ".target"  # path to target file

# Run the convert function
json_to_nmt_format(json_file, source_file, target_file)
