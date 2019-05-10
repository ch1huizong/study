#! /usr/bin/env perl

use strict;
use File::Basename;
use File::Spec;

my($source, $dest) = @ARGV;

return "cannot create hard link for directory!\n" if -d $source;
if(-d $dest){
	my $basename = basename $source;
	$dest = File::Spec -> catfile($dest, $basename);
}
link $source, $dest or "cannot create hard link from '$source' to '$dest':$!\n";

