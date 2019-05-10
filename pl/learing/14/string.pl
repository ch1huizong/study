#! /usr/bin/env perl

use strict;

# index,rindex
my $stuff = "Howdy world!";
my $where = index($stuff, "wor");
my $where1 = index($stuff,"w");
my $where2 = index($stuff, "w", $where1 + 1);
my $where3 = index($stuff, "w", $where2 + 1);
print "$where1\t$where2\t$where3\n";

my $last_slash = rindex("/etc/passwd","/");
print "$last_slash\n";

# substr,切片
my $mineral = substr("Fred J. Flintstone",8, 5);
my $rock = substr "Fred J. Flintstone",13, 1000;  #long
my $rock1 = substr "Fred J. Flintstone",13;
print "$mineral\n$rock\n$rock1\n";

my $out = substr("some very long string", -3, 2); #负索引

# 连用
my $long = "some very long string";
my $right = substr($long, index($long,"l"));
print "->$long\n->$right\n";

# 切片(选取)替换
my $string = "Hello, world!";
substr($string,0,5) = "Goodbye";
print $string,"\n";

# sprintf 返回格式化字符串
my $money = sprintf "%.2f", 2.49997;
print $money,"\n";

sub big_money{
	my $number = sprintf "%.2f", shift @_;
	1 while $number =~ s/^(-?\d+)(\d\d\d)/$1,$2/;
	$number =~ s/^(-?)/$1\$/;
	$number;
}
print &big_money(12345678.9),"\n";







