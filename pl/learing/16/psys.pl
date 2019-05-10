#! /usr/bin/env perl

use strict;

# system系统调用
system 'date';
system 'ls -l $HOME';
print "\n";
system 'for i in *; do echo == $i == ; cat $i; done';
print "-" x 60,"\n";

# 多参数版本,不会调用shell
#system 'tar','cvf',"my.tar",".";

# exec系统调用，陷进去
#exec 'date';

# 使用反引号捕获输出结果
print "使用反引号捕获输出结果-->\n";
my $now = `date`;
print "The time is now $now\n";

my @functions = qw{ int rand sleep length hex eof not exit sqrt umask };
my %about;

foreach(@functions){
	$about{$_} = `perldoc -t -f $_`;
}
foreach((my $key, my $value) = each %about){
	print "$key --> $value\n";
}
print "\n\n";
print "-" x 60,"\n";

# 列表上下文中使用反引号
my $who_text = `who`;
my @who_lines = split /\n/,$who_text;
my @who_lines1 = `who`;  #自动拆分多行，但不会消灭换行符

my %ttys;
foreach(`who`){
	my($user, $tty, $date) = /(\S+)\s+(\S+)\s+(.*)/;
	$ttys{$user} .= "$tty at $date\n";
}
foreach((my $key, my $value) = each %ttys){
	print "$key --> \n$value\n";   # 结果怎么是两遍？
}



