#! /usr/bin/env perl
use strict;
use warnings;

use Email::MIME;

my $message = Email::MIME->create(
	header_str => [
		From	=> 'ch1huizong@gmail.com',
		To		=> 'chehuizong@163.com',
		Subject => 'Welcome to Perl World!',
	],

	attributes => {
		encoding	=> 'quoted-printable',
		charset		=> 'ISO-8859-1',
	},
	body_str	=> "Welcome to Perl World! Enjoy it !\n",
);

use Email::Sender::Simple qw(sendmail);
sendmail($message);
print "Complete!\n";
