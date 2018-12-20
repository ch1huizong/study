-module(sc_app).
-behaviour(application).

-export([start/2, stop/1]).

start(_StartType, _StartArgs) ->
    sc_store:init(),
    case sc_sup:start_link() of
        {ok, Pid} ->
            sc_event_logger:add_handler(),  % 增加事件处理回调模块
            {ok, Pid};
        Other ->
            {error, Other}
    end.

stop(_State) ->
    ok.
