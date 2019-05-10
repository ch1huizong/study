#! /usr/bin/env perl
use strict;
use warnings;

use Email::Valid;

my @email_addresses = (
	'chehuizong@163.com',
	'look@',
	'ch1huizong@gmail.com',
	'perl.org',
	'hello_world@163.com',
);

foreach my $email (@email_addresses){
	if (Email::Valid->address($email)){
		print "Passed: $email\n";
	}else{
		print "Not Passed: $email\n";
	}
}

