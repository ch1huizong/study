-module(walks).
-export([plan_route/2]).

-spec plan_route(From::point(), To::point()) -> route().
-type direction() :: north | south | east | west .
-type point()     :: {integer(), integer()}.
-type route()     :: [{go, direction(), integer()}].

-spec file::open(Filename, Modes) -> {ok, Handle} | {error, Why} when
    Filename :: string(),
    Modes    :: [Mode],
    Mode     :: read | write | append,
    Handle   :: file_handle(),
    Why      :: error_term().

        
        

