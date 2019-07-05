#! /usr/bin/env perl
use strict;

$^I = ".bak";

while(<>){
	s{^(#!.*\n)}{\1## Copyright (C) 20XX by Yours Truly\n};
	print ;
}
