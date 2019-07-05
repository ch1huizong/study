#! /usr/bin/env perl
use 5.010;
use strict;

sub total {
	my $sum;
	foreach (@_){
		$sum += $_;
	}
	$sum;
}

# total
my @fred = qw( 1 3 5 7 9 );
my $fred_total = total(@fred);
print "The total of \@fred is $fred_total.\n";
print "Enter some numbers on seperate lines:\n";
my $user_total = total(<STDIN>);
print "The total of those numbers is $user_total.\n";

# 1..1000
print "The total of from 1 to 1000 is ",total(1..1000),"\n";


#above average
sub average {
	if (@_ == 0){ return }
	total(@_) / @_ ;
}
sub above_average {
	my $average = average(@_);
	my @list ;
	foreach (@_){
		if ($_ > $average){
			push @list, $_;
		}
	}
	@list;  #返回列表
}

my @fred = above_average(1..10);
print "\@fred is @fred\n";
print "(Should be 6 7 8 9 10)\n";
my @barney = above_average(100,1..10 );
print "\@barney is @barney\n";
print "(Should be just 100)\n";

# greet
sub greet {
	state @visitors;  # 累积数组
	my $visitor = shift;

	print "Hi, $visitor! ";
	if (! @visitors){
		print "You are the first one here!\n";
	}else{
		#print "$visitors[-1] is also here!\n";
		print "I've seen: @visitors\n";
	}
	push @visitors, $visitor;
}
greet("Fred");
greet("Barney");
greet("Wilma");
greet("Betty");
