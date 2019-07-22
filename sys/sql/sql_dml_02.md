# SQL数据操作语言

一、数据行
	
1. CURD

    - INSERT INTO 表名 (字段名1,...) VALUES (字段值1,...); 

	- `INSERT INTO table1 SELECT * FROM t2`  # t2导出到另一个表t1

    - `CREATE TABLE t1 AS SELECT * FROM t2` # 复制t2表到t1

 	- UPDATE 表名 SET  字段名1 = 字段值1,... (WHERE)...

	- DELETE FROM 表名 ...(WHERE)...

---

二. 查询

1. 单表:

    SELECT (DISTINCT) * FROM 表名 WHERE...GROUP BY...HAVING...ORDER BY...

    - 聚合函数: AVG, SUM, MIN,MAX, COUNT

    - WHERE高级过滤: 
	    - 通配符过滤, LIKE和%, _
		- 空值检测, IS NULL/IS NOT NULL
		- NOT / IN / BETWEEN * AND * /
	
    - 数据分组: 
	    - GROUP BY      以在组内进行聚合操作
		- HAVING        可以包含聚合函数，列必须是分组列

	- LIMIT index,offset

	- 其他
	    + DISTINCT 对整个结果集去重
		+ UNION					
            1. 列数目相同
            2. 列类型相同或能转换,通常结果集不必有关联					
		+ UNION ALL	 不去重复

2. 多表:(连接条件)
	
    - 交叉连接:
	    FROM t1 别名, t2 别名   隐式
	    CROSS JOIN              显示	
		没有ON条件;

	- 内连接:	
		(INNER) JOIN table_name ON condition
	    - 使用表别名,减少歧义;
		- 可以进行多表多JOIN连接;
		- 不等值条件, 进行了cross计算，相当与for...for循环;

    - 自连接:							
	    同一个表中查找相互匹配的数据行, 看成两个不同的表就得了, 取别名o1, o2;
		问题,自己链接自己,重复; A->B == A<-B,重复;

	- 外连接:
		RIGHT/LEFT/FULL  JOIN			

		解决两个表中不匹配记录的处理(空值匹配问题),与内部join最大区别对空值的处理不同;
		全JOIN是left/right的合集;


3. 子查询
	
    - 单值子查询: 一行一列, 单值,场合是SELECT列表/相关子查询/Where表达式
	- 表子查询: 多行多列,当作临时表,外部会引用临时表中定义列名
	
	- 场景:
	    1. SELECT中的单值子查询
		    SELECT f1, f2, (SELECT MAX(Year) FROM t2 WHERE t2.f1 = t1.f1 ) FROM t1;

			单值子查询引入外部主查询字段;

		2. 单值子查询用于Where子句;

		    内层会引用外部定义的表;
