-module(count).
-export([open/1, close/0, me/2, lookup/2]).

%% 关键是应用情景？
open(File) ->
	io:format("DETS opened:~p~n",[File]),
	Bool = filelib:is_file(File),
	case dets:open_file(?MODULE,[{file,File}]) of  %%主要是open_file语句
		{ok, ?MODULE} ->   
			case Bool of        %% 新建的，还是已经存在的？
				true -> void;
				false -> ok = dets:insert(?MODULE,[ {{?MODULE,0},0} ])
			end,
			true;
		{error, Reason} ->
			io:format("Can't open DETS table~n"),
			exit({error, File,Reason})  
	end.

close() -> dets:close(?MODULE).

me(Mod, Line) ->
	case dets:lookup(?MODULE,{Mod,Line}) of
		[{_,N}] ->
			dets:insert(?MODULE,[{{Mod,Line},N+1}]),
			N;
		[] ->
			dets:insert(?MODULE,[{{Mod,Line},1}])
	end.

%% client
lookup(Mod,Line) ->
	case dets:lookup(?MODULE,{Mod,Line}) of
		[{_,N}] -> N;
		[] -> no_exist
	end.
