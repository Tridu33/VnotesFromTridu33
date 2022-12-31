# 1. shiyanlou


```
SELECT[DISTINCT]
FROM
WHERE
GROUP BY
HAVING
UNION
ORDER BY

```



第1步，先运行蓝框里的内容

第2步，运行select子句得到查询结果

最后一步，运行orderby对查询结果排序

最后，你会发现规律其实很简单，sql查询语句的运行顺序：

select子句，orderby分别最后运行，

其他子句按书写顺序运行

1.  FROM 才是 SQL 语句执行的第一步，并非 SELECT 。数据库在执行 SQL 语句的第一步是将数据从硬盘加载到数据缓冲区中，以便对这些数据进行操作。
2.  SELECT 是在大部分语句执行了之后才执行的，严格的说是在 FROM 和 GROUP BY 之后执行的。理解这一点是非常重要的，这就是你不能在 WHERE 中使用在 SELECT 中设定别名的字段作为判断条件的原因。
















```sql
CREATE DATABASE mysql_shiyan;

use mysql_shiyan;

CREATE TABLE department
(
  dpt_name   CHAR(20) NOT NULL,
  people_num INT(10) DEFAULT '10',
  CONSTRAINT dpt_pk PRIMARY KEY (dpt_name)
 );

CREATE TABLE employee
(
  id      INT(10) PRIMARY KEY,
  name    CHAR(20),
  age     INT(10),
  salary  INT(10) NOT NULL,
  phone   INT(12) NOT NULL,
  in_dpt  CHAR(20) NOT NULL,
  UNIQUE  (phone),
  CONSTRAINT emp_fk FOREIGN KEY (in_dpt) REFERENCES department(dpt_name)
 );
 
CREATE TABLE project
(
  proj_num   INT(10) NOT NULL,
  proj_name  CHAR(20) NOT NULL,
  start_date DATE NOT NULL,
  end_date   DATE DEFAULT '2015-04-01',
  of_dpt     CHAR(20) REFERENCES department(dpt_name),
  CONSTRAINT proj_pk PRIMARY KEY (proj_num,proj_name)
 );

```


```sql

CREATE DATABASE mysql_shiyan;

use mysql_shiyan;

CREATE TABLE department
(
  dpt_name   CHAR(20) NOT NULL,
  people_num INT(10) DEFAULT '10',
  CONSTRAINT dpt_pk PRIMARY KEY (dpt_name)
 );

CREATE TABLE employee
(
  id      INT(10) PRIMARY KEY,
  name    CHAR(20),
  age     INT(10),
  salary  INT(10) NOT NULL,
  phone   INT(12) NOT NULL,
  in_dpt  CHAR(20) NOT NULL,
  UNIQUE  (phone),
  CONSTRAINT emp_fk FOREIGN KEY (in_dpt) REFERENCES department(dpt_name)
 );
 
CREATE TABLE project
(
  proj_num   INT(10) NOT NULL,
  proj_name  CHAR(20) NOT NULL,
  start_date DATE NOT NULL,
  end_date   DATE DEFAULT '2015-04-01',
  of_dpt     CHAR(20) REFERENCES department(dpt_name),
  CONSTRAINT proj_pk PRIMARY KEY (proj_num,proj_name)
 );

CREATE TABLE table_1
(
l_1 INT(10) PRIMARY KEY,
l_2 INT(10),
l_3 INT(10)
 );



#INSERT INTO department(dpt_name,people_num) VALUES('部门',人数);

INSERT INTO department(dpt_name,people_num) VALUES('dpt1',11);
INSERT INTO department(dpt_name,people_num) VALUES('dpt2',12);
INSERT INTO department(dpt_name,people_num) VALUES('dpt3',10);
INSERT INTO department(dpt_name,people_num) VALUES('dpt4',15);


#INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(编号,'名字',年龄,工资,电话,'部门');

INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(01,'Tom',26,2500,119119,'dpt4');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(02,'Jack',24,2500,120120,'dpt2');
INSERT INTO employee(id,name,salary,phone,in_dpt) VALUES(03,'Jobs',3600,019283,'dpt2');
INSERT INTO employee(id,name,salary,phone,in_dpt) VALUES(04,'Tony',3400,102938,'dpt3');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(05,'Rose',22,2800,114114,'dpt3');



#INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(编号,'工程名','开始时间','结束时间','部门名');

INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(01,'proj_a','2015-01-15','2015-01-31','dpt2');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(02,'proj_b','2015-01-15','2015-02-15','dpt1');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(03,'proj_c','2015-02-01','2015-03-01','dpt4');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(04,'proj_d','2015-02-15','2015-04-01','dpt3');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(05,'proj_e','2015-02-25','2015-03-01','dpt4');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(06,'proj_f','2015-02-26','2015-03-01','dpt2');





 
```


