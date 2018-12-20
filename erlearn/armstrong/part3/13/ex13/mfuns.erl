-module(mfuns).
-export([my_spawn1/3, my_spawn2/3, my_spawn3/4,live/1,
        keep_alive/2, keep_mylive/1, restart_all/1, restart_one/1]).


on_exit(Pid, Fun) ->
    spawn(fun() ->
			  Ref = monitor(process,Pid),
			  receive
				  {'DOWN', Ref, process, Pid, Why} ->
					  Fun(Why)
			  end
          end).


keep_alive(Name,Fun) ->
    register(Name, Pid=spawn(Fun)),
    on_exit(Pid, fun(_Why) -> keep_alive(Name,Fun) end).


my_spawn1(Mod, Func, Args) ->
	statistics(wall_clock),
	{Pid, Ref} = spawn_monitor(Mod, Func, Args),
	receive
		{'DOWN', Ref, process, Pid, Why} ->
			{_, T} = statistics(wall_clock),
			io:format("~p died with ~p, alive in ~p microseconds~n",[Pid, Why, T* 1000])
	end.


my_spawn2(Mod, Func, Args) ->
	statistics(wall_clock),
	Pid = spawn(Mod, Func, Args),
	on_exit(Pid,fun(Why) -> 
				{_, T} = statistics(wall_clock),
				io:format("~p died with ~p, alive in ~p microseconds~n",[Pid, Why, T* 1000])
			end).


my_spawn3(Mod, Func, Args, Time) ->
	Pid = spawn(Mod,Func, Args),
	receive
	after 
		Time * 1000 -> exit(Pid, kill)
	end.


live(Name) ->  % 公共进程
	register(Name, spawn(fun() -> live1() end)).

live1() ->
	receive
	after 5000 ->
		io:format("I'm running!~n"),
		live1()
	end.

keep_mylive(Name) ->   % 监视进程,与公共进程单独的1
	on_exit(whereis(Name), fun(_Why) -> live(Name) end).


%% restart缺少test
%%

restart_all(Fs) -> 
    spawn(fun() -> 
            Fl = [ spawn_monitor(F) || F <- Fs],
            loop1(Fl,Fs)
          end).

loop1(Fl,Fs) ->
	receive
		{'DOWN', _Ref, process, _Pid, _Why} ->
            lists:foreach(fun({P, _R}) -> exit(P,kill) end,Fl),
            restart_all(Fs)
	end.


restart_one(Fs) -> 
    spawn(fun() -> 
            Fl = [ {F,spawn_monitor(F)} || F <- Fs],
            loop2(Fl)
        end).

loop2(Fl) ->
	receive
		{'DOWN', Ref, process, Pid, _Why} ->
            {F,_} = lists:keyfind({Pid, Ref},2, Fl),
            New = spawn_monitor(F),
            Nl = lists:keyreplace(F,1, Fl, New),
            loop2(Nl)
	end.
