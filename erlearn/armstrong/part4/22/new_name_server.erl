-module(new_name_server).
-export([init/0, add/2, find/1, all_names/0, delete/1, handle/2]).
-import(server3, [rpc/2]).

%%客户端方法
all_names() -> rpc(name_server, allNames).
add(Name,Place) -> rpc(name_server, {add, Name, Place}).
delete(Name) -> rpc(name_server, {delete, Name}).
find(Name) -> rpc(name_server, {find, Name}).

%%回调方法
init() -> dict:new().
handle(allNames, Dict) -> {dict:fetch_keys(Dict), Dict}; % new 
handle({add, Name, Place},Dict) -> {ok, dict:store(Name, Place, Dict)};
handle({delete,Name}, Dict) -> { ok, dict:erase(Name,Dict) }; % new
handle({find, Name},Dict) -> { dict:find(Name,Dict), Dict }.
