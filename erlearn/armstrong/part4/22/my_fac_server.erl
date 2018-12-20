-module(my_fac_server).
-export([loop/0]).

loop() ->
    receive
        {From, {fac,N}} ->
            From ! {self(), fac(N)},
            loop();
        {become, Sth} ->  % 若运行需改写server5中rpc接口
            Sth()
    end.

fac(0) -> 1;
fac(N) -> N * fac(N-1).
