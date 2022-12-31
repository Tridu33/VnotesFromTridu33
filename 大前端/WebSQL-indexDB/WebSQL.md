[TOC]

贫穷版WebSQL

1、创建数据库
```
var db = window.openDatabase("mydata", "1.0","数据库描述",20000);
//window.openDatabase("数据库名字", "版本","数据库描述",数据库大小);
if(db)
alert("新建数据库成功！");
```
2、怎样连接数据库
```
db.transaction(function(tx) {
tx.executeSql("CREATE TABLE test (id int UNIQUE, mytitle TEXT, timestamp REAL)");
});
```
上面是新建数据表！本地数据库是通过db.transaction()函数来实现的，再看下面的代码吧！
插入记录：
```
db.transaction(function(tx) {
tx.executeSql("INSERT INTO test (mytitle, timestamp) values(?, ?)", ["WEB Database", new Date().getTime()], null, null);
});
```
更新记录：
```
db.transaction(function(tx) {
tx.executeSql("update test set mytitle=? where mytitle = 'fsafdsaf'",['xp'],null,null);
});
```
查询记录：
```
db.transaction(function(tx) {
tx.executeSql("SELECT * FROM test", [],
    function(tx, result) {
        for(var i = 0; i < result.rows.length; i++){
        document.write('<b>' + result.rows.item(i)['mytitle'] + '</b><br />');
        }
       }, 
    function(){
    alert("error");
    });
});
```
删除表：
```
db.transaction(function(tx) {
tx.executeSql("DROP TABLE test");
})

```



富裕点的家庭：

```
function websqlCreateTable(tableName){
var creatTableSQL = 'CREATE TABLE IF  NOT EXISTS ' + tableName + ' (NAME text,AGE text,HEIGHT text,WEIGTH text)';
    dataBase.transaction(function(ctx, result) {
        ctx.executeSql(creatTableSQL, [], function(ctx, result) {
            alert("表创建成功 " + tableName);
        }, function(tx, error) {
            alert('创建表失败:' + tableName + error.message);
        });
    });
}
```

用```websqlCreateTable(table);```来调用


**富裕家庭，一次编写“泛型”代码生成，不限参数不限表格类型通用的函数？DSL,或者直接找别的编译出来js。**







在[HTML5本地存储——Web SQL Database](http://www.cnblogs.com/dolphinX/p/3405335.html)提到过Web SQL Database实际上已经被废弃，而HTML5的支持的本地存储实际上变成了indexDb



# 1. WebSQL
[菜鸟教程的教程https://www.runoob.com/html/html5-web-sql.html](https://www.runoob.com/html/html5-web-sql.html)

[HTML5前端数据库——Web SQL Databasehttps://www.jianshu.com/p/64ded82068b0](https://www.jianshu.com/p/64ded82068b0)



 [HTML5本地存储——Web SQL Database](https://www.cnblogs.com/dolphinX/p/3405335.html)

html5引入Web SQL Database概念，它使用 SQL 来操纵客户端数据库的 API，这些 API 是异步的，规范中使用的是SQLlite（SQL后端）。

以下是规范中定义的三个核心方法：

1.  **openDatabase**：这个方法使用现有的数据库或者新建的数据库创建一个数据库对象。
2.  **transaction**：这个方法让我们能够控制一个事务，以及基于这种情况执行提交或者回滚。
3.  **executeSql**：这个方法用于执行实际的 SQL 查询。



































































































































































































