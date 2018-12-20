-module(tr_app).
-behaviour(application).

-export([
    start/2,
    stop/1
    ]).

start(_Type, _StartArgs) ->
    case tr_sup:start_link() of   % 启动根监督者进程
        {ok, Pid} ->
            {ok, Pid};
        Other ->
            {error, Other}
    end.

stop(_State) -> ok.
