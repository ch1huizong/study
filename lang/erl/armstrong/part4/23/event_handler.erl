-module(event_handler).
-export([make/1, add_handler/2, event/2]).

%% 客户端-服务器架构
%% client部分
make(Name) -> register(Name, spawn(fun() -> my_handler(fun no_op/1) end)).

%% 增加事件处理函数
add_handler(Name, Fun) ->  Name ! {add, Fun}.

%% 生成一个事件
event(Name, X) -> Name ! {event, X}.

%% server部分
my_handler(Fun) ->  % Fun初始化
    receive
        {add, Fun1} ->
            my_handler(Fun1);
        {event, Any}  ->
            (catch Fun(Any)), %%事件处理
            my_handler(Fun)
    end.

no_op(_) -> void.
