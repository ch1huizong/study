-module(user_default).
-compile(export_all).

hello() ->
    "Hello World.".

away(Time) ->
    io: format("I is away and will be back in ~w minutes ~n",
               [Time]).
