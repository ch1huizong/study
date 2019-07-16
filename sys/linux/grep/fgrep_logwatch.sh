#! /bin/bash

WATCHING_WORDS="watch_words"
LOG_FILE="/var/log/messages"

if [ ! -f "$WATCHING_WORDS" ]; then
    echo "$WATCHING_WORDS not found"
    exit 1
fi
 
tail -f $LOG_FILE | grep -F --color=auto -i -f $WATCHING_WORDS 
