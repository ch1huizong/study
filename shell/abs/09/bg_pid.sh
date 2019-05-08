#!/usr/bin/env bash
# 最后后台pid

LOG=$0.log

COMMAND1="sleep 100"

echo "Logging PIDS background commands for script: $0" >> "$LOG"
echo >> "$LOG"

echo -n "PID of \"$COMMAND1\": " >> "$LOG"
${COMMAND1} &

echo $! >> "$LOG"
