#! /usr/bin/env perl
use strict;

$_ = "He's out bowling with Barney tonight.";
s/Barney/Fred/;
print "$_\n";
print "\n";

# sub
$_ = "green scaly dinosaur";
print "$_\n";

s/(\w+) (\w+)/$2,$1/;
print "$_\n";

s/^/huge, /;
print "$_\n";

s/,.*green//;
print "$_\n";

s/green/red/;
print "$_\n";

s/\w+$/($`!)$&/;
print "$_\n";

s/\s+(!\W+)/$1 /;
print "$_\n";

s/huge/giantic/;
print "$_\n";

$_ = "home, sweet home!";
print "$_\n";
s/home/cave/g;
print "$_\n";

$_ = "Input  data\t may have    extra whitespace.";
print "$_\n";
s/\s+/ /g;
print "$_\n";

# 无损替换
my $original = 'Fred ate 1 rib';
my $copy = $original;
print "\$original:$original\n";
print "\$copy:$copy\n";

$copy =~ s/\d+ ribs?/10 ribs/; 
print "\$original:$original\n";
print "\$copy:$copy\n";

use 5.014;
my $copy = $original =~ s/\d+ ribs?/10 ribs/r;
print "\$original:$original\n";
print "\$copy:$copy\n";

# 大小写
$_ = "I saw Barney with Fred.";
print "$_\n";
s/(fred|barney)/\U$1/gi;
print "$_\n";
s/(fred|barney)/\L$1/gi;
print "$_\n";
s/(\w+) with (\w+)/\U$2\E with $1/i;
print "$_\n";
s/(fred|barney)/\u\L$1/gi;
print "$_\n";
print "\n";

# 分割函数split
my @fields = split /:/, "abc:def:g:h";
print "@fields\n";

my $some_input = "This is a \t       test.\n";
my @args = split /\s+/, $some_input;
print "@args\n";

# join函数
my $x = join ":",4,6,8,10,12;
print "$x\n";
my @values = split /:/,$x;
print join "-", @values;
print "\n";

# 模式解包并绑定变量
$_ = "Hello there, neighbor!";
my($first, $second, $third) = /(\S+) (\S+), (\S+)/;
print "$second is my $third\n";

# 模式解包并存储在数组中
my $text = "Fred dropped a 5 ton granite block on Mr. Slate";
my @words = ($text =~ /([a-z]+)/ig);
print "Result:@words\n";

# 模式解包并存储在字典中
my $data = "Barney Rubble Fred Flintstone Wilma Flintstone";
my %last_name = ($data =~ /(\w+)\s+(\w+)/g);
say keys %last_name;

#多行模式，^和$
$_ = "I'm much better\nthan Barney is\nat bowling,\nWilma.\n";
print "Found 'wilma' at start of line\n" if /^wilma\b/im;

my $filename = "text";
open FILE, $filename 
	or die "Can'nt open '$filename':$!";
my $lines = join "", <FILE>;
$lines =~ s/^/$filename: /gm;
print $lines;









