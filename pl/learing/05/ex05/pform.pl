#! /usr/bin/env perl
use strict;

print "1234567890" x 6 , "\n";
print "Input Width Format:";
chomp(my $width = <STDIN>);

while(<STDIN>){
	chomp;
	printf "%${width}s\n",$_;
}
