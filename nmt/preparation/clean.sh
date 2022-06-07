#!/bin/sh

SOURCE_TRAIN="jebb_train.source"
TARGET_TRAIN="jebb_train.target"

SOURCE_TEST="jebb_test.source"
TARGET_TEST="jebb_test.target"

NMT_PATH="/home/jerome/Bureau/BAProject/nmt"

rm $NMT_PATH/$SOURCE_TRAIN.*
rm $NMT_PATH/$SOURCE_TEST.*
rm $NMT_PATH/$TARGET_TRAIN.*
rm $NMT_PATH/$TARGET_TEST.*