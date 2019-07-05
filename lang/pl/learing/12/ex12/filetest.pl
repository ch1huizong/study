#! /usr/bin/env perl

use strict;

foreach(@ARGV){
	print $_,"\n";
	print "$_ exists.\n" if -e;
	print "$_ is readable.\n" if -r;
	print "$_ is writable.\n" if -w;
	print "$_ is excutable.\n" if -x;
	print "\n\n";
}
