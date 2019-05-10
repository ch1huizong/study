#! /usr/bin/env perl

use strict;

foreach(<*>){
	if (-l $_){
		my $value = readlink $_ or warn "no target for $_.\n";
		print "$_ -> $value\n";
	}
}
