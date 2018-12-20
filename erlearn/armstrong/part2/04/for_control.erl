-module(for_control).
-export([test/0, for/3]).

test() ->
    L1 = for(1,10,fun(I) -> I end),
    L2 = for(1,10, fun(I) -> I*I end),
    {L1,L2}.

for(Max, Max, F) -> [F(Max)];
for(I, Max, F) -> [F(I)|for(I+1,Max, F)].
