-module(motor_controller).
-export([add_event_handler/0]).

%% 自定义事件处理器模块
add_event_handler() ->
    event_handler: add_handler(errors, fun controller/1).

%% 自定义处理函数
controller(too_hot) ->
    io:format("Turn off the monitor~n");
controller(X) ->
    io:format("~w  ignored event: ~p~n",[?MODULE, X]).
