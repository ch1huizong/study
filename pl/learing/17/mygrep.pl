#! /usr/bin/env perl

use strict;

my @odd_numbers;
foreach(1..1000){
	push @odd_numbers, $_ if $_ % 2;
}
print "@odd_numbers\n";

# 使用grep,类似于python中filter函数
my @odd = grep { $_ % 2 } 1..1000;
print "\@odd:@odd\n";

open my $fh, "passwd" or "cannot open file:$!";
my @matches = grep /root|chzb/, <$fh>;
print @matches;

# 使用map函数
print "Some powers of two are:\n", map "\t" . ( 2 ** $_ ) . "\n", 0..15;

