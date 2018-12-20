%%% client-to-server1
-record(logon, {client_pid, username}).
-record(message, {client_pid, to_name, message}).

%%  server-to-client,await_result
-record(abort_client, {message}).
-record(server_reply, {message}).
%%  server-to-client,client1
-record(message_from, {from_name, message}).

%%% shell-to-client
-record(message_to, {to_name, message}).

