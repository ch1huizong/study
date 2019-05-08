-module(die_please).
-behaviour(gen_server).

-export([start_link/0]).
-export([init/1, handle_call/3, handle_cast/2, handle_info/2,
	 terminate/2, code_change/3]).

-define(SERVER, ?MODULE).
-define(SLEEP_TIME, (2 * 1000)).
-record(state, {}).


start_link() -> gen_server:start_link({local, ?SERVER}, ?MODULE, [], []).
init([]) -> {ok, #state{}, ?SLEEP_TIME}.   % 设置超时,after部分吧

handle_call(_Request, _From, State) -> 
    Reply = ok,
    {reply, Reply, State}.

handle_cast(_Msg, State) -> {noreply, State}.

handle_info(timeout, State) -> 
    i_want_to_die = right_now,  % 肯定会导致错误
    {noreply, State}.

terminate(_Reason, _State) -> ok.
code_change(_OldVsn, State, _Extra) -> {ok, State}.
