#! /usr/bin/env perl

$celsius = 20;

while ($celsius <= 45){
	$fahr = ($celsius * 9 / 5) + 32;  # 华式温度
	print "$celsius C is $fahr F.\n";
	$celsius = $celsius + 5;
}