```sql
CREATE DATABASE test_01;

CREATE DATABASE mysql_shiyan;

use mysql_shiyan;

CREATE TABLE department
(
  dpt_name   CHAR(20) NOT NULL,
  people_num INT(10) DEFAULT '10',
  CONSTRAINT dpt_pk PRIMARY KEY (dpt_name)
 );

CREATE TABLE employee
(
  id      INT(10) PRIMARY KEY,
  name    CHAR(20),
  age     INT(10),
  salary  INT(10) NOT NULL,
  phone   INT(12) NOT NULL,
  in_dpt  CHAR(20) NOT NULL,
  UNIQUE  (phone),
  CONSTRAINT emp_fk FOREIGN KEY (in_dpt) REFERENCES department(dpt_name)
 );
 
CREATE TABLE project
(
  proj_num   INT(10) NOT NULL,
  proj_name  CHAR(20) NOT NULL,
  start_date DATE NOT NULL,
  end_date   DATE DEFAULT '2015-04-01',
  of_dpt     CHAR(20) REFERENCES department(dpt_name),
  CONSTRAINT proj_pk PRIMARY KEY (proj_num,proj_name)
 );

CREATE TABLE table_1
(
l_1 INT(10) PRIMARY KEY,
l_2 INT(10),
l_3 INT(10)
 );



#INSERT INTO department(dpt_name,people_num) VALUES('部门',人数);

INSERT INTO department(dpt_name,people_num) VALUES('dpt1',11);
INSERT INTO department(dpt_name,people_num) VALUES('dpt2',12);
INSERT INTO department(dpt_name,people_num) VALUES('dpt3',10);
INSERT INTO department(dpt_name,people_num) VALUES('dpt4',15);


#INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(编号,'名字',年龄,工资,电话,'部门');

INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(01,'Tom',26,2500,119119,'dpt4');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(02,'Jack',24,2500,120120,'dpt2');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(03,'Rose',22,2800,114114,'dpt3');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(04,'Jim',35,3000,100861,'dpt1');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(05,'Mary',21,3000,100101,'dpt2');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(06,'Alex',26,3000,123456,'dpt1');





#INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(编号,'工程名','开始时间','结束时间','部门名');

INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(01,'proj_a','2015-01-15','2015-01-31','dpt2');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(02,'proj_b','2015-01-15','2015-02-15','dpt1');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(03,'proj_c','2015-02-01','2015-03-01','dpt4');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(04,'proj_d','2015-02-15','2015-04-01','dpt3');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(05,'proj_e','2015-02-25','2015-03-01','dpt4');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(06,'proj_f','2015-02-26','2015-03-01','dpt2');


#INSERT INTO table_1 VALUES(01,11,12);

INSERT INTO table_1 VALUES(02,22,89);
INSERT INTO table_1 VALUES(03,56,33);
INSERT INTO table_1 VALUES(04,34,37);
INSERT INTO table_1 VALUES(05,39,32);
INSERT INTO table_1 VALUES(06,90,33);





 

```




