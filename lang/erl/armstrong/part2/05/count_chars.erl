-module(count_chars).
-export([count/1]).


count(Str) -> count(Str, #{}).

count([H|T], #{ H := N }=X) ->  
	count(T, X#{ H := N+1 });
count([H|T], X) ->
	count(T, X#{ H => 1 });
count([], X) ->
	X.
