#! /usr/bin/env perl
use strict;
use warnings;

# 控制结构
# print "LALALA\n" while 1;   # 循环

my @array = 1..20;
print $array[$_] foreach 0..15;
print "\n";

# 文件IO
open(my $in, "<", "input.txt") or die "Can't open input.txt:$!";
open(my $out,">", "output.txt") or die "Can't open output.txt:$!";
open(my $log,">>", "my.log") or die "Can't open my.log:$!";

while(<$in>){					# read
	print "Just read in this line:$_";
}
close $in or die "$in:$!";

my $data = "This is a test line\n";
print $out $data;			    # write
print $log $data;			    # append

# 子函数
sub logger {
	my $logmessage = shift;
	open my $logfile, ">>", "my.log" or die "Could not open my.log:$!";
	print $logfile $logmessage;
}
logger("We have a logger subroutine!");

sub square {
	my $num = shift;
	my $result = $num * $num;
	return $result;
}

my $sq = square(8);
print "\$sq:$sq\n";



