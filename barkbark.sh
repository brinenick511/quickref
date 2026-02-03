#!/bin/bash
TITLE="${1:-"Done"}"
BODY="${2:-"Done"}"
NUM="${3:-1}"

BODY_WITH_BARK="${BODY}?sound=healthnotification"

python3 ~/utils/quickref/bark.py $TITLE $BODY_WITH_BARK $NUM
