-module(maps_fun).
-compile(export_all).

map_search_pred(Map, Pred) ->
	lists:map(fun ({Key, Value}) -> Pred(Key, Value) end, maps:to_list(Map)).
