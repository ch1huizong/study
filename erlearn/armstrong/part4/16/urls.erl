-module(urls).
-export([urls2htmlFile/2, bin2urls/1]).
-import(lists,[reverse/1,reverse/2,map/2]).

%% 把一个url列表写入文件,write_file写入IO列表

urls2htmlFile(Urls, File) ->
    file:write_file(File, urls2html(Urls)).

%% 得到Bin里的urls
bin2urls(Bin) -> gather_urls(binary_to_list(Bin),[]).

%% 一些装饰
urls2html(Urls) -> [ h1("Urls"), make_list(Urls) ].

% 头
h1(Title) -> ["<h1>", Title, "</h1>\n"].

% li..li
make_list(L) ->
    ["<ul>\n", map(fun(I) -> ["<li>", I ,"</li>"] end,L) , "</ul>\n" ].

%% very nice
gather_urls("<a href" ++ T,L) ->
    {Url, T1} = collect_url_body(T, reverse("<a href")),  %%note,L
    gather_urls(T1,[Url|L]);

gather_urls([_|T], L) ->
    gather_urls(T,L);

gather_urls([], L) ->
    L.

collect_url_body("</a>" ++ T, L) -> { reverse(L,"</a>"), T }; %%note
collect_url_body([H|T], L) -> collect_url_body(T, [H|L]);
collect_url_body([],_) -> {[],[]}.


