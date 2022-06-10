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

echo "Dehyphenate all files"
$PYTHON_PATH/python3 $NMT_PATH/preparation/dehyphenate.py $NMT_PATH/$SOURCE_TRAIN.cleaned
$PYTHON_PATH/python3 $NMT_PATH/preparation/dehyphenate.py $NMT_PATH/$SOURCE_TEST.cleaned
$PYTHON_PATH/python3 $NMT_PATH/preparation/dehyphenate.py $NMT_PATH/$TARGET_TRAIN.cleaned
$PYTHON_PATH/python3 $NMT_PATH/preparation/dehyphenate.py $NMT_PATH/$TARGET_TEST.cleaned
echo""

SOURCE_TRAIN_SIZE=$(wc -l < $NMT_PATH/$SOURCE_TRAIN.cleaned.dehyphenate)
TARGET_TRAIN_SIZE=$(wc -l < $NMT_PATH/$TARGET_TRAIN.cleaned.dehyphenate)
SOURCE_TEST_SIZE=$(wc -l < $NMT_PATH/$SOURCE_TEST.cleaned.dehyphenate)
TARGET_TEST_SIZE=$(wc -l < $NMT_PATH/$TARGET_TEST.cleaned.dehyphenate)

if [ "$SOURCE_TRAIN_SIZE" -ne "$TARGET_TRAIN_SIZE" ] ; then
    echo "Source and Target files for training are not of the same size"
    echo "Stopping execution"
    exit 1
else
    echo "Source and Target files for training are of the same size"
    echo "Continuing..."
fi
echo""

if [ "$SOURCE_TEST_SIZE" -ne "$TARGET_TEST_SIZE" ] ; then
    echo "Source and Target files for testing are not of the same size"
    echo "Stopping execution"
    exit 1
else
    echo "Source and Target files for testing are of the same size"
    echo "Continuing..."
fi
echo""

echo "Lowercase all files"
$PYTHON_PATH/python3 $NMT_PATH/preparation/lowercase.py $NMT_PATH/$SOURCE_TRAIN.cleaned.dehyphenate
$PYTHON_PATH/python3 $NMT_PATH/preparation/lowercase.py $NMT_PATH/$SOURCE_TEST.cleaned.dehyphenate
$PYTHON_PATH/python3 $NMT_PATH/preparation/lowercase.py $NMT_PATH/$TARGET_TRAIN.cleaned.dehyphenate
$PYTHON_PATH/python3 $NMT_PATH/preparation/lowercase.py $NMT_PATH/$TARGET_TEST.cleaned.dehyphenate
echo""

echo "Tokenize source: $SOURCE_TRAIN, $SOURCE_TEST and target: $TARGET_TRAIN, $TARGET_TEST"
$PYTHON_PATH/python3 $NMT_PATH/preparation/char_tokenizer.py $NMT_PATH/$SOURCE_TRAIN.cleaned.dehyphenate.lowercased $NMT_PATH/$TARGET_TRAIN.cleaned.dehyphenate.lowercased
$PYTHON_PATH/python3 $NMT_PATH/preparation/char_tokenizer.py $NMT_PATH/$SOURCE_TEST.cleaned.dehyphenate.lowercased $NMT_PATH/$TARGET_TEST.cleaned.dehyphenate.lowercased
echo""

echo "SUCCESS: Preparation Complete"
echo ""

echo "Renaming files for cleaning"
mv $SOURCE_TRAIN.cleaned.dehyphenate.lowercased.tokenized train2.source
mv $TARGET_TRAIN.cleaned.dehyphenate.lowercased.tokenized train2.target
mv $SOURCE_TEST.cleaned.dehyphenate.lowercased.tokenized test2.source
mv $TARGET_TEST.cleaned.dehyphenate.lowercased.tokenized test2.target
echo""

echo "Renaming complete, clean script can be used"