-module(my_builtin).
-export([my_tuple_to_list/1, my_time_func/1]).

my_tuple_to_list(T) ->
    End = tuple_size(T),
    my_tuple_to_list(End, T, []).

my_tuple_to_list(0, _T, Acc) -> Acc;
my_tuple_to_list(Length, T, Acc) ->
    my_tuple_to_list(Length-1, T, [element(Length, T)| Acc]).


my_time_func(F) ->
	T1 = erlang:monotonic_time(),
    F(),
	T2 = erlang:monotonic_time(),
    T2 - T1.
