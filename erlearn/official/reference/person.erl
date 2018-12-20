-module(person).
-export([new/2]).

-record(person, {name, age}).

new(Name, Age) ->
	#person{name=Name, age=Age}.
