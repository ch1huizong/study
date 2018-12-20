{application, gen_web_server,
    [
    {description, "gen_web_sever self behaviour"},
    {vsn, "0.0.1"},
    {modules, [gen_web_server,gws_server,gws_connection_sup]),
    {registered, [gws_connection_sup]},
    {applications, [kernel, stdlib]},
    ] 
}.
