-module(my_module).
-compile(export_all).

print(Term) ->
	io:format("The value of Term is: ~w.~n", [Term]).

either_or_both(true, B) when is_boolean(B) ->
	true;
either_or_both(A, true) when is_boolean(A) ->
	true;
either_or_both(false, false) ->
	false.

%% 互斥
area({circle, Radius}) ->
	Radius * Radius * 3.14;
area({rectangle, Height, Width}) ->
	Height * Width;
area({square, Side}) ->
	Side * Side.

yesno(F) ->
    case F(true,false) of
		true -> io:format("yes~n");
		false -> io:format("no~n")
	end.

test() ->
	%yesno(either_or_both). % 直接引用函数做参数
	yesno(fun either_or_both/2).

%% 非尾递归
sum(0) -> 0;
sum(N) -> sum(N-1) + N.

%% 尾递归版本
do_sum(N) -> do_sum(N, 0).
do_sum(0, Total) -> Total;
do_sum(N, Total) -> do_sum(N-1, Total + N).
