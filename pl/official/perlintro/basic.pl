#! /usr/bin/env perl
use strict;				# 严格模式
use warnings;

# 变量
my $name = "che";
print "Hello, $name\n";  # 变量内插
print 'Hello, $name\n',"\n";
print 42,"\n";

my $animal = "camel";    #变量声明
my $answer = 42;
print $animal,"\n";
print "The animal is $animal\n";
print "The square of $answer is", $answer * $answer, "\n";
print "\$_ is now:$_\n\n";  # 默认变量

# 数组
my @animals = ("camel", "llama", "owl");
my @numbers = (23, 42, 69);
my @mixed = ("camel", 42, 1.23);

print $animals[0],"\n";
print $animals[1],"\n";
print $mixed[$#mixed],"\n";  # $# 最后一个元素的索引 

print "@animals[0,1]\n";	# 数组切片
print "@animals[0..2]\n";	
print "@animals[1..$#animals]\n";

my @sorted = sort @animals;  # 数组排序
my @backwards = reverse @numbers;
print "Sorted:@sorted\n";
print "Reversed:@backwards\n\n";

# 哈希
my %fruit_color1 = ("apple","red","banana","yellow");
my %fruit_color2 = (
	apple	=> "red",
	banana	=> "yellow",
);
print "$fruit_color2{apple}\n";
my @fruits = keys %fruit_color1;     # 取键
my @colors = values %fruit_color1;   # 取值
print "Keys:@fruits\n";
print "Values:@colors\n\n";

# 引用,建立更复杂的数据类型
my $variables = {
	scalar	=> {
			description => "single item",
			sigil		=> '$',
	},

	array	=> {
			description => "ordered list of items",
			sigil		=> '@',
	},

	hash	=> {
			description => "key/value pairs",
			sigil		=> '%',
	}
};

print "Scalars begin with a $variables->{'scalar'}->{'sigil'}\n\n";

# 变量作用域
my $x = "foo";
my $con = 1;
if ($con){
	my $y = "bar";
	print $x,"\n";
	print $y, "\n";
}
print $x,"\n";
#print $y,"\n";   # 作用域外了，会引起编译错误
