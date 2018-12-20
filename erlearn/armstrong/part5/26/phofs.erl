-module(phofs).
-export([mapreduce/4]).
-import(lists,[foreach/2]).

%% 注意F1(Pid, X) -> 发送{Key, Val} 消息到Pid
%% F2(Key,[Val], AccIn(多一半Acc0)) -> AccOut
%% L = [X]

%% mapreduce框架
%% 涉及三种进程：主控进程，reduce进程，map进程
%%
%% 主控进程,等待reduce结果
mapreduce(F1, F2, Acc0, L) ->
    S = self(),
    Pid = spawn(fun() -> reduce(S, F1, F2, Acc0, L) end),
    receive
        {Pid, Result} -> Result
    end.

%% reduce进程,收集和整理
reduce(Parent, F1, F2, Acc0, L) ->
    process_flag(trap_exit, true),
    ReducePid = self(),
    foreach(fun(X) -> spawn_link(fun() -> do_job(ReducePid, F1, X) end)
            end,L),
    N = length(L),
    Dict0 = dict:new(),
    Dict1 = collect_replies(N, Dict0),  %% 收集各个子进程结果,返回新字典
    Acc = dict:fold(F2, Acc0, Dict1),   %% 对结果操作
    Parent ! {self(), Acc}.

%% reduce收集函数
collect_replies(0, Dict) ->
    Dict;
collect_replies(N, Dict) ->
    receive
        {Key, Val} ->
            case dict:is_key(Key,Dict) of
                true ->
                    Dict1 = dict:append(Key,Val, Dict),
                    collect_replies(N, Dict1); %% 还必须是N
                false ->
                    Dict1 = dict:store(Key, [Val], Dict),
                    collect_replies(N, Dict1)
            end;
        {'EXIT', _, _Why} ->  %一个进程结束了
            collect_replies(N-1, Dict)
    end.

%% map函数，F必须发送{Key, Value}到Pid,然后终止
do_job(ReducePid, F, X) ->
    F(ReducePid, X).

%% 三个dict函数,store, append, fold

