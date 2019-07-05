%% -*- mode:Erlang;

{application, tcp_rpc,
    [{description, "RPC server for Erlang"},
    {vsn, "0.0.1"},
    {modules, [tr_app, tr_sup, tr_server]},
    {registered, [tr_sup]},
    {applications, [kernel, stdlib]},
    {mod, {tr_app, []}}
    ]}.
