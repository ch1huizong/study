一、数据库、表结构操作
	
	1.创建：

		CREATE DATABASE my_db

		CREATE TABLE 表名称(
		列名称1 数据类型，
		列名称2 数据类型，
		列名称3 数据类型，
		...
		
		)
	
		创建索引：CREATE INDEX PersonIndex On Person (Lastname DESC, FirstName)

    ###########################################################################	

	例子：
		CREATE TABLE Persons(
		Id int NOT NULL AUTO_INCREMENT,     # 主键，自动增加值
		LastName varchar(255) NOT NULL,
		FirstName varchar(255) ,
		Address varchar(255),
		City varchar(255) DEFAULT 'Sandnes',   # default约束

		Id_O int,      # 外键字段，一个表中的外键字段是另一个表中的主键字段

		UNIQUE (Id) 或者 CONSTRAINT uc UNIQUE (Id, LastName)    # unique约束

		PRIMARY KEY (Id),       # 主键约束

		FOREIGN KEY (ID_O) REFERENCES Orders(ID_O),
		或者CONSTRAINT fk FOREIGN KEY (ID_O) REFERENCES Orders(ID_O)   # 外键约束

		CHECK (Id>0),

		)

    ###########################################################################	


	2.撤销：数据库、表、索引...

		DROP DATABASE 数据库名称
		DROP TABLE 表名称
		TRUNCATE TABLE 表名称


	3.变更：ALTER TABLE语句
		
		添加: ALTER TABLE 表名称 ADD 列名称 数据类型      #添加数据列
			 
					...ADD UNIQUE (ID)
					...ADD PRIMARY KEY (Id) 
					...ADD 外键
					...ADD CHECK (Id>0)
					...
					
			  约束命名: CONSTRAINT 约束名 约束(可以制定多列)
              
			  增加DEFAULT:  ALTER TABLE Persons ALTER City SET DEFAULT 'SANDES'


		删除：ALTER TABLE 表名称 DROP COLUMN 列名称   # 删除列

			  ALTER TABLE Persons DROP 约束   # 删除约束
					...DROP INDEX uc
					...DROP PRIMARY KEY
					...DROP FOREIGN KEY fk
					...DROP CHECK chk_Person
					...ALTER City DROP DEFAULT
			  

		改变列数据类型： ALTER TABLE 表名称 ALTER COLUMN 列名称 数据类型


二、查询和对行记录进行的操作
	
	查询记录：

	SELECT 列名称 FROM 表名称 WHERE  表达式1 AND/OR 表达式2    # 一般语法

	AS		#别名	
	LIMIT		# 限制
	OREDY BY 列 [DESC]   # 排序

	WHERE条件：

		LIKE | IN | BETWEEN ...AND ... | IS NULL或者IS NOT NULL |还有IFNULL(mysql) 
		结合通陪符号%,_

	
	SELECT 列 FROM table1 INNER(两边表都满足)|LEFT|RIGHT|FULL JOIN  table2  ON 表达式 ORDER BY 列名 #join语句
	
	SELECT 列 FROM 表1 UNION [ALL]	SELECT 列 FROM 表2  # union语句
	

    ###########################################################################	

	插入一条记录：
	INSERT INTO 表 VALUES (val1,val2...) 或者 INSERT INTO 表 (列1,列2...)  VALUES (val1,val2...)

	更新记录：
	UPDATE 表名称 SET 列名称=新值, ... WHERE 列名称 = 某值

	删除某行：
	DELETE FROM 表名称 WHERE 列名称=值   # 删除一行
	DELETE FROM 表名称    # 删除所有行



三、结果集筛选（函数）
	
	语法： select func(列)  from table;


	聚集函数: 输入值为整列，返回一个值

			  AVG,  COUNT(column),COUNT(*), COUNT(DISTINCT column), 

			  FIRST, LAST(mysql不支持),
			  MAX,MIN,SUM

			  GROUP(合计),HAVING(与where可以连用了,mysql作用不大)

	
	标量函数：输入为一个列中的值，转换后结果返回一系列值

			  UCASE, LCASE, MID(column,firstindex,len),LEN(在mysql中是LENGTH),
			  ROUND(column, decimal), NOW(), DATE_FORMAT(column_name, format)(mysql的形式)


四、关于myql部分
