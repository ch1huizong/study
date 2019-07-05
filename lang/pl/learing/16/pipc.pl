#! /usr/bin/env perl

use strict;

# 实现了类似linux的管道和python中协程的作用
open my $find_fh, '-|','find',qw( / -atime +30 -size +1000 -print )
	or die "fork: $!";
while(<$find_fh>){
	chomp;
	printf "%s size %dK last accessed %.2f days ago\n",
		$_, (1023 + -s $_)/1024, -A $_;
}
