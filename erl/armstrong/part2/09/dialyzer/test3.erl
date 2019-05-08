-module(test3).
-export([test/0, fac/1]).

test() -> fac(-5).

fac(0) -> 1;
fac(N) -> N * fac(N-1).
