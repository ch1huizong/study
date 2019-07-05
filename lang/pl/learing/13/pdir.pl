#! /usr/bin/env perl

use strict;
use File::Spec::Functions;

chdir '/etc' or die "cannot chdir to /etc: $!\n";

#目录句柄
my $dir_to_process = '/etc';
opendir my $dh, $dir_to_process or die "Cannot open $dir_to_process: $!";
foreach my $filename (readdir $dh){
	print "one file in $dir_to_process is $filename\n";
}
closedir $dh;

#目录句柄的过滤
my $dir_to_process = '/etc';
opendir $dh, $dir_to_process or die "cannot open $dir_to_process: $!\n";
while(my $name = readdir $dh){
	next if $name =~ /^\./;
	$name = catfile($dir_to_process, $name); # 构造完整文件名
	next unless -f $name and -r $name;
	print "$name\n";
}
closedir $dh;

