#! /usr/bin/env perl
use strict;

print "Need Word:";
chomp(my $word = <STDIN>);

while(<STDIN>){
	if(/\s+[A-Z][a-z]*\s+/){  #bug,里面开头后面没有大写字母
		print;
	}
}
