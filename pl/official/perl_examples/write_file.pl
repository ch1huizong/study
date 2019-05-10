#! /usr/bin/env perl
use strict;
use warnings;

use Path::Class;
use autodie;

my $dir = dir("/tmp");

my $file = $dir->file("perlfile.txt");

# write
my $file_handle = $file->openw();    # 写
my @list = ('a', 'list', 'of', 'lines');
foreach my $line ( @list ){
	$file_handle->print($line . "\n");
}

