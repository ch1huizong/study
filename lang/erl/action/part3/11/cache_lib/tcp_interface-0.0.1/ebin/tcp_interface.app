{application, tcp_interface,
    [
    {description, "tcp interface"},
    {vsn, "0.0.1"},
    {modules, [ti_app, ti_sup, ti_server]},
    {registered, [ti_sup]},
    {applications, [kernel, stdlib]},
    {mod, {ti_app, []}}
    ] 
}.
