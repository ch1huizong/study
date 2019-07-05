#!/bin/bash
# A system information gathering script
# bash版本

function uname_func()
{
    UNAME="uname -a"
    printf "Gathering system infomation with $UNAME command:\n\n"
    $UNAME
}

function diskspace_func()
{
    DISKSPACE="df -h"
    printf "Gathering system infomation with $DISKSPACE command:\n\n"
    $DISKSPACE
}

function main()
{
    uname_func
    diskspace_func
}

main
