-module(simple_sup).
-behaviour(supervisor).

-export([start/0, init/1]).

start() ->
    supervisor:start_link({local, simple_supervisor},?MODULE, []).

init([]) ->
    RestartStrategy = {one_for_one, 5, 1000},
    Packet = {packet, {packet_assembler, start, []},
            permanent, 500, worker, [packet_assembler]},
    Server = {server, {kv, start, []},
            permanent, 500, worker, [kv]},
    Logger = {logger, {simple_logger, start, []},
            permanent, 500, worker, [simple_logger]},
    Children = [Packet, Server, Logger],
    {ok, {RestartStrategy, Children}}.
