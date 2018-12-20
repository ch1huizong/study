-module(web_profiler).
-export([ping/2]).

-import(lists,[reverse/1]).

ping(Host, Timeout) ->
    get_url(Host,Timeout).

get_url(Host,Timeout) ->
    case gen_tcp:connect(Host, 80,[binary,{packet,0 }], Timeout * 1000) of
        {ok, S} ->
            T1 = erlang:now(),
            ok = gen_tcp:send(S, "HEAD / HTTP/1.0\r\n\r\n"),
            receive_data(S, []),
            Timecost = timer:now_diff(erlang:now(), T1) / 1000,
            io:format("~p : ~p~n",[Host, Timecost]),
            {Host, Timecost};
        {error, _Reason} ->
            io:format("~p : timeout~n",[Host]),
            {Host, timeout}
    end.
    

receive_data(Socket, SoFar) ->
    receive
        {tcp, Socket, Bin} ->
            receive_data(Socket,[Bin | SoFar]);
        {tcp_closed, Socket} ->
            list_to_binary(reverse(SoFar))
    end.

