# 1. cpp交叉编译python判断自身运行环境windows





cpp


```cpp
#ifdef WIN32 
#include <string>
#include <iostream>
#include "windows.h"
#include "sys/time.h"
#else  
#include <ovs/resource.h>
#include <sys/time.h>
#endif  
```


python






```python
import platform
 
if platform.system().lower() == 'windows':
    print("windows")
elif platform.system().lower() == 'linux':
    print("linux")


```