#! /usr/bin/env perl
use strict;

#$^I = ".out";
while(<>){
	#s/Fred/Larry/gi;
	s/(Fred)(.*?)(Wilma)/\3\2\1/gi;
#	s/(Wilma)(.*?)(Fred)/\3\2\1/gi;
	print;
}

