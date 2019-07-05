#! /usr/bin/env perl

use strict;
use Module::CoreList;

my %modules = %{ $Module::CoreList::version{5.020} };
print join "\n",keys %modules;
