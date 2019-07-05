-module(mfuns).
-compile(export_all).

most() ->
	Mlist = [{M,length(M:module_info(exports))} || {M,_} <- code:all_loaded() ],
	Nlist = lists:keysort(2,Mlist),
	lists:last(Nlist).

all_funs() ->
    D0 = dict:new(),
    Funs = [{Key, M} || {M, _} <- code:all_loaded(), Key <- M:module_info(exports)],
    D1 = register_funs(Funs, D0),
    D1.

register_funs([], D0) -> D0;
register_funs([{Key, M} | T ], D0) ->
    D1 = dict:update(Key, fun(Old) -> Old ++ [M] end, [M], D0),
    register_funs(T, D1).
           


