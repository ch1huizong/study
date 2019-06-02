#! /usr/bin/env python
# -*- coding:UTF-8 -*-

"""模拟case-switch语句"""

animals = []
felines = 0

def deal_with_a_cat():
    global felines
    print "Meow"
    animals.append("feline")
    felines += 1

def deal_with_a_dog():
    print "bark"
    animals.append("canine")

def deal_with_a_bear():
    print "watch out for the *HUG*!"
    animals.append("ursine")

token = {
    "cat" : deal_with_a_cat,
    "dog" : deal_with_a_dog,
    "bear": deal_with_a_bear,
}

words = ["cat", "bear", "cat", "dog"]
for word in words:
    token[word]()

nf = felines;
print "We met %d feline%s" % (nf, 's'[nf==1:])
print "The animals we met were:", ' '.join(animals)
