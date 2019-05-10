#! /usr/bin/env perl

@rocks = qw( bed java look );

print "Before pop:\n\t@rocks\n";
$fred = pop(@rocks);
$barney = pop @rocks;
pop @rocks;
print "After pop:\n\t@rocks\n";

print "Before push:\n\t@rocks\n";
push(@rocks,0);
push @rocks,8;
push @rocks,1..10;
@others = qw/ 9 0 2 1 0/;
push @rocks,@others;
print "After push:\n\t@rocks\n";

print "-" x 60,"\n";

print "Shift And Unshift:\n";
@array = qw# dino fred barney #;
$m = shift(@array);
$n = shift @array;
shift @array;
$o = shift @array;

print "Shift:\n";
print "\t",'$m:',$m,"\n";
print "\t",'$n:',$n,"\n";
print "\t",'$o:',$o,"\n";
print "\t",'$array:',"@array","\n";

print "Unshift:\n";
unshift(@array,5);
unshift @array,4;
@others = 1..3;
unshift @array,@others;
print "\t",'@array:',"@array","\n";

print "-" x 60,"\n";

print "Test splice:\n";
@array = qw( pebbles dino fred barney betty );
@removed1 = splice @array,1,2,qw(wilma);
print "@removed1\n";
print "@array\n";

print "-" x 60,"\n";
print "Other Operations:\n";
print "Reverse:\n";
@fred = 6..10;
print '@fred:',"@fred\n";
@new = reverse @fred;
print '@new:',"@new\n";
print '@fred:',"@fred\n";

print "\n";

print "Sort:\n";
@rocks = qw/ bedrock slate rubble granite/;
print '@rocks:',"@rocks\n";
@sorted = sort(@rocks);
print '@sorted:',"@sorted\n";

print "\n" x 3;
# 强制切换成表量上下文
print "How many rocks do you have?\n";
print "I have ",@rocks," rocks!\n";
print "I have ",scalar @rocks," rocks!\n";


