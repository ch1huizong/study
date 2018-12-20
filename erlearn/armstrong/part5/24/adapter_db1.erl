-module(adapter_db1).
-export([new/1, store/3, lookup/2]).

%% 通过元组模块的概念
%% 适配器模式，提供统一接口(不同实现)

new(dict) ->
    {?MODULE, dict, dict:new()};
new(lists) ->
    {?MODULE, list, []};
new(persistent) ->
	{ok, Table} = dets:open_file(?MODULE,[{file, "data"}]),
	{?MODULE, persistent,Table }.

store(Key, Val, {_, dict, D})  ->
    D1 = dict:store(Key, Val, D),
    {?MODULE, dict, D1};
store(Key, Val, {_, list, L})  ->
    L1 = lists:keystore(Key,1,L,{Key, Val}),
    {?MODULE, list, L1};
store(Key, Val, {_, persistent, T}) ->
	ok = dets:insert(T,{Key,Val}),
	{?MODULE, persistent, T}.


lookup(Key, {_, dict, D}) ->
    dict:find(Key, D);
lookup(Key, {_, list, L}) ->
    case lists:keysearch(Key, 1, L) of
        {value, {Key, Val}} -> {ok, Val};
        false               -> error
    end;
lookup(Key,{_,persistent, T}) ->
	case dets:lookup(T,Key) of 
		[] -> error;
		[{_,Val}] -> {ok, Val}
	end.

