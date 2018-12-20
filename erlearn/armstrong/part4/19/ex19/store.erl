-module(store).
-export([store/1]).

%% 并非所有的模块,只是内置模块
store(ets) ->
	io:format("Creating ETS table...~n"),
	Tid = ets:new(et,[bag]),
	store1(code:all_loaded(),Tid,ets),
	io:format("Complete ETS table!~n"),
	Tid;
store(dets) ->
	io:format("Creating DETS table...~n"),
	{ok, Tname} = dets:open_file(dt,[{type,bag},{file,"./data.dat"}]),
	store1(code:all_loaded(),Tname,dets),
	io:format("Complete DETS table!~n"),
	dets:close(Tname).


store1([{M, _}|T],Tab,ets) ->
	lists:foreach(fun(Key) -> ets:insert(Tab,{Key,M}) end, M:module_info(exports)),
	store1(T, Tab,ets);

store1([{M, _}|T],Tab,dets) ->
	lists:foreach(fun(Key) -> dets:insert(Tab,{Key,M}) end, M:module_info(exports)),
	store1(T, Tab,dets);

store1([],_,_) -> ok.
