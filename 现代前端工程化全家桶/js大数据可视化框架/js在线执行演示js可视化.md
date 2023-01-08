https://www.jsv9000.app/





# js在线可视化执行演示




## 先微后宏  事件循环


1、所有任务都在主线程上执行，形成一个执行栈。
2、主线程发现有异步任务，如果是微任务就把他放到微任务的消息队列里，如果是宏任务就把他放到宏任务的消息队列里。
3、执行栈所有同步任务执行完毕。
4、执行微任务队列，之后再执行宏任务队列。
5、轮询第4步。



```js
console.log('normal')

setTimeout(() => {
    console.log('setTimeout')
})

Promise.resolve(1).then((value) => {
    console.log('Promise')
})

queueMicrotask(() => {
    console.log('queueMicrotask')
})
```













