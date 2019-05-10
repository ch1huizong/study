#! /usr/bin/env perl

use strict;

my %last_name = qw{
	fred flintstone Wilma Flintstone Barney Rubble
	betty rubble Bamm-Bamm Rubble PEBBLES FLINTSTONE
};

sub by_first_second {
	"\L$last_name{$b}" cmp "$last_name{$a}"  # 按姓式排序
		or
	"\L$b" cmp "\L$a"   #按名字排序
}

my @results = sort by_first_second keys %last_name;

foreach(@results){
	print "$_ -> $last_name{$_}\n";
}

