#!/bin/sh

FILE="jebb_test"
GT="jebb_test_gt"

LEXICON_PATH="/home/jerome/Bureau/BAProject/lexicon"
PYTHON_PATH="/home/jerome/miniconda3/envs/natas/bin"

echo "Remove empty lines from files: $FILE, $GT"
$PYTHON_PATH/python3 $LEXICON_PATH/preprocessing/remove_empty_lines.py $LEXICON_PATH/$FILE $LEXICON_PATH/$GT
echo""

echo "Dehyphenate all files"
$PYTHON_PATH/python3 $LEXICON_PATH/preprocessing/dehyphenate.py $LEXICON_PATH/$FILE.cleaned
$PYTHON_PATH/python3 $LEXICON_PATH/preprocessing/dehyphenate.py $LEXICON_PATH/$GT.cleaned
echo""

FILE_SIZE=$(wc -l < $LEXICON_PATH/$FILE.cleaned.dehyphenate)
GT_SIZE=$(wc -l < $LEXICON_PATH/$GT.cleaned.dehyphenate)

if [ "$FILE_SIZE" -ne "$GT_SIZE" ] ; then
    echo "Dataset and ground truth files are not of the same size"
    echo "Stopping execution"
    exit 1
else
    echo "Dataset and ground truth files are of the same size"
    echo "Continuing..."
fi
echo""

echo "Lowercase all files"
$PYTHON_PATH/python3 $LEXICON_PATH/preprocessing/lowercase.py $LEXICON_PATH/$FILE.cleaned.dehyphenate
$PYTHON_PATH/python3 $LEXICON_PATH/preprocessing/lowercase.py $LEXICON_PATH/$GT.cleaned.dehyphenate
echo""

echo "Remove special character and lines"
$PYTHON_PATH/python3 $LEXICON_PATH/preprocessing/remove_special_token.py $LEXICON_PATH/$FILE.cleaned.dehyphenate.lowercased $LEXICON_PATH/$GT.cleaned.dehyphenate.lowercased

FILE_SIZE=$(wc -l < $LEXICON_PATH/$FILE.cleaned.dehyphenate.lowercased.normalized)
GT_SIZE=$(wc -l < $LEXICON_PATH/$GT.cleaned.dehyphenate.lowercased.normalized)

if [ "$FILE_SIZE" -ne "$GT_SIZE" ] ; then
    echo "Dataset and ground truth files are not of the same size"
    echo "Stopping execution"
    exit 1
else
    echo "Dataset and ground truth files are of the same size"
    echo "Continuing..."
fi
echo""

echo "SUCCESS: Preparation Complete"
echo ""

echo "Remove empty lines from files: $FILE.cleaned.dehyphenate.lowercased.normalized, $GT.cleaned.dehyphenate.lowercased.normalized"
$PYTHON_PATH/python3 $LEXICON_PATH/preprocessing/remove_empty_lines.py $LEXICON_PATH/$FILE.cleaned.dehyphenate.lowercased.normalized $LEXICON_PATH/$GT.cleaned.dehyphenate.lowercased.normalized
echo""

echo "Renaming files for cleaning"
mv $FILE.cleaned.dehyphenate.lowercased.normalized.cleaned $FILE.preprocessed
mv $GT.cleaned.dehyphenate.lowercased.normalized.cleaned $GT.preprocessed
echo "Renaming complete, clean script can be used"