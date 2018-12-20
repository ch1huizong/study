-module(myfuns).
-export([map_search_pred/2]).

map_search_pred(Map,Pred) ->
	T = maps:to_list(Map),
	map_search_pred1(T, Pred).

map_search_pred1([], _) -> not_found;
map_search_pred1([{Key, Value}| T],Pred) ->
	case Pred(Key,Value) of
		true -> {Key, Value};
		false -> map_search_pred1(T,Pred)
	end.

		
