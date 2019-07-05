#! /usr/bin/env perl

use strict;

# 删除
my $successful = unlink qw(a b c);
print "I deleted $successful file(s) just now.\n";

# 删除与glob连用
foreach my $file (glob '*.o'){
	unlink $file or warn "failed on $file: $!\n";
}

# 重命名,批量改名
use 5.014;
foreach my $file (glob '*.old'){
	my $newfile = $file =~ s/\.old/.new/r;
	if (-e $newfile){
		warn "can't rename $file to $newfile:$newfile exits.\n";
	}elsif (rename $file => $newfile){

	}else{
		warn "rename $file to $newfile failed:$!\n";
	}

}

#硬软链接\
my $perl = readlink '/bin/perl';
print "$perl\n";

# 新建目录和删除目录
my $temp_dir = "/tmp/scratch_$$";
mkdir $temp_dir, 0700 or die "cannot create $temp_dir:$!\n";
unlink glob "$temp_dir/* $temp_dir/.*";
rmdir $temp_dir;


