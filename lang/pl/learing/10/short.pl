#! /usr/bin/env perl

use 5.0.10;
use warnings;
use strict;

my $Verbose = $ENV{VERBOSE} // 1;
print $Verbose,"\n";
print "I can talk to you!\n" if $Verbose;

foreach my $try (0, undef, '0', 1, 24){
	print "Trying [$try] ---> ";
	my $value = $try // 'default';  # 已定义则短路，未定义则默认值
	print "\tgot [$value]\n";
}

my $name;
printf "%s", $name // '';
