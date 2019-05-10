#! /usr/bin/env perl

use strict;
use File::Basename; 
use File::Spec;
use File::Class;

my $name = "/usr/local/bin/python";
my $basename = basename $name;
print $basename,"\n";
print "-" x 60,"\n";

print "Please enter a filename: ";
chomp(my $oldname = <STDIN>);

my $dirname = dirname $oldname;
my $basename = basename $oldname;

$basename =~ s/^/not/;
my $newname = File::Spec -> catfile($dirname, $basename);
print $newname,"\n";

rename($oldname, $newname)  # 这里确定必须是真实的名字
	or warn "Can't rename '$oldname' to '$newname':$!";




