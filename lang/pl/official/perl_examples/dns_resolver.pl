#! /usr/bin/env perl
use strict;
use warnings;

use Net::DNS::Resolver;

my $hostname = "perl.org";
my $res = Net::DNS::Resolver->new(
	nameservers => [qw(222.222.202.202)],
);

my $query = $res->search($hostname);

if ($query){
	foreach my $rr ($query->answer){
		next unless $rr->type eq "A";
		print "Found an A record: " . $rr->address, "\n";
	}
}
