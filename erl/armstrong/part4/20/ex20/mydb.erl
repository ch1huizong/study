-module(mydb).
-compile(export_all).

-include_lib("stdlib/include/qlc.hrl").

-record(users,{name, email, password}).
-record(tips, {url, description, checkdate}).
-record(abuse,{ip, visits}).

%% 建立数据库
init_all_nodes(NodeList) ->
	io:format("Initiating Databases on ~p...~n",[NodeList]),
	mnesia:create_schema(NodeList),
    rpc:multicall(NodeList,mnesia,start,[]), % 全部启动
	mnesia:create_table(users, [{attributes, record_info(fields, users)},
                                {disc_copies, NodeList}	
								]),
	mnesia:create_table(tips,  [{attributes, record_info(fields, tips)},
                                {disc_copies, NodeList}	
								]),
	mnesia:create_table(abuse, [{attributes, record_info(fields, abuse)},
                                {disc_copies, NodeList}	
								]),
	io:format("Initiated.~n").

%% 开启本节点 
start() ->
	io:format("Starting Local database...~n"),
	mnesia:wait_for_tables([users,tips,abuse],20000),
	io:format("Database has been already...~n").

example_tables() ->
	[
		%% users
		{users, che, 'chehuizong@163.com', quiet},
		{users, root, 'root@admin.com', quiet},
		{users, admin, 'admin@163.com', quiet},
		%% tips
		{tips,'http://book.erlangsnippet.com' ,'books about of erlang',20160921},
		{tips,'http://news.erlangsnippet.com', 'erlang snippet news', 20160929},
		%% abuse
		{abuse,'192.168.1.1',17},
		{abuse,'192.168.1.255',18},
		{abuse,'192.168.1.111',29}
	].

%% 重置
reset_tables() ->
	io:format("Clear tables...~n"),
	mnesia:clear_table(users),
	mnesia:clear_table(tips),
	mnesia:clear_table(abuse),
	io:format("Complete clear.~n"),

	F = fun() -> lists:foreach(fun mnesia:write/1,example_tables()) end,
	mnesia:transaction(F).

%% 查询
do(Q) ->
	F = fun() -> qlc:e(Q) end,
	{atomic, Val} = mnesia:transaction(F),
	Val.
	
select_all(Tab) ->
	do(qlc:q([ X  || X  <- mnesia:table(Tab)])).

%% need lookup abuse
select_evil() -> ok.

%% 增加
add_users_item(Name,Email,Password) ->
	Row = #users{name=Name,email=Email, password=Password},
	F = fun() -> mnesia:write(Row) end,
	mnesia:transaction(F).

add_tips_item(Url, Desc, Date) ->
	Row = #tips{url=Url, description=Desc, checkdate=Date},
	F = fun() -> mnesia:write(Row) end,
	mnesia:transaction(F).

add_abuse_item(Ip,Visits) ->
	Row = #abuse{ip=Ip,visits=Visits},
	F = fun() -> mnesia:write(Row) end,
	mnesia:transaction(F).
