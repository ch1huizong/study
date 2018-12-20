-module(sc_element).

-behaviour(gen_server).

-export([
        start_link/2,
        create/2,
        create/1,
        fetch/1,
        replace/2,
        delete/1
    ]).

-export([init/1, handle_call/3, handle_cast/2, handle_info/2,
        terminate/2, code_change/3 ]).

-import(sc_event, [expire/0]).

-define(SERVER, ?MODULE).
-define(DEFAULT_LEASE_TIME, 120).

-record(state, {value, lease_time, start_time}).

start_link(Value, LeaseTime) ->
    gen_server:start_link(?MODULE, [Value, LeaseTime],[]).

create(Value, LeaseTime) ->
    sc_element_sup:start_child(Value, LeaseTime). 

create(Value) ->
    sc_element_sup:start_child(Value,?DEFAULT_LEASE_TIME).

fetch(Pid) ->
    gen_server:call(Pid, fetch).

replace(Pid, Value) ->
    gen_server:cast(Pid, {replace, Value}).

delete(Pid) ->
    gen_server:cast(Pid, delete).

%% 实现的回调函数
init([Value, LeaseTime]) ->
    Now = calendar:local_time(),
    StartTime = calendar:datetime_to_gregorian_seconds(Now),
    {ok,
    #state{value = Value,
            lease_time = LeaseTime,
            start_time = StartTime },
    time_left(StartTime, LeaseTime)
    }.

time_left(_StartTime, infinity) ->
    infinity;
time_left(StartTime, LeaseTime) ->
    Now = calendar:local_time(),
    CurrentTime = calendar:datetime_to_gregorian_seconds(Now),
    TimeElapsed = CurrentTime - StartTime,
    case LeaseTime - TimeElapsed of
        Time when Time =< 0  ->  0;
        Time -> Time * 1000
    end.

handle_call(fetch, _From, State) ->
    #state{value = Value,
            lease_time = LeaseTime,
            start_time = StartTime } = State,
    TimeLeft = time_left(StartTime, LeaseTime),
    {reply, {ok, Value}, State, TimeLeft}.
   
handle_cast({replace, Value}, State) ->
    #state{
            lease_time = LeaseTime,
            start_time = StartTime } = State,
    TimeLeft = time_left(StartTime, LeaseTime),
    {noreply,State#state{value = Value}, TimeLeft};
handle_cast(delete, State) ->
    {stop, normal, State}.

handle_info(timeout, State) ->
    sc_event:expire(),    % 缓存过期投递事件,我可以怎么一个反向查询Key?
    {stop, normal, State}.

terminate(_Reason, _State) ->  % 从表中删除次进程项
    sc_store:delete(self()).

code_change(_OldVsn, State, _Extra) ->
    {ok, State}.
