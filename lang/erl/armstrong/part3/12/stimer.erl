-module(stimer).
-export([start/2, cancel/1]).

start(Time, Fun) -> spawn(fun() -> timer(Time, Fun) end).
cancel(Pid) -> Pid ! cancel.

timer(Time, Fun) -> 
    receive
        cancel ->	%% 取消部分
            void
    after Time ->  %% 定时部分
            Fun()
    end.
