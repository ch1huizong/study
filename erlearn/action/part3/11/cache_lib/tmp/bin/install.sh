#!/bin/sh
ROOT=`pwd`
DIR=./erts-6.2/bin
sed s:%FINAL_ROOTDIR%:$ROOT: $DIR/erl.src > $DIR/erl
