



# 1. Control Flow Graphs for Java Bytecode




Control Flow Graphs for Java Bytecode


https://www.jacoco.org/jacoco/trunk/doc/flow.html


```java

public static void example() {
    a();
    if (cond()) {
        b();
    } else {
        c();
    }
    d();
}
```


```class
public static example()V
      INVOKESTATIC a()V
      INVOKESTATIC cond()Z
      IFEQ L1
      INVOKESTATIC b()V
      GOTO L2
  L1: INVOKESTATIC c()V
  L2: INVOKESTATIC d()V
      RETURN
```



循环分支执行等



























































