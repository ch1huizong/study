-module(tr_sup).

-behaviour(supervisor).

%% API
-export([start_link/0]).

%% 监督者回调
-export([init/1]).

-define(SERVER, ?MODULE).

start_link() ->
    supervisor:start_link({local, ?SERVER}, ?MODULE, []).

init([]) ->
    Server = {tr_server, {tr_server, start_link, []},   % server进程
            permanent, 2000, worker, [tr_server]},
    Children = [ Server ],
    RestartStrategy = { one_for_one, 0, 1 },
    {ok, {RestartStrategy, Children}}.

