-module(myfuns).
-compile(export_all).

my_tuple_to_list(T) ->
    End = tuple_size(T),
    my_tuple_to_list(End, T, []).

my_tuple_to_list(0, _T, Acc) -> Acc;
my_tuple_to_list(Length, T, Acc) ->
    my_tuple_to_list(Length-1, T, [element(Length,T)| Acc]).


my_time_func(F) ->
	T1 = now(),
    F(),
	T2 = now(),
	timer:now_diff(T2,T1)/1000000.



				




