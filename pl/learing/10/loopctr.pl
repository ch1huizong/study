#! /usr/bin/env perl
use strict;

my ($total, $valid, %count);
# 统计单词
while(<>){
	foreach(split){
		$total++;
		next if /\W/;   #注意next语句使用,测试条件
		$valid++;
		$count{$_}++;
	}
}

print "Total things = $total, valid words = $valid\n";
foreach my $word (sort keys %count){
	print "$word was seen $count{$word} times.\n";
}

my @words = qw( fred barney pebbles dino wilma betty );
my @words = qw();
my $errors = 0;

foreach (@words){
	print "Type the word '$_':";
	chomp(my $try = <STDIN>);
	if ($try ne $_){
		print "Sorry - That's not right.\n\n";
		$errors++;
		redo;      # 重新这次循环
	}
}
print "You've completed the test, with $errors errors.\n";

for(1..10){
	print "Iteration number $_.\n\n";
	print "Please choose:last, next, redo, or none of the above?";
	chomp(my $choice = <STDIN>);
	last if $choice =~ /last/i;
	next if $choice =~ /next/i;
	redo if $choice =~ /redo/i;
	print "None choice... onward!\n\n";
}
print "That's all, folks!\n";

