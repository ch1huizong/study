-module(math_functions).
-include_lib("eunit/include/eunit.hrl").

-export([even/1, odd/1, filter/2, 
         split1/1, split2/1,odds_and_evens/3
        ]).

even(X) when is_integer(X) ->
    case (X rem 2) of
        0 -> true;
        1 -> false
    end.

odd(X) when is_integer(X) ->
    case (X rem 2) of
        0 -> false;
        1 -> true
    end.

filter(F,[H|T]) ->  
    case F(H) of
        true -> [ H | filter(F,T) ];
        false -> filter(F,T) 
    end;
filter(_,[]) -> [].


split1(L) ->  % method1
    Odds = filter(fun odd/1,L),
    Evens = filter(fun even/1,L),
    {Odds, Evens}.

split2(L) -> % method2
    odds_and_evens(L,[],[]).

odds_and_evens([H|T],Odds,Evens) ->
    case (H rem 2) of
        0 -> odds_and_evens(T,Odds, [H|Evens]);
        1 -> odds_and_evens(T, [H|Odds], Evens)
    end;
odds_and_evens([], Odds, Evens) ->
    { lists:reverse(Odds), lists:reverse(Evens) }.

split_test() ->
	L = lists:seq(1,10),
    Result1 = split1(L),
    Result2 = split2(L),
    Result1 = Result2,
    ok.
