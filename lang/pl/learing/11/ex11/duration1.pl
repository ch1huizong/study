#! /usr/bin/env perl

use strict;
use Time::Piece;
use DateTime;

my $t = localtime;

my $now = DateTime->new(
	year	=> $t->year,
	month	=> $t->mon,
	day		=> $t->mday,
);

my $then = DateTime->new(
	year	=> $ARGV[0],
	month	=> $ARGV[1],
	day		=> $ARGV[2],
);

my $duration = $now - $then;

my @units = $duration -> in_units( qw(years months days) );

printf "%d years, %d months, and %d days\n",@units;
