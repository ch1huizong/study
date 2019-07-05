#! /usr/bin/env perl

use 5.010;
use strict;

say "Looking for my files that are readeable and writable";
die "No file specified!\n" unless @ARGV;

foreach(@ARGV){
	say "$_ is readable and writable" if -o -r -w ;
}
