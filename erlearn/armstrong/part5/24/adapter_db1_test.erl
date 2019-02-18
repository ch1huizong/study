-module(adapter_db1_test).
-export([test/0]).
-import(adapter_db1,[new/1, store/2, lookup/1]).

test() ->
    %% 测试dict模块
    M0 = new(dict),
    M1 = M0:store(key1, val1),
    M2 = M1:store(key2, val2),
    {ok, val1} = M2:lookup(key1),
    {ok, val2} = M2:lookup(key2),
    error = M2:lookup(nokey),

    %% 测试lists模块
    N0 = new(lists),
    N1 = N0:store(key1, val1),
    N2 = N1:store(key2, val2),
    {ok, val1} = N2:lookup(key1),
    {ok, val2} = N2:lookup(key2),
    error = N2:lookup(nokey),

	%% 测试dets模块
    D0 = new(persistent),
    D1 = D0:store(key1, val1),
    D2 = D1:store(key2, val2),
    {ok, val1} = D2:lookup(key1),
    {ok, val2} = D2:lookup(key2),
    error = D2:lookup(nokey),
    ok.


