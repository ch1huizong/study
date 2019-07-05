#! /usr/bin/env perl
use strict;
use warnings;

use Spreadsheet::Read;

my $workbook = ReadData ("test.xlsl");
print $workbook->[1]{A3}  . "\n";
