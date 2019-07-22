
一、数据行
	
	1. CURD

	INSERT INTO 表名 (字段名1,...)	VALUES (字段值1,...); 

	INSERT ... SELECT...			导出到另一个表

	SELECT INTO 字段1,字段2,...  INTO 新表 FROM 旧表

	UPDATE 表名 SET  字段名1 = 字段值1,... (WHERE)...

	DELETE FROM 表名 ...(WHERE)...



二. 查询

	1.单表:

	SELECT (DISTINCT) * FROM 表名 WHERE...GROUP BY...HAVING...ORDER BY...

		a.聚合函数: AVG, SUM, MIN,MAX, COUNT

		b.WHERE高级过滤: 
			a.通配符过滤:			LIKE: %, _
			b.空值检测：			IS NULL/IS NOT NULL
			c.NOT / IN / BETWEEN * AND * /
		
		c.数据分组: 
			GROUP BY				以在组内进行聚合操作
			HAVING					可以包含聚合函数，列必须是分组列

		d.LIMIT index,offset

		e. 其他
			DISTINCT				对整个结果集去重

			UNION					1.列数目相同，2.列类型相同或能转换,通常结果集不必有关联					
			UNION ALL				不去重复



	2.多表:(连接条件)
	
	交叉连接:
		FROM t1 别名, t2 别名			隐式
		CROSS JOIN						显示	
		
		没有ON条件;
	

	内连接:	
		(INNER) JOIN table_name ON condition (JOIN...)
	
		使用表别名,减少歧义;
		可以进行多表多JOIN连接;
		不等值条件, 进行了cross计算，相当与for...for循环;


	自连接:							
		表中查找相互匹配的数据行, 看成两个不同的表就得了, 取别名o1, o2;
		问题,自己链接自己,重复; A->B == A<-B,重复;

	外连接:
		RIGHT/LEFT/FULL  JOIN			

		解决两个表中不匹配记录的处理(空值匹配问题),与内部join最大区别对空值的处理不同;
		全JOIN是left/right的合集;
		mysql不支持full, 可以用union模拟;



	3.子查询(递归):
	
	单值子查询						一行一列, 单值,场合是SELECT列表/相关子查询/Where表达式


	表子查询						多行多列,当作临时表,外部会引用临时表中定义列名
	
	场景:
		1.SELECT中的单值子查询;

			SELECT f1, f2, (SELECT MAX(Year) FROM t2 WHERE t2.f1 = t1.f1 ) FROM t1;

			单值子查询引入外部主查询字段;


		2.单值子查询用于Where子句;

			内层会引用外部定义的表;



	集合操作(多行单列):动态集合

		IN  
		ANY/ALL不能单独使用,与比较运算符结合,ALL子查询结果若null,那么条件返回true

		WHERE EXISTS (相关子查询) for...if 像是根据条件测试返回记录



	UPDATE/DELETE WHERE (相关子查询)有问题?
