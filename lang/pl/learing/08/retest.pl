#! /usr/bin/env perl
use strict;

# 模式测试程序
print "输入你的模式:";
chomp(my $pattern = <STDIN>);

while (<>){
	chomp;
	if(/($pattern)/){
		print "Matched: |$`<$&>$'|\n";
	}else{
		print "No match: |$_|\n";
	}
}
