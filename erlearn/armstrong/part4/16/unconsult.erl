-module(unconsult).
-export([unconsult/2]).

%% 把数据列表写入文件
unconsult(File,L) ->
    {ok, S} = file: open(File, write),
    lists:foreach(fun(X) -> io:format(S,"~p.~n",[X]) end,L),
    file:close(S).
