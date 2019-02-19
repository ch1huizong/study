#! /bin/bash

veg1=carrots
veg2=tomatoes

if [[ "$veg1" < "$veg2" ]]
then
    echo "Although $veg1 precede $veg2 in the dictionary,"
    echo "this implies nothing about my culinary preferences."
else
    echo "What kind of dictionary are you using, anyhow?"
fi
