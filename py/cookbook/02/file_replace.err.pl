#! /usr/bin/env perl
use strict;
use warnings;

my ($stext, $rtext, $input, $output) = @ARGV;

die "usage:$0 search_text replace_text [infile [outfile]]\n" unless @AGRV >= 3 && @ARGV <=5; 

open(my $in, "<$input") or die "cannot open '$input' file:$!\n";
open(my $out, "$output>") or die "cannot open '$output' file:$!\n";

while(<$in>){
	s/\$stext/$rtext/;
	print $out $_;
}

close $in;
close $out;





