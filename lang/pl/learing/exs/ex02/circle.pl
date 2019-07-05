#! /usr/bin/env perl

$pi = 3.141592654 ;

# circle
print "What is the radius? ";
chomp($radius = <STDIN>);
if($radius <= 0){
	print "Perimeter of a Circle of radius $radius is 0.\n";
}else{
	$perimeter = 2 * $pi * $radius;
	print "Perimeter of a Circle of radius $radius is $perimeter.\n"; 
}


# cross
print "Input First Number:";
chomp($first = <STDIN>);
print "Input Second Number:";
chomp($second = <STDIN>);
print "The Cross is ", $first * $second,"\n";

# repeat
print "Input a string:";
$mystring = <STDIN>;
print "Input the repeat number:";
chomp($repeat = <STDIN>);
$result = $mystring x $repeat;
print "The Result is:\n$result";
