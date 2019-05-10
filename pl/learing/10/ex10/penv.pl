#! /usr/bin/env perl

use 5.010;
use strict;

$ENV{ZERO} = 0;
$ENV{EMPTY} = '';
$ENV{UNDEFINED} = undef;

my $longest = 0;
foreach my $key (keys %ENV){  #计算最大键长度
	my $key_len = length($key);
	$longest = $key_len if $key_len > $longest;
}

foreach my $key (keys %ENV){
	printf "%-${longest}s %s\n", $key, $ENV{$key} // "(undefined)";
}


