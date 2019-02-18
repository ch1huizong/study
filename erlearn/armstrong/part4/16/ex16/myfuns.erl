-module(myfuns).
-compile(export_all).
-import(lib_find,[files/3,files/5]).

is_recompiled(Filename) -> 
	Sdate = filelib:last_modified(Filename),
	Beamfile = filename:basename(Filename,".erl") ++ ".beam",
	Bdate = filelib:last_modified(Beamfile),
	case Bdate >= Sdate of
		true ->
			not_need_recompiled;
		_ -> 
			yes_need_recompiled
	end.
			


small_md5(Filename) -> 
	case file:read_file(Filename) of
		{ok, Bin} -> 
			erlang:md5(Bin);
		{error, Reason} -> 
			Reason
	end.

big_md5(Filename) -> 
	case file:open(Filename,[read,binary, raw]) of
		{ok, S} ->
			C = erlang:md5_init(),
			cal_big_md5(C,S);
		{error,_} -> io:format("Can't open file:~p~n.",[Filename])
	end.

cal_big_md5(Context, Fd) ->
	case file:read(Fd,1024) of
		{ok, Block} ->
			NewContext = erlang:md5_update(Context,Block),
			cal_big_md5(NewContext,Fd);
		eof ->
			file:close(Fd),
			erlang:md5_final(Context);
		{error, Reason} ->
			Reason
	end.


%% 使用的是进程空间
cached(Filename) ->
	case get(Filename) of
		{Md5, Last_modified_time} -> 
			Modified_time = filelib:last_modified(Filename),
			case Modified_time > Last_modified_time of
				true ->
					put(Filename,{small_md5(Filename),Modified_time}),
					io:format("~p md5 updated.~n",[Filename]);
				_ ->
					Md5
			end;
		undefined -> 
			Last_modified_time = filelib:last_modified(Filename), %% Filename在文件系统存在,前提
			put(Filename,{small_md5(Filename), Last_modified_time}),
			io:format("~p md5 created.~n",[Filename])
	end.

%%上面，使用文件

			
	
	
	

