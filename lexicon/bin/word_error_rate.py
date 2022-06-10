#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from evaluate import load


# This is used to compute the word error rate (WER) using test data and ground truth (GT)
# Usage: python3 word_error_rate.py [data file] [gt file]
# Return: WER in percent

def print_wer(data, gt):
    df_data = open(data, "r")
    df_gt = open(gt, "r")

    predictions = []
    references = []
    for data_line, gt_line in zip(df_data, df_gt):
        data_line = data_line.strip()
        gt_line = gt_line.strip()

        if len(data_line) != 0 and len(gt_line) != 0:
            predictions.append(data_line)
            references.append(gt_line)

    df_gt.close()
    df_data.close()

    wer = load("wer")
    wer_score = wer.compute(predictions=predictions, references=references)

    print("WER : " + str(wer_score))


path = "/home/jerome/Bureau/BAProject/lexicon/"  # change path if needed

data_raw = sys.argv[1]
gt_raw = sys.argv[2]

print("Dataset:", data_raw)
print("GT:", gt_raw)
print("")
print_wer(data_raw, gt_raw)
