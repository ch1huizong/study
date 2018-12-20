-module(packet).
-export([term_to_packet/1, packet_to_term/1, test/0]).

% 先后？
term_to_packet(Term) ->
	B = term_to_binary(Term),
	N = byte_size(B),
	<<N:32,B/binary>>.

packet_to_term(<<_N:32,B/binary>>) ->
	binary_to_term(B).

test() ->
	T = {a,b,c,[1,2,3,"hello"]},
	packet_to_term(term_to_packet(T)).