```sql


#INSERT INTO department(dpt_name,people_num) VALUES('部门',人数);

INSERT INTO department(dpt_name,people_num) VALUES('dpt1',11);
INSERT INTO department(dpt_name,people_num) VALUES('dpt2',12);
INSERT INTO department(dpt_name,people_num) VALUES('dpt3',10);
INSERT INTO department(dpt_name,people_num) VALUES('dpt4',15);


#INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(编号,'名字',年龄,工资,电话,'部门');

INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(01,'Tom',26,2500,119119,'dpt4');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(02,'Jack',24,2500,120120,'dpt2');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(03,'Rose',22,2800,114114,'dpt3');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(04,'Jim',35,3000,100861,'dpt1');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(05,'Mary',21,3000,100101,'dpt2');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(06,'Alex',26,3000,123456,'dpt1');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(07,'Ken',27,3500,654321,'dpt1');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(08,'Rick',24,3500,987654,'dpt3');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(09,'Joe',31,3600,110129,'dpt2');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(10,'Mike',23,3400,110110,'dpt4');
INSERT INTO employee(id,name,salary,phone,in_dpt) VALUES(11,'Jobs',3600,019283,'dpt2');
INSERT INTO employee(id,name,salary,phone,in_dpt) VALUES(12,'Tony',3400,102938,'dpt3');






#INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(编号,'工程名','开始时间','结束时间','部门名');

INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(01,'proj_a','2015-01-15','2015-01-31','dpt2');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(02,'proj_b','2015-01-15','2015-02-15','dpt1');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(03,'proj_c','2015-02-01','2015-03-01','dpt4');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(04,'proj_d','2015-02-15','2015-04-01','dpt3');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(05,'proj_e','2015-02-25','2015-03-01','dpt4');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(06,'proj_f','2015-02-26','2015-03-01','dpt2');










```



```txt
6	Alex	26	3000	123456	dpt1
7	Ken	27	3500	654321	dpt1
8	Rick	24	3500	987654	dpt3
9	Joe	31	3600	100129	dpt2
10	Mike	23	3400	110110	dpt1
11	Jim	35	3000	100861	dpt4
12	Mary	21	3000	100101	dpt2

```



```sql
CREATE DATABASE mysql_shiyan;

use mysql_shiyan;

CREATE TABLE department
(
  dpt_name   CHAR(20) NOT NULL,
  people_num INT(10) DEFAULT '10',
  CONSTRAINT dpt_pk PRIMARY KEY (dpt_name)
 );

CREATE TABLE employee
(
  id      INT(10) PRIMARY KEY,
  name    CHAR(20),
  age     INT(10),
  salary  INT(10) NOT NULL,
  phone   INT(12) NOT NULL,
  in_dpt  CHAR(20) NOT NULL,
  UNIQUE  (phone),
  CONSTRAINT emp_fk FOREIGN KEY (in_dpt) REFERENCES department(dpt_name)
 );
 
CREATE TABLE project
(
  proj_num   INT(10) NOT NULL,
  proj_name  CHAR(20) NOT NULL,
  start_date DATE NOT NULL,
  end_date   DATE DEFAULT '2015-04-01',
  of_dpt     CHAR(20) REFERENCES department(dpt_name),
  CONSTRAINT proj_pk PRIMARY KEY (proj_num,proj_name)
 );

```



```sql

```



```sql

```



```sql

```



```sql

```


```sql

```


```sql

```


```sql

```


```sql

```












```sql

```


```sql

```


```sql

```


```sql

```


