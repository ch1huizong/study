#! /usr/bin/env perl
use strict;

my $n = -5;
print "$n is a negative number.\n" if $n < 0;

my $n = 1;
print " ",($n += 2) until $n > 10;
print "\n";

# 统计出现的次数
my @people = qw( fred barney fred wilma dino barney fred pebbles );
my %count;
$count{$_}++ foreach @people;

my %seen;
foreach(@people){
	print "I've seen you something before, $_!\n" if $seen{$_}++;
}

for ($_ = "bedrock"; s/(.)//;){
	print "One character is: $1\n";
}

