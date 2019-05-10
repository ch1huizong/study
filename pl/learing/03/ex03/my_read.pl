#! /usr/bin/env perl

# 读入行字符串，反向输出
print reverse <STDIN>;

# 读入行字符串，排序输出，两种方式
@lines = <STDIN>;
@sorted = sort @lines;
# first
print "One line in seperate line:\n";
print @sorted;

# second
print "\n";
print "One line in a line:\n";
chomp(@sorted);
print "@sorted\n"; 


# 读入索引，并输出相应的名字
@names = qw(fred betty barney dino wilma pebbles bamm-bamm);
chomp(@indexes = <STDIN>);
foreach (@indexes){
	print "$names[$_ - 1]\n";
}




