{application, http_interface,
    [
    {description, "A RESTful HTTP Interface"},

    {vsn, "0.0.1"},

    {modules, [hi_app, hi_server, hi_sup]},

    {registered, [hi_sup]},
    {applications, [kernel, stdlib]},
    {mod, {hi_app,[]}}
    ] 
}.
