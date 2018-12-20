-module(simple_app).
-behaviour(application).

-export([start/2, stop/1]).

start(_, _) -> simple_sup:start().

stop(_) -> ok.
    
