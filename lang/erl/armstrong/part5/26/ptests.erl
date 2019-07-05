-module(ptests).
-export([tests/1, fib/1]).
-import(lists, [map/2]).
-import(lib_misc,[pmap/2]).

%% 三个变量，调度器，问题，函数

tests([N]) ->  % 调读器
    Nsched = list_to_integer(atom_to_list(N)),
    run_tests(1, Nsched).

% 主控
run_tests(N, Nsched) ->
    case test(N) of
        stop -> 
            init:stop();
        Val ->
            io:format("~p.~n", [{Nsched,Val}]),
            run_tests(N+1,Nsched)
    end.

%% 问题1
test(1) -> 
    %% 生产包含100个列表的列表，每个列表包含1000随机数
    seed(), % seed固定了
    S = lists:seq(1,100),
    L = map(fun(_) -> mkList(1000) end,S),
    {Time1, S1} = timer:tc(lists, map, [fun lists:sort/1,  L]),    % 比较函数不同
    {Time2, S2} = timer:tc(lib_misc, pmap, [fun lists:sort/1,  L]),
    {sort, Time1, Time2,  equal(S1,S2)};

test(2) ->
    %%  L = [27,27...] 共100个
    L = lists:duplicate(100,27),
    {Time1, S1} = timer:tc(lists, map, [fun ptests:fib/1,  L]),
    {Time2, S2} = timer:tc(lib_misc, pmap, [fun ptests:fib/1,  L]),
    {fib, Time1, Time2,  equal(S1,S2)};

test(3) ->
    stop.

equal(S, S) -> true;
equal(S1, S2) -> {differ, S1, S2}.

fib(0) -> 1;
fib(1) -> 1;
fib(N) -> fib(N-1) + fib(N-2).

%%重置随机数生成器
seed() -> random: seed(44,55,66).

%% 生成K个随机数的,列表
mkList(K) -> mkList(K, []).

mkList(0,L) -> L;
mkList(N,L) -> mkList(N-1, [random:uniform(1000000) | L]).
