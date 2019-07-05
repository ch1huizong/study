#! /usr/bin/env perl

use 5.010;
use strict;
use warnings;

my $Debug = $ENV{DEBUG} // 1;

my $num = int(1+rand(100));
print "你的秘密数字是$num\n" if $Debug;

while(1){
	print "请输入1到100之间的数字:";
	chomp(my $guess = <STDIN>);

	if ($guess =~ /quit|exit|\A\s*\z/i){   # 十分重要
		print "退出游戏!\n";
		last;
	}elsif ( $guess > $num ){
		print "太高了!再试一次!\n";
	}elsif ($guess == $num){
		print "恭喜你，猜对了！\n";
		last;
	}else{
		print "太低了!再试一次！\n";
	}
}
