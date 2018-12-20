#!/bin/sh
cd run/foo; python logsim.py & 
cd ../bar; sleep 600; python logsim.py &
