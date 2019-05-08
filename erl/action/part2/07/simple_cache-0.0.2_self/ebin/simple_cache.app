{application, simple_cache,
    [
    {description, "A simple caching system"},
    {vsn, "0.0.2"},
    {modules, [sc_app, sc_sup]},
    {registered, [sc_sup]},
    {applications, [kernel, stdlib, sasl]},
    {mod, {sc_app, []}}
    ] 
}.
