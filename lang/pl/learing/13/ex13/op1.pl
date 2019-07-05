#! /usr/bin/env perl

use strict;

print "Please input the target dir:";
chomp(my $target = <STDIN>);
if ($target =~ /\A\s*\z/){
	chdir or die "cannot change to home dir:$!\n";
}else{
	chdir $target or die "cannot change to $target dir:$!\n";
}

# 使用目录句柄
# 注意使用了.而不是$target,防止切换到目的目录后有同名的子目录$target
opendir my $dh, "." or die "cannot change to $target dir:$!\n"; 
foreach my $file (sort readdir $dh){
	next if $file =~ /\A\./;
	print "$file\n";
}



