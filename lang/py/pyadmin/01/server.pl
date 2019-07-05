#! /usr/bin/env perl

use Server;

$server = Server->new('192.168.1.3','King');

$server->ping('192.168.1.10');
