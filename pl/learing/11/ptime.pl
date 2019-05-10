#! /usr/bin/env perl

use strict;
use Time::Piece;
use DateTime;
use DateTime::Duration;

my $dt = DateTime->from_epoch( epoch => time );
printf "%4d%02d%02d", $dt->year, $dt->month, $dt->day,"\n";
print $dt->ymd,"\n";
print $dt->ymd('/'),"\n";
print $dt->ymd(''),"\n";
print "\n";

# 日期时间差
my $dt1 = DateTime->new(
	year	=> 1987,
	month	=> 8,
	day		=> 23,
);
my $dt2 = DateTime->new(
	year	=> 2016,
	month	=> 11,
	day		=> 7,
);
my $duration = $dt2 - $dt1;
my @units = $duration -> in_units( qw(year month day) ); #有问题?
printf "%d years, %d months, and %d days\n",@units;

my $duration = DateTime::Duration->new( days => 7 );
my $dt3 = $dt2 + $duration;
print $dt3->ymd,"\n";

# simple
my $t = localtime;
print 'The month is ',$t->month,"\n";
