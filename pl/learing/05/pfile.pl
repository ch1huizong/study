#! /usr/bin/env perl

$success_open = open SHADOW, "shadow";
$success_write = open TARGET,"> myshadow";

if (! $success_open){
	die "Can't open file:$!";
}

while (<SHADOW>){
	print TARGET $_;
}
