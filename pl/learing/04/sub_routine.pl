#! /usr/bin/env perl
use 5.010;

# 关于子程序
sub marine {
	state $n = 0;
	$n += 1;
	print "Hello,sell number $n!\n";
}

# 全部引用的是全局变量
sub sum_of_fred_and_barney {
	print "Hey, you called the sum_of_fred_and_barney subroutine!\n";
	$fred + $barney;
}

sub larger_of_fred_or_barney {
	if ($fred > $barney){
		$fred;
	}else{
		$barney;
	}
}

sub list_from_fred_to_barney{
	if ($fred < $barney){
		$fred..$barney;
	}else{
		reverse $barney..$fred;
	}
}

# 开始引入私有变量
sub max1 {
	if ($_[0] > $_[1]){
		$_[0];
	}else{
		$_[1];
	}
}

sub max2 {
	my($m, $n) = @_;
	if ($m > $n){ $m } else { $n }
}

# 变长参数列表，可以有多个参数
sub max3{
	my($max_so_far) = shift @_;
	foreach (@_){
		if ($_ > $max_so_far){
			$max_so_far = $_;
		}
	}
	$max_so_far;
}
$maximum = &max3(3,5,10,4,6);
print "\$maximum is $maximum.\n";

#返回值return
sub which_element_is {
	my($what, @array) = @_;
	foreach(0..$#array){
		if ($what eq $array[$_]){
			return $_;
		}
	}
	-1;
}

my @names = qw/ fred barney betty dino wilma pebbles bamm-bamm/;
my $result = &which_element_is("dino", @names);
print "\$result is $result.\n";

$fred = 11;
$barney = 6;
@c = &list_from_fred_to_barney;
print "\@c is @c.\n";

$wilma = &sum_of_fred_and_barney;
print "\$wilma is $wilma.\n";

$barney = 3 * &sum_of_fred_and_barney;
print "\$barney is $barney.\n";

$large = &larger_of_fred_or_barney;
print "\$large is $large.\n";

foreach (1..10){
	my($square) = $_ * $_;
	print "$_ squared is $square.\n";
}

marine();
marine();
marine();

# 开始引入累加器
running_sum(5 , 6);
running_sum(1..3);
running_sum( 4 );

sub running_sum{
	state $sum = 0;
	state @numbers ;  #注意声明,相当与累加器

	foreach my $number (@_){
		push @numbers, $number;
		$sum += $number;
	}
	
	say "The sum of (@numbers) is $sum.";
}

