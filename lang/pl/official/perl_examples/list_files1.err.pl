#! /usr/bin/env perl
use strict;
use warnings;

use Path::Class;

my $topdir = dir('/','etc');

sub gen_files {
	my $dir = shift @_;

	while (my $file = $dir->next){
		if ($file->is_dir()){       
			#gen_files($file);   # 递归调用怎么不行啊？循环列出所有文件
			#print "---" . $file->stringify . "\n";
			next;
		}else{
			print $file->stringify . "\n";
		}
	}	
}

gen_files($topdir);


