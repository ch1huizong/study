-module(web).
-export([serve/1]).

serve(Client) ->
    receive
        {Client, close} ->
            true;
        {Client, Request} ->
            Response = generate_response(Request),
            Client ! {self(), Response},
            serve(Client)   % 提供持久链接
    after 10000 ->
            Client ! {self(), close}

    end.
