#! /usr/bin/env perl
use strict;
use warnings;

use Path::Class;
use autodie;

my $dir = dir("/tmp");

my $file = $dir->file("perlfile.txt");

# read
my $content = $file->slurp();   # 所有内容

my $file_handle = $file->openr();    # 读

while( my $line = $file_handle->getline() ){
	print $line;
}
print '-' x 60, "\n";
print $content;
