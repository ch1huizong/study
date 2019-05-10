#! /usr/bin/env perl

use strict;

my $dir = "/";
chdir $dir or "cannot change to $dir:$!";
system 'ls','-l';
system 'ls -l 1>ls.out 2>ls.err';
