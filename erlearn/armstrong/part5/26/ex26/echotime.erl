-module(echotime).
-export([test/1]).
-import(lists, [map/2, reverse/1]).

-import(lib_misc,[pmap1/2]).
-import(web_profiler,[ping/2]).

test(Hosts) ->
    {ok, S} = file:open(Hosts, read),
    Urllist = readlines(S,[]),
    %Result = map(fun(I) -> ping(I, 30) end,Urllist),
    Result = pmap1(fun(I) -> ping(I, 30) end,Urllist),
    Result.

readlines(S, L) ->
    case io:get_line(S, '') of
        eof -> 
            file:close(S),
            reverse(L);
        Line -> 
            Line1 = lists:droplast(Line),
            readlines(S, [Line1 | L])
    end.
