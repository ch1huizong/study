#!/usr/bin/env python
# -*- coding:UTF-8

import socket

def get_constants(prefix):
    "返回一个协议码值对应表"
    return dict( (getattr(socket,n),n)          # 巧妙,配合dict函数
         for n in dir(socket) if n.startswith(prefix)
    )

protocols = get_constants('IPPROTO_')
for name in ['icmp','udp','tcp',]:
    proto_num = socket.getprotobyname(name)
    const_name = protocols[proto_num]
    print'%4s   ->  %2d (soket.%-12s = %2d)'%\
        (name,proto_num,const_name,getattr(socket,const_name))
