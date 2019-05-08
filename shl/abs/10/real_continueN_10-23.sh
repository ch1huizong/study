  1 # Albert Reiner 给出了一个关于使用"continue N"的例子:
  2 # ---------------------------------------------------------
  3 
  4 #  假定我有很多作业需要运行, 这些任务要处理一些数据,
  5 #+ 这些数据保存在某个目录下的文件里, 文件是以预先给定的模式进行命名的. 
  6 #+ 有几台机器要访问这个目录, 
  7 #+ 我想把工作都分配给这几台不同的机器,
  8 #+ 然后我一般会在每台机器里运行类似下面的代码:
  9 
 10 while true
 11 do
 12   for n in .iso.*
 13   do
 14     [ "$n" = ".iso.opts" ] && continue
 15     beta=${n#.iso.}
 16     [ -r .Iso.$beta ] && continue
 17     [ -r .lock.$beta ] && sleep 10 && continue
 18     lockfile -r0 .lock.$beta || continue
 19     echo -n "$beta: " `date`
 20     run-isotherm $beta
 21     date
 22     ls -alF .Iso.$beta
 23     [ -r .Iso.$beta ] && rm -f .lock.$beta
 24     continue 2
 25   done
 26   break
 27 done
 28 
 29 #  在我的应用中的某些细节是很特殊的, 尤其是sleep N, 
 30 #+ 但是更一般的模式是:
 31 
 32 while true
 33 do
 34   for job in {pattern}
 35   do
 36     {job already done or running} && continue
 37     {mark job as running, do job, mark job as done}
 38     continue 2
 39   done
 40   break        # 而所谓的`sleep 600'只不过是想避免程序太快结束, 而达不到演示效果. 
 41 done
 42 
 43 #  脚本只有在所有任务都完成之后才会停止运行,
 44 #+ (包括那些运行时新添加的任务). 
 45 #+ 通过使用合适的lockfiles,
 46 #+ 可以使几台机器协作运行而不会产生重复的处理,
 47 #+ [在我的这个例子中, 重复处理会使处理时间延长一倍时间, 因此我很想避免这个问题].
 48 #+ 同样, 如果每次都从头开始搜索, 可以由文件名得到处理顺序.
 49 #+ 当然, 还有一种办法, 也可以不使用`continue 2',
 50 #+ 但这样的话, 就不得不检查相同的任务是不是已经被完成过了,
 51 #+ (而我们应该马上来找到下一个要运行的任务)
 52 #+ (在演示的情况中, 检查新任务前我们终止或睡眠了很长一段时间).
 53 #+ 
