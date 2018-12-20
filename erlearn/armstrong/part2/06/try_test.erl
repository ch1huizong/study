-module(try_test).
-export([gen_exception/1, catcher/1, demo1/0, demo2/0,demo3/0]).

gen_exception(1) -> a;
gen_exception(2) -> throw(a);
gen_exception(3) -> exit(a);
gen_exception(4) -> {'EXIt', a};
gen_exception(5) -> error(a).

catcher(N) ->
    try gen_exception(N) of
        Val -> {N, normal, Val}  % without "
    catch
        throw: X -> {N, caught, thrown, X};
        exit: X -> {N, caught, exited, X};
        error: X -> {N, caught, error, X}
    end.

demo1() ->
    [ catcher(I) || I <- [1,2,3,4,5] ].

demo2() ->
    [ {I, (catch gen_exception(I))} || I <- [1,2,3,4,5]].

demo3() ->
    try gen_exception(5)
    catch
        error: X -> {X, erlang:get_stacktrace()}
    end.


