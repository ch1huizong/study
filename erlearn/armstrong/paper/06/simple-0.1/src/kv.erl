-module(kv).
-behaviour(gen_server).
-define(SERVER, ?MODULE).

%% ------------------------------------------------------------------
%% API Function Exports
%% ------------------------------------------------------------------

-export([start_link/0, start/0, stop/0, lookup/1, store/2]).

%% ------------------------------------------------------------------
%% gen_server Function Exports
%% ------------------------------------------------------------------

-export([init/1, handle_call/3, handle_cast/2, handle_info/2,
         terminate/2, code_change/3]).

%% ------------------------------------------------------------------
%% API Function Definitions
%% ------------------------------------------------------------------

start_link() ->
    gen_server:start_link({local, ?SERVER}, ?MODULE, [], []).

start() ->
    gen_server:start_link({local, ?SERVER}, ?MODULE, [], []).

stop() ->
    gen_server:cast(kv, stop).

store(Key, Value) ->
    gen_server:call(kv, {store, Key, Value}).

lookup(Key) ->
    gen_server:call(kv, {lookup, Key}).

%% ------------------------------------------------------------------
%% gen_server Function Definitions
%% ------------------------------------------------------------------

init([]) ->
    io:format("Key-Value server starting~n"),
    {ok, dict:new()}.


handle_call({store, Key, Value}, _From, Dict) ->
    Dict1 = dict:store(Key,Value,Dict),
    {reply, ack, Dict1};
handle_call({lookup, crash}, _From, _Dict) ->
    1/0;
handle_call({lookup, Key}, _From, Dict) ->
    {reply, dict:find(Key, Dict), Dict}.


handle_cast(stop, Dict) ->
    {stop, normal, Dict}.


handle_info(_Info, Dict) ->
    {noreply, Dict}.


terminate(_Reason, _Dict) ->
    io:format("K-V server terminating~n"),
    ok.


code_change(_OldVsn, Dict, _Extra) ->
    {ok, Dict}.

%% ------------------------------------------------------------------
%% Internal Function Definitions
%% ------------------------------------------------------------------

