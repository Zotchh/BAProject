#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

from levenshtein import levenshtein_distance
from datetime import datetime


# This is used to choose the best correction from candidates generated from lexicons
# Usage: python3 spellcheck.py [in_file] [greek_lexicon_file] [en_lexicon_file] [gt file]
# Return: a file in [path] folder, [in_file].corrected


def generate_candidates(keyword, lexicon):
    """
    Return a list of possible candidates for keyword using lv distance as well as a dict {candidates -> lv dist}
    @params:
        keyword     - Required  : target word (String)
        lexicon     - Required  : lexicon used to get candidate from (List[String])
    """
    candidates = []
    candidates_lev = {}
    for word in lexicon:
        lev_distance = levenshtein_distance(keyword, word)
        if lev_distance <= 3:
            candidates.append(word)
            candidates_lev[word] = lev_distance

    return candidates, candidates_lev


def select_best_candidate(replacements, frequencies, lv_distances):
    """
    Return the best replacement by taking the most similar word first and the most frequent one then
    @params:
        replacements    - Required  : candidates for replacement (List[String])
        frequencies     - Required  : dictionary of frequencies (Dict{String -> Int})
        lv_distances    - Required  : dictionary of lv distances (Dict{String -> Int})
    """
    best_replacement = ""
    best_freq = 0
    best_lv = 4

    for word in replacements:
        if lv_distances[word] < best_lv:
            best_lv = lv_distances[word]
            best_freq = frequencies.get(word, 0)
            best_replacement = word
        elif lv_distances[word] == best_lv:
            if frequencies.get(word, 0) > best_freq:
                best_freq = frequencies.get(word, 0)
                best_replacement = word

    return best_replacement


def build_lexicon(greek_lexicon_file, en_lexicon_file, gt_file):
    """
    Return a lexicon for greek and english mixed
    @params:
        greek_lexicon_file  - Required  : greek lexicon filename (String)
        en_lexicon_file     - Required  : english lexicon filename (String)
        gt_file             - Required  : ground truth filename (String)
    """
    df_greek_lexicon = open(greek_lexicon_file, "r")
    df_en_lexicon = open(en_lexicon_file, "r")
    df_gt = open(gt_file, "r")

    lexicon = []
    frequencies = {}

    for line in df_greek_lexicon:
        separator_index = line.find(',')
        if separator_index != -1:
            word = line[:separator_index]
            freq = int(line[separator_index+1:])
            lexicon.append(word)
            frequencies[word] = freq

    for line in df_en_lexicon:
        line = line.strip()
        lexicon.append(line)

    for line in df_gt:
        line = line.strip()
        lexicon.append(line)

    df_greek_lexicon.close()
    df_en_lexicon.close()
    df_gt.close()

    return lexicon, frequencies


def correct(input_file, output_file, greek_lexicon_file, en_lexicon_file, gt_file):
    """
    Generate an output file with token detected as incorrect replaced with their potential best correction
    @params:
        input_file              - Required  : input filename (String)
        output_file             - Required  : output filename (String)
        greek_lexicon_file      - Required  : greek lexicon filename (String)
        en_lexicon_file         - Required  : english lexicon filename (String)
        gt_file                 - Required  : ground truth filename (String)
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("START =", current_time)

    in_file = open(input_file, "r")
    out_file = open(output_file, "w+")

    # Get file length and reset
    length = sum(1 for line in in_file)
    in_file.seek(0)

    print("Building lexicons...")
    lexicon, frequencies = build_lexicon(greek_lexicon_file, en_lexicon_file, gt_file)
    print("COMPLETE: lexicons successfully built")

    replacement_count = 0
    cache = {}
    for i, line in enumerate(in_file):
        keyword = line.strip()
        if keyword not in lexicon:
            if cache.get(keyword, "") != "":
                out_file.write(cache[keyword] + "\n")
            else:
                candidates, lv_distances = generate_candidates(keyword, lexicon)
                if len(candidates) > 0:
                    print("Replacements found for token: " + keyword)
                    replacement_count += 1
                    replacement = select_best_candidate(candidates, frequencies, lv_distances)
                    cache[keyword] = replacement
                    out_file.write(replacement + "\n")
                else:
                    out_file.write(keyword + "\n")
        else:
            out_file.write(keyword + "\n")

        if i % 100 == 0:
            print("Token " + str(i) + "/" + str(length))

    print("COMPLETE: There were " + str(replacement_count) + " replacements")

    in_file.close()
    out_file.close()

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("END =", current_time)


path = "/home/jerome/Bureau/BAProject/lexicon/"  # change path if needed

target_raw = sys.argv[1]
target_raw_name = os.path.basename(target_raw)
target_corrected = path + target_raw_name + ".corrected"

greek_lexicon_raw = sys.argv[2]
en_lexicon_raw = sys.argv[3]
gt_raw = sys.argv[4]

print("Target Dataset:", target_raw)

correct(target_raw, target_corrected, greek_lexicon_raw, en_lexicon_raw, gt_raw)
