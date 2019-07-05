#! /usr/bin/env perl

# 访问
foreach my $person (qw/barney fred/){
	print "I've heard of $person $family_name{$person}.\n";
}

print '-' x 60,"\n";

# 创建
%some_hash = ('foo',35, 'bar',12.4, 2.5,'hello',
	'wilma',1.72e30, 'betty',"bye\n");

@any_array = %some_hash;  #展哈系
print "@any_array\n";

print '-' x 60,"\n";

# 反转
my %inverse_hash = reverse %some_hash;
@array = %inverse_hash;
print "@array\n";

print '-' x 60,"\n";

# 胖箭头
my %last_name = (
	fred	=> 'flintstone',
	dino	=> undef,
	barney	=> 'rubble',
	betty	=> 'rubble',
);

# 哈系函数
my @k = keys %last_name;
my @v = values %last_name;
print "@k\n";
print "@v\n\n";

# 迭代
print "Unsorted:\n";
while ( ($key, $value) = each %last_name ){
	print "$key => $value\n";
}
print "\n";
print "Sorted:\n";
foreach my $key (sort keys %last_name){
	$value = $last_name{$key};
	print "$key => $value\n";
}




