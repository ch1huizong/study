-module(web_server).
-export([web_server/1]).

web_server(Client) ->
	receive
		{Client, {get, Page}} ->
			case file:read(Page) of
				{ok, Bin} ->
					Client ! {self(), Bin};
				{error, _} ->
					Client ! {self(), error}
			end,
			web_server(Client)
	end.
