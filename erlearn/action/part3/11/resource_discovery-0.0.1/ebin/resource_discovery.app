{application, resource_discovery, 
    [
    {description, "resource discovery system"},
    {vsn, "0.0.1"},
    {modules, [
                rd_app, 
                rd_sup,
                resource_discovery ]},
                
    {registered, [rd_sup]},
    {applications, [kernel, stdlib]},   
    {mod, {rd_app, []}}
    ] 
}.

