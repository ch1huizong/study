-module(mytimer).
-export([timer/0, timer/1]).

timer() ->
	spawn(mytimer, timer,[self()]),
	receive
		timeout -> io:format("Received timeout!~n",[])
	end.			

timer(Pid) ->
	receive
	after
		5000 ->
			Pid ! timeout
	end.			

