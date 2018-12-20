-module(http_driver).
-export([relay/3]).

relay(Socket, Server, State) ->
    receive
        {tcp, Socket, Data} ->
            case parse_request(State, Data) of
                {completed, Request, State1} ->
                    Server ! {self(), {request, Request}},
                    relay(Socket, Server, State1);
                {more, State1} ->
                    relay(Socket, Server, State1)
            end;
        {tcp_closed, Socket} ->
            Server ! {self(), close};
        {Server, close} ->
            gen_tcp:close(Socket);
        {Server, Response} ->
            Data = format_response(Response),
            gen_tcp:send(Socket, Data),
            relay(Socket, Server, State);
        {'EXIT', Server, _} ->
            gen_tcp:close(Socket)
    end.
