#! /usr/bin/env perl
use strict;

my @array = qw/fred barney betty/;
print @array,"\n";
print "@array","\n";

my @items = qw(wilma dino pebbles);
printf "The items are:\n" . ("%-10s\n" x @items), @items;

#模拟cat
print <>;

#模拟sort;
print sort <>;




