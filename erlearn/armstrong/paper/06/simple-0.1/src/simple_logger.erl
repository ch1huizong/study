-module(simple_logger).
-behaviour(gen_event).

-export([start/0, stop/0, log/1, report/0]).

-export([init/1, terminate/2, handle_event/2, handle_call/2, 
        handle_info/2,code_change/3]).

-define(NAME, my_simple_event_logger).

%=====================================================================
%  API
%=====================================================================

start() ->
    case gen_event:start_link({local, ?NAME}) of
        Ret = {ok, _Pid} ->
            gen_event:add_handler(?NAME, ?MODULE,[]),
            Ret;
        Other ->
            Other
    end.

stop() ->
    gen_event:stop(?NAME).

log(E) ->
    gen_event:notify(?NAME,{log, E}).

report() ->
    gen_event:call(?NAME, ?MODULE, report).


%=====================================================================
%  callback
%=====================================================================
init([]) -> 
    io:format("Logger starting~n"),
    {ok, []}.

handle_event({log, E}, S) -> {ok, trim([E|S])}.

handle_call(report, S) -> {ok, S, S}.

handle_info(_Info, S) -> {ok, S}.
   
terminate(stop, _) -> true.

code_change(_Old, S, _Extra) -> {ok, S}.

trim([X1, X2, X3, X4, X5 | _]) -> [X1,X2,X3,X4,X5];
trim(L) -> L.
