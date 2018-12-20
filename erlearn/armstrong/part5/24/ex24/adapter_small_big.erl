-module(adapter_small_big).
-export([new/1, store/3, lookup/2]).

%% 缺少判断值大小函数

new(small) ->
	Td = ets:new(?MODULE,[set,named_table]),
    {?MODULE, small, Td};
new(big) ->
	{ok, Table} = dets:open_file(?MODULE,[{file, "bigdata"}]),
	{?MODULE, big,Table }.

store(Key, Val, {_, small, E})  ->
	ets:insert(E,{Key, Val}),
	{?MODULE, small, E};
store(Key, Val, {_, big, T}) ->
	dets:insert(T,{Key,Val}),
	{?MODULE, persistent, T}.


lookup(Key, {_, small, E}) ->
	case ets:lookup(E,Key) of 
		[] -> error;
		[{_,Val}] -> {ok, Val}
	end;
lookup(Key,{_,big, T}) ->
	case dets:lookup(T,Key) of 
		[] -> error;
		[{_,Val}] -> {ok, Val}
	end.

%%  内存和磁盘,利用上
put(Key,memory, Val) ->  void;

put(Key,disk, Val) -> ok.

