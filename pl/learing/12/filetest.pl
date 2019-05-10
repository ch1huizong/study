#! /usr/bin/env perl

use strict;

my $filename = "a";
die "Oops!A file called '$filename' already exists.\n" if -e $filename;

my @original_files = qw/ fred barney betty wilma pebbles dino bamm-bamm /;
my @big_old_files;
foreach my $filename (@original_files){
	push @big_old_files, $filename
		if -s $filename > 100_1000 and -A $filename > 90;
}
