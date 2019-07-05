-module(test_mapreduce).
-compile(export_all).
-import(lists,[reverse/1, sort/1]).

test() ->
    wc_dir(".").

wc_dir(Dir) ->
    F1 = fun gen_words/2,
    F2 = fun count_words/3,
    Files = lib_find:files(Dir, "*.erl", false),
    L1 = phofs:mapreduce(F1, F2, [], Files),
    reverse(sort(L1)).


% F1
gen_words(Pid, File) ->
    F = fun(Word) -> Pid ! {Word, 1} end,
    lib_misc: foreachWordInFile(File, F).
% F2
count_words(Key, Vals, A) ->
    [{length(Vals), Key} | A ].
