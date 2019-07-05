#! /usr/bin/env perl

use strict;

die "No file names supplied!\n" unless @ARGV;
my $oldest_file = shift @ARGV;
my $oldest_time = -M $oldest_file;

foreach(@ARGV){
	my $age = -M;  # 342不使用临时变量的情况，不明白它在说什么？
	($oldest_file, $oldest_time) = ($_, $age)
		if $age > $oldest_time;
	
}

printf "The oldest file was %s, and it was %0.1f days old.\n", 
	$oldest_file,$oldest_time;
