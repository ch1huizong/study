# SQL数据定义语言

一、数据表
    1. 类型： 整数、数值、字符串、日期、二进制

	2. 操作: 

        CREATE/ALTER/DROP TABLE * 

	    CREATE INDEX 索引名 ON 表名(字段1,字段2,...)

	    DROP INDEX 索引名 ON 表名

	    ALTER语句, ALTER TABLE 表名... ADD/DROP/ALTER 
	3. 约束:
		
	    - 约束种类： NOT NULL、DEFAULT、UNIQUE、CHECK、主键（联合主键）、外键,AUTO_INCREMENT

	    - 约束定义： (CONSTRAINT 约束名) 约束类型(UNIQUE) (字段1,字段2,...)

	    - 三种添加约束的方式：
            1. 字段直接添加 
            2. 末尾添加,重命名约束名
            3. Alter表中添加

    4. 操作已有表的约束：

	    ALTER TABLE	表名 ADD CONSTRAINT 约束名 约束类型(UNIQUE)(字段1,字段2,...)

	    ALTER TABLE 表名 DROP CONSTRAINT 约束名
		

---


二. 注意点
	1. 创建外键约束的目的是在表间建立依赖关系,预防破坏表之间连接,防止非法数据插入外键列
    2. SQL语言没有循环，类似与高阶map操作, SQL内含了for循环; 
    3. SQL对大小写不敏感。
