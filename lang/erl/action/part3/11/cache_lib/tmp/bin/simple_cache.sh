#!/bin/sh
./erts-6.2/bin/erl \
	-sname cache \
	-setcookie abc \
	-boot  ./releases/0.0.1/start \
	-config ./releases/0.0.1/sys \
	-detached

