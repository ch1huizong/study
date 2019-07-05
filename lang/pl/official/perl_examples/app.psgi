#! /usr/bin/env perl
use strict;
use warnings;

use Plack::App::Directory;

my $app = Plack::App::Directory->new({ 
			root => "/root/Documents"
})->to_app;
