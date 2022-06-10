#!/bin/sh

SOURCE_TRAIN="jebb_train.source"
TARGET_TRAIN="jebb_train.target"

SOURCE_TEST="jebb_test.source"
TARGET_TEST="jebb_test.target"

NMT_PATH="/home/jerome/Bureau/BAProject/nmt"
PYTHON_PATH="/home/jerome/miniconda3/envs/natas/bin"

echo "Remove empty lines from source: $SOURCE_TRAIN, $SOURCE_TEST and target: $TARGET_TRAIN, $TARGET_TEST"
$PYTHON_PATH/python3 $NMT_PATH/preparation/remove_empty_lines.py $NMT_PATH/$SOURCE_TRAIN $NMT_PATH/$TARGET_TRAIN
$PYTHON_PATH/python3 $NMT_PATH/preparation/remove_empty_lines.py $NMT_PATH/$SOURCE_TEST $NMT_PATH/$TARGET_TEST
echo""

echo "Tokenize source: $SOURCE_TRAIN, $SOURCE_TEST and target: $TARGET_TRAIN, $TARGET_TEST"
$PYTHON_PATH/python3 $NMT_PATH/preparation/char_tokenizer.py $NMT_PATH/$SOURCE_TRAIN.cleaned $NMT_PATH/$TARGET_TRAIN.cleaned
$PYTHON_PATH/python3 $NMT_PATH/preparation/char_tokenizer.py $NMT_PATH/$SOURCE_TEST.cleaned $NMT_PATH/$TARGET_TEST.cleaned
echo""

echo "SUCCESS: Preparation Complete"
echo ""

echo "Renaming files for cleaning"
mv $SOURCE_TRAIN.cleaned.tokenized train.source
mv $TARGET_TRAIN.cleaned.tokenized train.target
mv $SOURCE_TEST.cleaned.tokenized test.source
mv $TARGET_TEST.cleaned.tokenized test.target
echo""

echo "Renaming complete, clean script can be used"