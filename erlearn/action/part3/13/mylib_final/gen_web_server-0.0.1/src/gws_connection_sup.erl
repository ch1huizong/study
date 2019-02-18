-module(gws_connection_sup).
-behaviour(supervisor).

-export([
        start_link/4,
        start_child/1
    ]).

-export([init/1]).

%%%============================================================
%%% API 函数

start_link(Callback, IP, Port, UserArgs) ->
    {ok, Pid} = supervisior:start_link(?MODULE, [Callback, IP, Port, UserArgs]),% 监督者启动
    start_child(Pid),  % Server实例进程启动
    {ok, Pid}.

start_child(Server) ->
    supervisor:start_child(Server, []).

%%%============================================================
%%% Supervisor回调函数

init([Callback, IP, Port, UserArgs]) ->
    BasicSockOpts = [binary,
                    {active, false},
                    {packet, http_bin},
                    {reuseaddr, true}],
    SockOpts = case IP of
                    undefined -> BasicSockOpts;
                    _         -> [{ip, IP} | BasicSockOpts]
                end,
    {ok, LSock} = gen_tcp:listen(Port, SockOpts),

    Server = {gws_server, {gws_server, start_link, [Callback,LSock, UserArgs]},
                temporary, brutal_kill, worker, [gws_server]},
    Children = [Server],
    RestartStrategy = {simple_one_for_one, 1000, 3600},
    {ok, {RestartStrategy, Children}}.

