#! /usr/bin/env perl

# standard input
while (defined($line = <STDIN>)){
	print "I saw $line";
}

while (<STDIN>){
	print "I saw $_";
}

# 全部读入，再逐次打印
foreach(<STDIN>){
	print "I saw $_";
}

# 钻石操作符，读取命令行参数
while (<>) {
	chomp;
	print "It was $_ that I saw!\n";
}
