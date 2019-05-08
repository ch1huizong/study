-module(mess_client).
-export([client/2]).
-include("mess_interface.hrl").

%%% The client process which runs on each server node
client(Server_Node, Name) ->
    {messenger, Server_Node} ! #logon{client_pid=self(), username=Name},
    await_result(),   %% 等待服务器结果
    client(Server_Node).

client(Server_Node) ->  %% command <--> client
    receive
        logoff -> exit(normal);
        #message_to{to_name=ToName, message=Message} ->
            {messenger, Server_Node} !  #message{client_pid=self(), to_name=ToName,message=Message},
            await_result();
        {message_from, FromName, Message} ->   %%直接接受的服务器响应server-->client
            io:format("Message from ~p: ~p~n", [FromName, Message])
    end,
    client(Server_Node).

%%% wait for a response from the server
%%% 等待服务器消息
await_result() ->  %%请求-响应 client <--> server
    receive
        #abort_client{message=Why} ->
            io:format("~p~n", [Why]),
            exit(normal);
        #server_reply{message=What} ->
            io:format("~p~n", [What])
    after 150000  ->    %% new4
            io:format("No  response from server~n",[]),
            exit(timeout)
    end.
