-module(clock).
-export([start/2, stop/0]).

start(Time, Fun) ->
    register(clock, spawn(fun() -> tick(Time, Fun) end)).

stop() -> clock ! stop.

tick(Time, Fun) ->
    receive
        stop -> 
            void
    after Time ->
        Fun(),          % 正式调用
        tick(Time, Fun)
    end.
