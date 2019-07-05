#! /usr/bin/env perl

use strict;

my @numbers = (17, 100, 04, 1.50, 3.14159, -10, 1.5, 4, 2001, 90210, 666);
my @results = sort { $a <=> $b; } @numbers;
foreach(@results){
	printf "%20g\n",$_;
}

