-module(job_centre).

-behaviour(gen_server).
-export([start_link/0, add_job/1, work_wanted/0, job_done/1]).

%% gen_server callbacks
-export([init/1, handle_call/3, handle_cast/2, handle_info/2,
	 terminate/2, code_change/3]).
-define(SERVER,?MODULE).

start_link() -> gen_server:start_link({local, ?SERVER}, ?MODULE, [], []).
add_job(F) -> gen_server:call(?SERVER,{add, F}).
work_wanted() -> gen_server:call(?SERVER,del).
%%	{jobNumber,F} | no.
job_done(JobNumber) -> ok.


init([]) -> {ok, [{number,0}]}.

handle_call({add, F}, _From, State) ->
	{number, N} = lists:keyfind(number,1,State),
	Update = lists:keyreplace(number,1,State,{number,N + 1}),
	{reply, N+1, [{N+1,F}|Update]};

handle_call(del, _From, State) ->
	Reply = case lists:keyfind(number,1,State) of
				{_,N} when N > 0 ->
			
			end;

	
	




handle_cast(_Msg, State) -> {noreply, State}.
handle_info(_Info, State) -> {noreply, State}.
terminate(_Reason, _State) -> ok.
code_change(_OldVsn, State, Extra) -> {ok, State}.
