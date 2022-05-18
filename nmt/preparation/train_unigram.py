#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import sentencepiece as spm

path = ""   # change path if needed

train_source_file_tok = path + sys.argv[1]
train_target_file_tok = path + sys.argv[2]

# Source subword model
source_train_value = '--input=' + train_source_file_tok + ' --model_prefix=source --vocab_size=10000 --hard_vocab_limit=false --split_digits=true'
spm.SentencePieceTrainer.train(source_train_value)
print("Done, training a SentencepPiece model for the Source finished successfully!")

# Target subword model
target_train_value = '--input=' + train_target_file_tok + ' --model_prefix=target --vocab_size=10000 --hard_vocab_limit=false --split_digits=true'
spm.SentencePieceTrainer.train(target_train_value)
print("Done, training a SentencepPiece model for the Target finished successfully!")