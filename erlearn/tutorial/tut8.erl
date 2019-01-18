-module(tut8).
-export([reverse/1]).

reverse(List) ->
    reverse(List, []).

reverse([Head| Rest], Reversed_list) ->
    reverse(Rest, [Head | Reversed_list]);
reverse([], Reversed_list) ->
    Reversed_list.
