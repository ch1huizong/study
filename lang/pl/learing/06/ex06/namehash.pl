#! /usr/bin/env perl
use strict;

my %name_hash = (
	fred	=> "flintstone",
	barney	=> "rubble",
	wilma	=> "flintstone",
);
print "Input the first name:";
chomp(my $first_name = <STDIN>);
print "The last name for $first_name is \"", $name_hash{$first_name},"\".\n";
