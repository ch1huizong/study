#! /usr/bin/env perl

use strict;

# 排序小程序,数字大小
sub by_number {
	#if ($a < $b){ -1 }elsif ($a > $b){ 1 }else { 0 };
	$a <=> $b;
}

# 按字母排序
sub by_code_point {
	$a cmp $b;
}

sub case_insensitive {
	"\L$a" cmp "\L$b";
}

# 列表排序
my @some_numbers = (1,101,2,7,3,18,10);
my @result = sort by_number @some_numbers;
my @result1 = sort { $a <=> $b } @some_numbers;
my @result2 = reverse sort { $a <=> $b } @some_numbers;
my @result3 = sort { $b <=> $a } @some_numbers;

print "Unsorted:\t@some_numbers\n";
print "  Sorted:\t@result\n";
print "  Sorted:\t@result1\n";
print "Reversed:\t@result2\n";
print "Reversed:\t@result3\n";

print "-" x 60,"\n";

# 哈系排序
my %score = (
	"barney"	=> 195,
	"fred"		=> 205,
	"dino"		=> 30,
	"bamm-bamm"	=> 195,
);

sub by_score {
	$score{$b} <=> $score{$a} 
		or
	$a cmp $b
}

my @winners = sort by_score keys %score;
foreach(@winners){
	print "$_ -> $score{$_}\n";
}

