# 1. sqlite














一、

sqlite3长用于 轻量级的 数据存储，象单片机这一类，但是现在的sqlite3,已经很先进，不能小看

二、

**sqlite3常用命令**  
当前目录下建立或打开test.db数据库文件，并进入sqlite命令终端，以sqlite>前缀标识：  
#sqlite3 test.db  
   
查看数据库文件信息命令(注意命令前带字符'.')：  
sqlite>.database  
  
查看所有表的创建语句：  
sqlite>.schema  
   
查看指定表的创建语句：  
sqlite>.schema table_name  
   
以sql语句的形式列出表内容：  
sqlite>.dump table_name  
   
设置显示信息的分隔符：  
sqlite>.separator symble  
Example：设置显示信息以‘：’分隔  
sqlite>.separator :  
   
设置显示模式：  
sqlite>.mode mode_name  
Example:默认为list，设置为column，其他模式可通过.help查看mode相关内容  
sqlite>.mode column  
   
输出帮助信息：  
sqlite>.help  
   
设置每一列的显示宽度：  
sqlite>.width width_value  
Example:设置宽度为2  
sqlite>.width 2  
   
列出当前显示格式的配置：  
sqlite>.show  
   
退出sqlite终端命令：  
sqlite>.quit  
或  
sqlite>.exit  
   
**3、sqlite3指令**  
sql的指令格式：所有sql指令都是以分号(;)结尾，两个减号(--)则表示注释。  
如：  
sqlite>create studen\_table(Stu\_no interger PRIMARY KEY, Name text NOT NULL, Id interger UNIQUE, Age interger CHECK(Age>6), School text DEFAULT 'xx小学);  
该语句创建一个记录学生信息的数据表。  
   
**3.1 sqlite3存储数据的类型**  
NULL：标识一个NULL值  
INTERGER：整数类型  
REAL：浮点数  
TEXT：字符串  
BLOB：二进制数  
  
**3.2 sqlite3存储数据的约束条件**  
Sqlite常用约束条件如下：  
PRIMARY KEY - 主键：  
1）主键的值必须唯一，用于标识每一条记录，如学生的学号  
2）主键同时也是一个索引，通过主键查找记录速度较快  
3）主键如果是整数类型，该列的值可以自动增长  
NOT NULL - 非空：  
约束列记录不能为空，否则报错  
UNIQUE - 唯一：  
除主键外，约束其他列的数据的值唯一  
CHECK - 条件检查：  
约束该列的值必须符合条件才可存入  
DEFAULT - 默认值：  
列数据中的值基本都是一样的，这样的字段列可设为默认值  
  
**3.3 sqlite3常用指令**  
1）建立数据表  
create table table_name(field1 type1, field2 type1, ...);  
table_name是要创建数据表名称，fieldx是数据表内字段名称，typex则是字段类型。  
例，建立一个简单的学生信息表，它包含学号与姓名等学生信息：  
create table student\_info(stu\_no interger primary key, name text);

  
 create table if not exists 表名(字段名1,字段名2...);  

   
2）添加数据记录  
insert into table_name(field1, field2, ...) values(val1, val2, ...);  
valx为需要存入字段的值。  
例，往学生信息表添加数据：  
Insert into student\_info(stu\_no, name) values(0001, alex);  
   
3）修改数据记录  
update table_name set field1=val1, field2=val2 where expression;  
where是sql语句中用于条件判断的命令，expression为判断表达式  
例，修改学生信息表学号为0001的数据记录：  
update student\_info set stu\_no=0001, name=hence where stu_no=0001;  
   
4）删除数据记录  
delete from table_name \[where expression\];  
不加判断条件则清空表所有数据记录。  
例，删除学生信息表学号为0001的数据记录：  
delete from student\_info where stu\_no=0001;  
   
5）查询数据记录  
select指令基本格式：  
select columns from table_name \[where expression\];  
a查询输出所有数据记录  
select * from table_name;  
b限制输出数据记录数量  
select * from table_name limit val;  
c升序输出数据记录  
select * from table_name order by field asc;  
d降序输出数据记录  
select * from table_name order by field desc;  
e条件查询  
select * from table_name where expression;  
select * from table_name where field in ('val1', 'val2', 'val3');  
select * from table_name where field between val1 and val2;  
f查询记录数目  
select count (*) from table_name;  
g区分列数据  
select distinct field from table_name;  
有一些字段的值可能会重复出现，distinct去掉重复项，将列中各字段值单个列出。  
   
6）建立索引  
当说数据表存在大量记录，索引有助于加快查找数据表速度。  
create index index\_name on table\_name(field);  
例，针对学生表stu_no字段，建立一个索引：  
create index student\_index on student\_table(stu_no);  
建立完成后，sqlite3在对该字段查询时，会自动使用该索引。  
   
7）删除数据表或索引  
drop table table_name;  

drop index index_name;


















