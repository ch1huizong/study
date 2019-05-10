#! /usr/bin/env perl
use strict;
use warnings;

use Config::Any;

my @files = (
	"path/to/config_file.json",
	"path/to/config.pl",
	"path/to/config.xml",
);
my $config = Config::Any->load files( { files => \@files } );
