-module(packet_assembler).
-behaviour(gen_fsm).
-define(SERVER, ?MODULE).
-define(NAME, my_simple_packet_assembler).

%% ------------------------------------------------------------------
%% API Function Exports
%% ------------------------------------------------------------------

-export([start_link/0, start/0, send_header/1, send_data/1]).

%% ------------------------------------------------------------------
%% gen_fsm Function Exports
%% ------------------------------------------------------------------

-export([init/1, waiting/2, collecting/2, handle_event/3,
        handle_sync_event/4, handle_info/3,
        terminate/3,code_change/4]).

%% ------------------------------------------------------------------
%% API Function Definitions
%% ------------------------------------------------------------------

start_link() ->
    gen_fsm:start_link({local, ?SERVER}, ?MODULE, [], []).

start() ->
    gen_fsm:start_link({local, ?NAME}, ?MODULE, [], []).

send_header(Len) -> gen_fsm:send_event(?NAME, Len).

send_data(Str) -> gen_fsm:send_event(?NAME, Str).

%% ------------------------------------------------------------------
%% gen_fsm Function Definitions
%% ------------------------------------------------------------------

init([]) ->
    io:format("Packet assembler starting~n"),
    {ok, waiting, nil}.

waiting(N, nil) ->
    {next_state, collecting, {N, 0, []}}.

collecting(Buff0, {Need, Len, Buff1}) ->
    L = length(Buff0),
    if 
        L + Len < Need ->
            {next_state, collecting, {Need, Len+L, Buff1++Buff0}};
        L + Len =:= Need ->
            Buff = Buff1 ++ Buff0,
            io:format("Got data:~s~n", [Buff]),
            {next_state, waiting, nil}
    end.

handle_event(_Event, StateName, State) ->
    {next_state, StateName, State}.

handle_sync_event(_Event, _From, StateName, State) ->
    {reply, ok, StateName, State}.

handle_info(_Info, StateName, State) ->
    {next_state, StateName, State}.

terminate(Reason, _StateName, _State) ->
    io:format("Packet assembler terminated:~p~n", [Reason]),
    ok.

code_change(_OldVsn, StateName, State, _Extra) ->
    {ok, StateName, State}.

%% ------------------------------------------------------------------
%% Internal Function Definitions
%% ------------------------------------------------------------------

