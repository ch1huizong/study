#! /usr/bin/env perl
use strict;
use warnings;

use Path::Class;

my $dir = dir('/','etc');

while (my $file = $dir->next){
	
	next if $file->is_dir();

	print $file->stringify . "\n";
}
