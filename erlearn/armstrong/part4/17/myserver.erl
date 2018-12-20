-module(myserver).
-export([start_server/0, start_seq_server/0, start_parallel_server/0]).

%% 只处理一个连接

start_server() ->
    {ok, Listen} = gen_tcp:listen(2345,[binary, {packet,4}, 
                                        {reuseaddr,true}, 
                                        {active, true} ]),
    {ok, Socket} = gen_tcp:accept(Listen),
    gen_tcp:close(Listen),
    loop(Socket).



%% 顺序服务器，可以处理多个进来的连接，
%% 但需要一个连接处理完成后才能下一个

start_seq_server() ->
    {ok, Listen} = gen_tcp:listen(2345,[binary, {packet,4}, 
                                        {reuseaddr,true}, 
                                        {active, true} ]),
    seq_loop(Listen).

seq_loop(Listen) ->
    {ok, Socket} = gen_tcp:accept(Listen),
    loop(Socket),
    seq_loop(Listen).


%% 并行服务器
start_parallel_server() ->
    {ok, Listen} = gen_tcp:listen(2345,[binary, {packet,4}, 
                                        {reuseaddr,true}, 
                                        {active, true} ]),
    spawn(fun()-> per_connect(Listen) end).

per_connect(Listen) ->
    {ok, Socket} = gen_tcp:accept(Listen),
    spawn(fun()-> per_connect(Listen) end),
    loop(Socket).
    


loop(Socket) ->
    receive
        {tcp, Socket, Bin} ->
            io:format("Server received binary = ~p~n", [Bin]),
            Str = binary_to_term(Bin),
            io:format("Server (unpacked) = ~p~n",[Str]),
            Reply = lib_misc:string2value(Str),
            io:format("Sleep...~n"),
            lib_misc:sleep(6000),
            io:format("Server  replying = ~p~n",[Reply]),
            gen_tcp:send(Socket,term_to_binary(Reply)),
            loop(Socket);
        {tcp_closed, Socket} ->
            io:format("Server socket closed~n")
    end.

