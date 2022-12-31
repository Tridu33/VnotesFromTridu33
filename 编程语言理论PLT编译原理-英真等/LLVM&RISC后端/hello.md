# hello




https://www.bilibili.com/video/BV1r4411k72A





```

int main(){
return 42;

```

```
$clang -S -emit-llvm -O3 simple.c
```
second

```
int main (){

    int a=32;

    int b=16;

    return a+b;

}
```
没优化
```
clang -S -emit-llvm  second.c
```

```
; ModuleID = 'second.c'

source_filename = "second.c"
;生成文件

target datalayout = "e-m:w-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

target triple = "x86_64-pc-windows-msvc19.25.28614"

  ;------------------------------------

; Function Attrs: noinline nounwind optnone uwtable

define dso_local i32 @main() #0 {
;%x is local variables,locals represent register注册4寄存器任务， assignments
;registers are "infinite",unlike asm
  %1 = alloca i32, align 4
;"alloca" return a pointer
  %2 = alloca i32, align 4
;分配大小int准备给%2 a
  %3 = alloca i32, align 4
;b %3
  store i32 0, i32* %1, align 4
;sotre the value 0 (i32) into %1（an pointer to an i32）
  store i32 32, i32* %2, align 4
;sotre the value 0 (i32) into a/%2（an pointer to an i32）
  store i32 16, i32* %3, align 4
;sotre the value 0 (i32) into b/%3（an pointer to an i32）
  %4 = load i32, i32* %2, align 4
;load type i32 value from 内存地址memory address  "%2=&a(存32,a pointer to an i32)"  into  %4寄存器
  %5 = load i32, i32* %3, align 4
;load type i32 value from 内存地址memory address  "%3=&b(存16,a pointer to an i32)"  into  %5寄存器
  %6 = add nsw i32 %4, %5
;%6=%4 + %5
  ret i32 %6
;return %6
}

  ;-------------------------------------------

attributes #0 = { noinline nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "frame-pointer"="none" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

  

!llvm.module.flags = !{!0, !1}

!llvm.ident = !{!2}

  

!0 = !{i32 1, !"wchar_size", i32 2}

!1 = !{i32 7, !"PIC Level", i32 2}

!2 = !{!"clang version 10.0.0 "}


```


优化
```
clang -S -emit-llvm -O3 second.cecond.c
```

```
; ModuleID = 'second.c'
source_filename = "second.c"
target datalayout = "e-m:w-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-windows-msvc19.25.28614"

; Function Attrs: norecurse nounwind readnone uwtable
define dso_local i32 @main() local_unnamed_addr #0 {
  ret i32 48;优化后直接记住这个数字48结果
}

attributes #0 = { norecurse nounwind readnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "frame-pointer"="none" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0, !1}
!llvm.ident = !{!2}

!0 = !{i32 1, !"wchar_size", i32 2}
!1 = !{i32 7, !"PIC Level", i32 2}
!2 = !{!"clang version 10.0.0 "}

```


