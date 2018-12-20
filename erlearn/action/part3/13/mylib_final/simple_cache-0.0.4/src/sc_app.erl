-module(sc_app).
-behaviour(application).

-export([start/2, stop/1]).

-define(WAIT_FOR_RESOURCES, 2500).

start(_StartType, _StartArgs) ->
    ok = ensure_contact(),
    resource_discovery:add_local_resource(simple_cache, node()),    % 资源发现服务初始化
    resource_discovery:add_target_resource_type(simple_cache),
    resource_discovery:trade_resources(),
    timer:sleep(?WAIT_FOR_RESOURCES), 
    sc_store:init(),                                                % 数据库初始化
    case sc_sup:start_link() of
        {ok, Pid} ->
            sc_event_logger:add_handler(),                          % 增加事件处理回调模块
            {ok, Pid};
        Other ->
            {error, Other}
    end.

stop(_State) ->
    ok.

ensure_contact() ->
    DefaultNodes = ['slave1@s1', 'slave2@s2'], 
    case get_env(simple_cache, contact_nodes, DefaultNodes) of      % 查询本地的配置项目contact_nodes
        [] ->
            {error, no_contact_nodes};
        ContactNodes ->
            ensure_contact(ContactNodes)
    end.

ensure_contact(ContactNodes) ->   % 连接
    Answering = [ N || N <- ContactNodes, net_adm:ping(N) =:= pong ],
    case Answering of
        [] ->
            {error, no_contact_nodes_reachable};
        _ ->
            DefaultTime = 6000,
            WaitTime = get_env(simple_cache, wait_time, DefaultTime),% 查询超时配置
            wait_for_nodes(length(Answering), WaitTime) 
    end.

% 等待达到全联通状态
wait_for_nodes(MinNodes, WaitTime) ->
    Slices = 10, % 循环数
    SliceTime = round(WaitTime/Slices),  
    wait_for_nodes(MinNodes, SliceTime, Slices).

wait_for_nodes(_MinNodes, _SliceTime, 0) ->
    ok;
wait_for_nodes(MinNodes, SliceTime, Iterations) -> % 检查是否已经连接上足够多的节点
    case length(nodes()) > MinNodes of
        true ->
            ok;
        false ->
            timer:sleep(SliceTime),
            wait_for_nodes(MinNodes, SliceTime, Iterations -1)
    end.

get_env(AppName, Key, Default) ->
    case application:get_env(AppName, Key) of
        undefined -> Default;
        {ok, Value} -> Value
    end.
