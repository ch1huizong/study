#! /usr/bin/env perl
use 5.014;
use strict;

$_ = "yabba dabba doo";
if (/abba/){
	print "It matched!\n";
}

$_ = 'a real \\ backslash';
if (/\\/){
	print "It matched!\n";
}

$_ = "abba";
if (/(.)\1/){
	print "It matched same character next to itself!\n";
}

$_ = "yabba dabba doo";
if (/y(....) d\1/){
	print "It matched the same after y and d!\n";
}

$_ = "yabba dabba doo";
if (/y(.)(.)\2\1/){
	print "It matched after the y!\n";
}

$_ = "yabba dabba doo";
if (/y((.)(.)\3\2) d\1/){
	print "It matched many!\n";
}
print "*" x 60,"\n\n";

$_ = "aa11bb";
if (/(.)\g{1}11/){		# 新引用
	print "It matched!\n";
}
if (/(.)\g{-1}11/){   # 使用负号引用
	print "Negative matched!\n";
}

$_ = 'The HAL-9000 requires authorization to continue.';
if (/HAL-[\d]+/a){
	print "The string mentions some model of HAL computer.\n";
}


