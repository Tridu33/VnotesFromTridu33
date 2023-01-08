[TOC]



# 1. IndexDB
Migrating your WebSQL DB to IndexedDB
[https://www.html5rocks.com/en/tutorials/webdatabase/websql-indexeddb/](https://www.html5rocks.com/en/tutorials/webdatabase/websql-indexeddb/)
[https://github.com/greenido/WebSQL-to-IndexedDB-example](https://github.com/greenido/WebSQL-to-IndexedDB-example)

阮一峰
[http://www.ruanyifeng.com/blog/2018/07/indexeddb.html](http://www.ruanyifeng.com/blog/2018/07/indexeddb.html)
框架，代码snip是学不完的，要学元认知，越是基础代表越是能力高，api层层封装，

**编程核心能力是:会看官方api说明。**


这个实例好！
[HTML5 indexedDB前端本地存储数据库实例教程https://www.zhangxinxu.com/wordpress/2017/07/html5-indexeddb-js-example/](https://www.zhangxinxu.com/wordpress/2017/07/html5-indexeddb-js-example/)
可以看到直接把SQL语句弄到JS中了，主流的关系型数据库即视感，这么设计看上去似乎无可厚非，但恰恰这个设计成为了Web SQL Database被舍弃的重要原因之一：一是学习成本高了很多，SQL虽然本身并不复杂，但跨度较大，例如我司玩JS的工程师和玩SQL的工程师中间还隔了个玩php的工程师；二是本身使用很不方便，需要把JS对象转换成关系型的字符串语句，很啰嗦的。


而indexedDB直接JS对象入库，无缝对接。

这里出现了一个比较重要的概念，叫做objectStore，这是indexedDB可以替代Web SQL Database的重要优势所在，我称之为“存储对象”。

objectStore.add()可以向数据库添加数据，objectStore.delete()可以删除数据，objectStore.clear()可以清空数据库，objectStore.put()可以替换数据等还有很多很多操作API。

在这里，我们使用objectStore来创建数据库的主键和普通字段。


[网道api https://wangdoc.com/javascript/bom/indexeddb.html#indexeddb-%E5%AF%B9%E8%B1%A1](https://wangdoc.com/javascript/bom/indexeddb.html#indexeddb-%E5%AF%B9%E8%B1%A1)



IndexedDB 是一个比较复杂的 API，涉及不少概念。它把不同的实体，抽象成一个个对象接口。学习这个 API，就是学习它的各种对象接口。

数据库：IDBDatabase 对象

对象仓库：IDBObjectStore 对象,类似于关系型数据库的表格。

索引： IDBIndex 对象

事务： IDBTransaction 对象

操作请求：IDBRequest 对象

指针： IDBCursor 对象

主键集合：IDBKeyRange 对象








 [前端数据库——WebSQL和IndexedDB](https://www.cnblogs.com/ljwsyt/p/9760266.html)


WebSQL半途而废开发，用idexDB

![](_v_images/1582442552_29525.png)


对于只存储某些字段的需求来说，可以使用Local Storage和 Session Storage来完成。但是一旦存储大量的数据，Local Storage和 Session Storage就远远不能满足需求了。这时，IndexedDB的强大之处就会体现出来了。

## 1.1. HTML5 indexedDB前端本地存储数据库实例教程



[IndexedDB使用与出坑指南 https://segmentfault.com/a/1190000006924681](https://segmentfault.com/a/1190000006924681)


[IndexedDB 教程https://www.jianshu.com/p/ca838ff7e4d8](https://www.jianshu.com/p/ca838ff7e4d8)



[HTML5本地存储——IndexedDBhttps://zhuanlan.zhihu.com/p/27419332](https://zhuanlan.zhihu.com/p/27419332)


HTML5本地存储——IndexedDB（一：基本使用）](https://www.cnblogs.com/dolphinX/p/3415761.html)

```
function openDB (name) {
            var request=window.indexedDB.open(name);
            request.onerror=function(e){
                console.log('OPen Error!');
            };
            request.onsuccess=function(e){
                myDB.db=e.target.result;
            };
        }

        var myDB={
            name:'test',
            version:1,
            db:null
        };
        openDB(myDB.name);
```

```

```


```

```



```

```


```

```


```

```


```

```








## 1.2. API


[IndexedDB API   https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API)

IDBObjectStore
[https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API)




IDBCursor

https://developer.mozilla.org/en-US/docs/Web/API/IDBCursor



IDBKeyRange

https://developer.mozilla.org/en-US/docs/Web/API/IDBKeyRange















[https://www.ibm.com/developerworks/cn/web/wa-indexeddb/](https://www.ibm.com/developerworks/cn/web/wa-indexeddb/)
 使用 HTML5 IndexedDB API

本地数据持久性提高了 Web 应用程序可访问性和移动应用程序响应能力

[https://developer.mozilla.org/en-US/docs/IndexedDB](https://developer.mozilla.org/en-US/docs/IndexedDB)

[https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API)

[https://www.w3.org/TR/IndexedDB/](https://www.w3.org/TR/IndexedDB/)




https://developer.mozilla.org/zh-CN/docs/Web/API/IndexedDB_API


[
indexedDB中没有表的概念，而是objectStore，一个数据库中可以包含多个objectStore，objectStore是一个灵活的数据结构，可以存放多种类型数据。也就是说一个objectStore相当于一张表，里面存储的每条数据和一个键相关联。

我们可以使用每条记录中的某个指定字段作为键值（keyPath），也可以使用自动生成的递增数字作为键值（keyGenerator），也可以不指定。选择键的类型不同，objectStore可以存储的数据结构也有差异。　

这个就有点复杂了。看这里的教程：  
*1.http://www.cnblogs.com/dolphinX/p/3415761.html*　

2.http://www.cnblogs.com/dolphinX/p/3416889.html

详细API地址：http://www.ibm.com/developerworks/cn/web/wa-indexeddb/#ibm-pcon












