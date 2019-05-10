#! /usr/bin/env perl
use strict;

my $what = shift @ARGV;
while(<>){
	if(/($what)/){   # 需要加上括号，限制范围
		print $1,"\n";
	}
}
