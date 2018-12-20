-module(pmaps).
-import(lists,[map/2, foreach/2]).

-export([pmap/2, pmap1/2, pmap/3, pmap/4, pmap1/4]).

pmap(F, L) -> 
    S = self(),
    %% make_ref() returns a unique reference
    %%   we'll match on this later
    Ref = erlang:make_ref(), 
    Pids = map(fun(I) -> 
		       spawn(fun() -> do_f(S, Ref, F, I) end)
	       end, L),
    %% gather the results
    gather(Pids, Ref).

do_f(Parent, Ref, F, I) ->					    
    Parent ! {self(), Ref, (catch F(I))}.
gather([Pid|T], Ref) ->
    receive
	{Pid, Ref, Ret} -> [Ret|gather(T, Ref)]
    end;
gather([], _) ->
    [].

pmap1(F, L) -> 
    S = self(),
    Ref = erlang:make_ref(),
    foreach(fun(I) -> 
		    spawn(fun() -> do_f1(S, Ref, F, I) end)
	    end, L),
    %% gather the results
    gather1(length(L), Ref, []).

do_f1(Parent, Ref, F, I) ->					    
    Parent ! {Ref, (catch F(I))}.

gather1(0, _, L) -> L;
gather1(N, Ref, L) ->
    receive
	{Ref, Ret} -> gather1(N-1, Ref, [Ret|L])
    end.

pmap(F, L, Max) -> void.

pmap(Nodes,F, L, Max) -> void.

pmap1(Nodes, F, L, Max) -> void.



