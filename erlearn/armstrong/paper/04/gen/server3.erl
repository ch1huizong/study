-module(server3).

-export([start/3, stop/1, rpc/2, swap_code/2]).

start(Name, F, State) ->
	register(Name, 
			spawn(fun() -> 
						loop(Name, F, State)
				end)).

stop(Name) -> Name ! stop.

swap_code(Name, F) -> rpc(Name, {swap_code, F}).

rpc(Name, Q) ->
	Name ! {self(), Q},
	receive
		{Name, crash} -> exit(rpc);
		{Name, ok, Reply} -> Reply
	end.


loop(Name, F, State) ->
	receive 
		stop -> 
			void;
		{From, {swap_code, F1}} ->
			From ! {Name, ok, ack},
			loop(Name, F1, State);
		{From, Q} -> 
			case (catch F(Q, State)) of
				{'EXIT', Why} ->
					log_error(Name, Q, Why),
					From ! {Name, crash},
					loop(Name, F, State);
				{Reply, State1} ->
					From ! {Name, ok, Reply},
					loop(Name, F, State1)
			end
	end.

log_error(Name, Q, Why) ->
	io:format("Server ~p query ~p caused exception ~p~n",
			[Name, Q, Why]).
