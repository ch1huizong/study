#! /usr/bin/env perl

use strict;

print "Please enter a string: ";
chomp(my $string = <STDIN>);
print "Please enter a sub string: ";
chomp(my $sub = <STDIN>);

my @places;

# 精巧
for(my $pos=-1;;){
	$pos = index $string, $sub, $pos+1;
	last if $pos == -1;
	push @places, $pos;
}

print "Location of '$sub' in '$string' are: @places\n";

