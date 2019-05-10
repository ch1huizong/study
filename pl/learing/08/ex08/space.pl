#! /usr/bin/env perl

while(<>){
	chomp;
	if (/\s\z/){
		print "$_#\n";
	}
}
