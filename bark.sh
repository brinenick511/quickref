#!/bin/bash
TITLE="${1:-"Done"}"
BODY="${2:-"Done"}"
NUM="${3:-1}"

python3 ~/utils/quickref/bark.py $TITLE $BODY $NUM