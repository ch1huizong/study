#! /usr/bin/env perl
use strict;

$_ = "I saw Barney\ndown at the bowling alley\nwith Fred\nlast night.\n";
if (/Barney.*Fred/s){   #匹配\n
	print "That string mentions Fred after Barney!\n";
}

#while (<STDIN>){
#	print if /\.png\Z/; # 定位到\n,不用去除\n
#}

#while (<STDIN>){
#	chomp;					# 数据清洗了
#	print "$_\n" if /\.png\z/; # 绝对定位到行末
#}

my $some_other = "I dream of betty rubble.";
if ($some_other =~ /\brub/){
	print "Yes, there's the rub.\n";
}

print "Do you like Perl?";
my $like_perl = <STDIN> =~ /\byes\b/i;
if ($like_perl){
	print "You said earlier that you like Perl, so...\n";
}