```sql
CREATE DATABASE gradesystem;
use gradesystem;
CREATE TABLE student(
sid int NOT NULL AUTO_INCREMENT,
sname varchar(20) NOT NULL,
gender varchar(10) NOT NULL,
PRIMARY KEY(sid)
 );
CREATE TABLE course(
cid int NOT NULL AUTO_INCREMENT,
cname varchar(20) NOT NULL,
PRIMARY KEY(cid)
);
CREATE TABLE mark(
mid int NOT NULL AUTO_INCREMENT,
sid int NOT NULL,
cid int NOT NULL,
score int NOT NULL,
PRIMARY KEY(mid),
FOREIGN KEY(sid) REFERENCES student(sid),
FOREIGN KEY(cid) REFERENCES course(cid)
);
INSERT INTO student VALUES(1,'Tom','male'),(2,'Jack','male'),(3,'Rose','female');
INSERT INTO course VALUES(1,'math'),(2,'physics'),(3,'chemistry');
INSERT INTO mark VALUES(1,1,1,80),(2,2,1,85),(3,3,1,90),(4,1,2,60),(5,2,2,90),(6,3,2,75),(7,1,3,95),(8,2,3,75),(9,3,3,85);

```



















bak.sql

```sql

-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: mysql_shiyan
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `dpt_name` char(20) NOT NULL,
  `people_num` int(10) DEFAULT '10',
  PRIMARY KEY (`dpt_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES ('dpt1',11),('dpt2',12),('dpt3',10),('dpt4',15);
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `id` int(10) NOT NULL,
  `name` char(20) DEFAULT NULL,
  `age` int(10) DEFAULT NULL,
  `salary` int(10) NOT NULL,
  `phone` int(12) NOT NULL,
  `in_dpt` char(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone` (`phone`),
  KEY `emp_fk` (`in_dpt`),
  KEY `inx_id` (`id`),
  KEY `idx_name` (`name`),
  KEY `idx_id` (`id`),
  CONSTRAINT `emp_fk` FOREIGN KEY (`in_dpt`) REFERENCES `department` (`dpt_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'Tom',26,2500,119119,'dpt4'),(2,'Jack',24,2500,120120,'dpt2'),(3,'Jobs',NULL,3600,19283,'dpt2'),(4,'Tony',NULL,3400,102938,'dpt3'),(5,'Rose',22,2800,114114,'dpt3'),(6,'Alex',26,3000,123456,'dpt1'),(7,'Ken',27,3500,654321,'dpt1'),(8,'Rick',24,3500,987654,'dpt3'),(9,'Joe',31,3600,100129,'dpt2'),(10,'Mike',23,3400,110110,'dpt1'),(11,'Jim',35,3000,100861,'dpt4'),(12,'Mary',21,3000,100101,'dpt2');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project` (
  `proj_num` int(10) NOT NULL,
  `proj_name` char(20) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT '2015-04-01',
  `of_dpt` char(20) DEFAULT NULL,
  PRIMARY KEY (`proj_num`,`proj_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES (1,'proj_a','2015-01-15','2015-01-31','dpt2'),(2,'proj_b','2015-01-15','2015-02-15','dpt1'),(3,'proj_c','2015-02-01','2015-03-01','dpt4'),(4,'proj_d','2015-02-15','2015-04-01','dpt3'),(5,'proj_e','2015-02-25','2015-03-01','dpt4'),(6,'proj_f','2015-02-26','2015-03-01','dpt2');
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `table_1`
--

DROP TABLE IF EXISTS `table_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `table_1` (
  `l_1` int(10) NOT NULL,
  `l_2` int(10) DEFAULT NULL,
  `l_3` int(10) DEFAULT NULL,
  PRIMARY KEY (`l_1`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_1`
--

LOCK TABLES `table_1` WRITE;
/*!40000 ALTER TABLE `table_1` DISABLE KEYS */;
/*!40000 ALTER TABLE `table_1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `v_emp`
--

DROP TABLE IF EXISTS `v_emp`;
/*!50001 DROP VIEW IF EXISTS `v_emp`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `v_emp` AS SELECT 
 1 AS `v_name`,
 1 AS `v_age`,
 1 AS `v_phone`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `v_emp`
--

/*!50001 DROP VIEW IF EXISTS `v_emp`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_emp` AS select `employee`.`name` AS `v_name`,`employee`.`age` AS `v_age`,`employee`.`phone` AS `v_phone` from `employee` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-04 18:24:49


```

















































