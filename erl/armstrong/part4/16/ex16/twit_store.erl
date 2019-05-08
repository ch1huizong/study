-module(twit_store).
-export([init/1, store/2, fetch/1]).

init(K) -> ok.

store(N,Buf) -> 
	{ok, S} = file:open("twit_store.data",[write,raw, binary]),
	file:pwrite(S,(N-1)*140,<<Buf:140/binary>>),
	file:close(S).

fetch(N) ->
	{ok, S} = file:open("twit_store.data",[read,raw, binary]),
	Bin = file:pread(S,(N-1)*140, 140),
	io:format("N-th twiter is ~s~n",binary_to_list(Bin)).


