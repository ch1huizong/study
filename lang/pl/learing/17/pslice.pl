#! /usr/bin/env perl

use strict;

#切片
my @names = qw{ zero one two three four five six seven eight nine };
my @numbers = ( @names )[ 9, 0, 2, 1, 0 ]; # 列表切片，注意括号
my @numbers1 = @names[ 9, 0, 2, 1, 0 ];     # 数组切片，注意可以没有括号
print "@numbers\n";
print "@numbers1\n";
print "Bedrock @names[9, 0, 2, 1, 0]\n";    # 数组切片可以内插

# 哈稀切片
my %score = (
	"barney"	=> 195,
	"fred"		=> 205,
	"dino"		=> 30,
	"bamm-bamm"	=> 195,
);

my @three_scores = @score{qw / barney fred dino /};   #注意是一个切片，列表
print "\@three_scores:@three_scores\n";

my @players = qw/ barney fred dino/;
my @bowling_scores = (1, 2, 3);
@score{ @players } = @bowling_scores; # 哈系切片赋值，字典综合赋值
print "\@players:@players\n";
print "\@scores: @score{@players}\n";



