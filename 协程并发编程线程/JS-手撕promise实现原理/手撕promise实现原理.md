







# 手撕promise实现原理
Continuation 在 JS 中的应用 - 尚春的文章 - 知乎
https://zhuanlan.zhihu.com/p/94611888
Yassine Elouafi 在系列文章 Algebraic Effects in JavaScript 中系统性地介绍了 Continuation、CPS、使用 Generator 改造 CPS 并实现 callCC、进一步支持 Delimited Continuation 以及最终支持 Algebraic Effects 等内容，行文顺畅，内容示例夯实，是研究 JS Continuation 上乘的参考资料。


关键词:monad,call/cc,yield,async,await,

立即求值语义的JS打开一个惰性求值的口子，异步自动调用承诺的任务链


https://juejin.cn/post/7112639843871490061/ 完全符合Promise/A+规范的Promise源码实现

图解 Promise 实现原理（一）—— 基础实现 - 无名之辈的文章 - 知乎
https://zhuanlan.zhihu.com/p/58428287

https://juejin.cn/post/7051364317119119396 手写Promise和链式调用


```js

class myPromise {
  static PENDING = "pending";
  static FULFILLED = "fulfilled";
  static REJECTED = "rejected";
  constructor(func) {
    this.promiseState = myPromise.PENDING; 
    this.promiseResult = null; 
    this.fulfilledFuncCallback = []; 
    this.rejectedFuncCallback = []; 
    try {
      func(this.resolve.bind(this), this.reject.bind(this));
    } catch (err) {
      this.reject(err);
    }
  }
  resolve(value) {
    if (this.promiseState == myPromise.PENDING) {
      this.promiseState = myPromise.FULFILLED;
      this.promiseResult = value;
      this.fulfilledFuncCallback.forEach((item) => {
        item();
      });
    }
  }
  reject(reason) {
    if (this.promiseState == myPromise.PENDING) {
      this.promiseState = myPromise.REJECTED;
      this.promiseResult = reason;
      this.rejectedFuncCallback.forEach((item) => {
        item();
      });
    }
  }
  then(fulfilledFunc, rejectedFunc) {
    let newPromise = new myPromise((resolve, reject) => {
      if (this.promiseState == myPromise.PENDING) {
        this.fulfilledFuncCallback.push(() => {
          setTimeout(() => {
            try {
              if (typeof fulfilledFunc !== "function") {
                resolve(this.promiseResult);
              } else {
                let x = fulfilledFunc(this.promiseResult);
                resolvePromise(newPromise, x, resolve, reject);
              }
            } catch (error) {
              reject(error);
            }
          });
        });
        this.rejectedFuncCallback.push(() => {
          setTimeout(() => {
            try {
              if (typeof rejectedFunc !== "function") {
                reject(this.promiseResult);
              } else {
                let x = rejectedFunc(this.promiseResult);
                resolvePromise(newPromise, x, resolve, reject);
              }
            } catch (error) {
              reject(error);
            }
          });
        });
      }
      if (this.promiseState == myPromise.FULFILLED) {
        setTimeout(() => {
          try {
            if (typeof fulfilledFunc !== "function") {
              resolve(this.promiseResult);
            } else {
              let x = fulfilledFunc(this.promiseResult);
              resolvePromise(newPromise, x, resolve, reject);
            }
          } catch (error) {
            reject(error);
          }
        });
      }
      if (this.promiseState == myPromise.REJECTED) {
        setTimeout(() => {
          try {
            if (typeof rejectedFunc !== "function") {
              reject(this.promiseResult);
            } else {
              let x = rejectedFunc(this.promiseResult);
              resolvePromise(newPromise, x, resolve, reject);
            }
          } catch (error) {
            reject(error);
          }
        });
      }
    });
    return newPromise;
  }
}

function resolvePromise(newPromise, x, resolve, reject) {
  if (x === newPromise) {
    // 因为x是回调的结果值，如果x指向newPromise即自己，那么会重新解析自己，导致循环调用
    throw new TypeError("禁止循环调用");
  }
  
  // 如果x是一个Promise，我们必须等它完成（失败或成功）后得到一个普通值时，才能继续执行。
  // 那我们把要执行的任务放在x.then（）的成功回调和失败回调里面即可
  // 这就表示x完成后就会调用我们的代码。
  
  // 但是对于成功的情况,我们还需要再考虑下,x.then成功回调函数的参数,我们称为y
  // 那y也可能是一个thenable对象或者promise
  // 所以如果成功时，执行resolvePromise(promise2, y, resolve, reject)
  // 并且传入resolve, reject，当解析到普通值时就resolve出去，反之继续解析
  // 这样子用于保证最后resolve的结果一定是一个非promise类型的参数
  if (x instanceof myPromise) {
    x.then((y) => {
      resolvePromise(newPromise, y, resolve, reject);
    },  r => reject(r));
  } 
  // (x instanceof myPromise) 处理了promise的情况，但是很多时候交互的promise可能不是原生的
  // 就像我们现在写的一个myPromise一样，这种有then方法的对象或函数我们称为thenable。
  // 因此我们需要处理thenable。
  else if ((typeof x === "object" || typeof x === "function") && x !== null ) {
    try {
      // 暂存x这个对象或函数的then，x也可能没有then，那then就会得到一个undefined
      var then = x.then;
    } catch (e) {
      // 如果读取then的过程中出现异常则reject异常出去
      return reject(e);
    }
    // 判断then是否函数且存在，如果函数且存在那这个就是合理的thenable，我们要尝试去解析
    if (typeof then === "function") {
      // 状态只能更新一次使用一个called防止反复调用
      // 因为成功和失败的回调只能执行其中之一
      let called = false;
      try {
        then.call(
          x,
          (y) => {
            // called就是用于防止成功和失败被同时执行，因为这个是thenable，不是promise
            // 需要做限制如果newPromise已经成功或失败了，则不会再处理了
            if (called) return;
            called = true;
            resolvePromise(newPromise, y, resolve, reject);
          },
          (r) => {
            // called就是用于防止成功和失败被同时执行，因为这个是thenable，不是promise
            // 需要做限制如果newPromise已经成功或失败了，则不会再处理了
            if (called) return;
            called = true;
            reject(r);
          }
        );
        // 上面那一步等价于，即这里把thenable当作类似于promise的对象去执行then操作
        // x.then(
        //   (y) => {
        //     if (called) return;
        //     called = true;
        //     resolvePromise(newPromise, y, resolve, reject);
        //   },
        //   (r) => {
        //     if (called) return;
        //     called = true;
        //     reject(r);
        //   }
        // )
      } catch (e) {
        // called就是用于防止成功和失败被同时执行，因为这个是thenable，不是promise
        // 需要做限制如果newPromise已经成功或失败了，则不会再处理了
        if (called) return;
        called = true;
        reject(e);
      }
    } else {
      // 如果是对象或函数但不是thenable（即没有正确的then属性）
      // 当成普通值则直接resolve出去
      resolve(x);
    }
  } 
  // 如果既不是promise，也不是非null的对象或函数，当成普通值则直接resolve出去
  else {
    return resolve(x);
  }
}

```



























