#! /usr/bin/env perl
use 5.010;
use strict;

$_ = "Hello there, neighbor";
if (/\s([a-zA-Z]+),/){
	print "the word was '$1'\n";
}

if (/(\S+) (\S+), (\S+)/){
	print "words were $1 $2 $3\n";
}

my $dino = "I fear that I'll be extinct after 1000 years.";
if ($dino =~ /([0-9]*) years/){
	print "That said '$1' years.\n";
}
my $dino = "I fear that I'll be extinct after a few million years.";
if ($dino =~ /([0-9]*) years/){
	print "Two:That said '$1' years.\n";
}
		
my $wilma = '123';
$wilma =~ /([0-9]+)/;
$wilma =~ /([a-zA-Z]+)/;
print "Match $1\n";

my $names = 'Fred or Barney';
if ( $names =~ /(?<name1>\w+) (?:and|or) (?<name2>\w+)/ ){
	say "I saw $+{name1} and $+{name2}.";
}

print "\n\n","-" x 60, "\n\n";

# 特殊变量
if ("Hello there, neighbor" =~ /\s(\w+),/){
	print "The actually matched '$&'.\n";
	print "That was ($`) ($&) ($').\n";
}

use 5.010;
if ("Hello there, neighbor" =~ /\s(\w+),/p){
	print "The actually matched '${^MATCH}'.\n";
	print "The whole String:\n";
	print "That was (${^PREMATCH})(${^MATCH})(${^POSTMATCH}).\n";
}

