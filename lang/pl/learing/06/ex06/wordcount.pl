#! /usr/bin/env perl
use strict;

my %word_count;
while(<>){
	chomp;
	$word_count{$_} += 1;
}

foreach my $key (sort keys %word_count){
	print "$key -> $word_count{$key}\n";
}
print "\n\n";

# %env

printf "%-10s\t\t%-10s\n","Key", "Value";
foreach my $key (sort keys %ENV){
	printf "%-10s\t\t%-10s\n",$key,$ENV{$key};
}

