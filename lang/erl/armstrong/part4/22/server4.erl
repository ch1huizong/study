-module(server4).
-export([start/2, rpc/2, swap_code/2]).

start(Name, Mod) ->
    register(Name, spawn(fun()-> loop(Name, Mod, Mod:init()) end)).

%% 热交换
swap_code(Name, Mod) -> rpc(Name, {swap_code, Mod}).

rpc(Name, Request) ->
    Name ! {self(), Request},
    receive 
        {Name, crash} -> exit(rpc);   %% 使客户端崩溃
        {Name, ok, Response} -> Response
    end.


loop(Name, Mod, OldState) ->
    receive
        {From, {swap_code, NewCallBackMod}} ->
            From ! {Name, ack},
            loop(Name,NewCallBackMod, OldState);

        {From, Request} -> 
            try Mod:handle(Request, OldState) of  %% 事务处理
                {Response, NewState} ->
                    From ! {Name, ok, Response},
                    loop(Name, Mod, NewState)
            catch 
                _:Why ->
                    log_the_error(Name, Request, Why),
                    From ! {Name, crash},
                    loop(Name, Mod, OldState)
            end
    end.

log_the_error(Name, Request, Why) -> 
    io:format("Server ~p request ~p~nCaused exception ~p~n",[Name,Request, Why]).
