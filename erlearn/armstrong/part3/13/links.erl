-module(links).
-compile(export_all).


%% 若Pid进程终止，监视者进程执行Fun函数
on_exit(Pid, Fun) ->
    spawn(fun() ->
                  Ref = monitor(process,Pid),
                  receive
                      {'DOWN', Ref, process, Pid, Why} ->
                          Fun(Why)
                  end
		 end).


%% 让一组进程共同终止
start(Fs) ->
    spawn(fun() -> 
			[ spawn_link(F) || F <- Fs],
            receive 
				after 
					infinity -> true 
            end
		end). % 共同父亲进程无期限等待


%% 生成一个永不终止的进程
%% bug:两端代码之间有可能挂掉? 如何解决？
keep_alive(Name,Fun) ->
    register(Name, Pid=spawn(Fun)),
    on_exit(Pid, fun(_Why) -> keep_alive(Name,Fun) end).
