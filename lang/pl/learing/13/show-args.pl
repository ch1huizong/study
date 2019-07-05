#! /usr/bin/env perl

use strict;

foreach my $arg (@ARGV){
	print "one arg is $arg\n";
}

# glob
my @all_files = glob '.* *';
print "@all_files\n";

# 文件名通配另一种写法,编译器会判断是文件句柄还是通陪符
my $dir = '/etc';
my @dir_files = <$dir/* $dir/.*>;
print "@dir_files\n";

