#!/bin/sh

# why num?
echo -n "27:cummingsify.here is my poem," | netcat -q -1 localhost $1 
echo
