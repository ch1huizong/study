#! /usr/bin/env perl

use Server;

$server = Server->new('192.168.0.150','Klab');
$server->ping('192.168.0.1');
