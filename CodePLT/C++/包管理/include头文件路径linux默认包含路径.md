















linux默认包含路径


【1】include头文件路径
    除了默认的/usr/include, /usr/local/include等include路径外，还可以通过设置环境变量来添加系统include的路径：
    # C
    export C_INCLUDE_PATH=XXXX:$C_INCLUDE_PATH
    # CPP
    export CPLUS_INCLUDE_PATH=XXX:$CPLUS_INCLUDE_PATH
    
    以上修改可以直接命令行输入（一次性），可以在/etc/profile中完成（对所有用户生效），也可以在用户home目录下的.bashrc或.bash_profile中添加（针对某个用户生效），修改完后重新登录即生效。

【2】link链接库文件路径
    链接库文件在连接（静态库和共享库）和运行（仅限于使用共享库的程序）时被使用，其搜索路径是在系统中进行设置的（也可以在编译命令中通过 -l  -L 来指定，这里讲的是使用系统默认搜索路径）。
    一般 Linux 系统把 /lib  /usr/lib  /usr/local/lib 作为默认的库搜索路径，所以使用这几个目录中的链接库文件可直接被搜索到（不需要专门指定链接库路径）。对于默认搜索路径之外的库，则需要将其所在路径添加到gcc/g++的搜索路径之中。
    链接库文件的搜索路径指定有两种方式：1）修改/etc/so.ld.conf   2）修改环境变量，在其中添加自己的路径
    
    1）在环境变量中添加
    动态链接库搜索路径：
    export LD_LIBRARY_PATH=XXX:$LD_LIBRARY_PATH
    静态链接库搜索路径：
    export LIBRARY_PATH=XXX:$LIBRARY_PATH
    以上修改可以直接命令行输入（一次性），可以在/etc/profile中完成（对所有用户生效），也可以在用户home目录下的.bashrc或.bash_profile中添加（针对某个用户生效）,修改完后重新登录即生效。

    2）在/etc/ld.so.conf 中添加指定的链接库搜索路径（需要root权限），然后运行 /sbin/ldconfig，以达到刷新 /etc/ld.so.cache的效果。
    
    以上两种方式均可以达到指定链接库搜索路径的效果。
    
    第二种搜索路径的设置方式对于程序连接时的库（包括共享库和静态库） 的定位已经足够了，但是对于使用了共享库的程序的执行还是不够的。这是因为为了加快程序执行时对共享库的定位速度，避免使用搜索路径查找共享库的低效率，系统会直接读取 /etc/ld.so.cache 并从中进行搜索的。/etc/ld.so.cache 是一个非文本的数据文件，不能直接编辑，它是根据 /etc/ld.so.conf 中设置的搜索路径由 /sbin/ldconfig 命令将这些搜索路径下的共享库文件集中在一起而生成的（ldconfig 命令要以 root 权限执行）。因此，为了保证程序执行时对库的定位，在 /etc/ld.so.conf 中进行了库搜索路径的设置之后，还要运行 /sbin/ldconfig 命令，更新 /etc/ld.so.cache 文件。
    ldconfig的作用就是将/etc/ld.so.conf 指定的路径下的库文件缓存到/etc/ld.so.cache 。因此当安装完一些库文件(例如刚安装好glib)，或者修改ld.so.conf增加新的库路径后，需要运行一下/sbin/ldconfig 使所有的库文件都被缓存到ld.so.cache中，不然修改的内容就等于没有生效。
    在程序连接时，对于库文件（静态库和共享库）的搜索路径，除了上面的设置方式之外，还可以通过 -L 和 -l 参数显式指定。因为用 -L 设置的路径将被优先搜索，所以在连接的时候通常都会以这种方式直接指定要连接的库的路径。

注意：
    1）在配置环境变量的时候，等号前面不要加空格，否则可能出现 command not found
    2）修改/etc/ld.so.conf后，当系统重新启动后，所有基于 GTK2 的程序在运行时都将使用新安装的 GTK+ 库。由于 GTK+ 版本的改变，有时会给应用程序带来兼容性的问题，造成某些程序运行不正常。为了避免出现这些情况，在 GTK+ 及其依赖库的安装过程中对于库的搜索路径的设置将采用环境变量的方式
    export LD_LIBRARY_PATH=/opt/gtk/lib:$LD_LIBRARY_PATH
    


# include











对于 C/C++ 标准库头文件，直接 #include <文件名> 即可。

项目内自己编写的头文件，使用 #include "文件名"。 

对于第三方头文件或自己编写的项目外头文件，有三种方法：

（推荐）编辑项目目录下的 CMakeLists.txt，添加一行include_directories("/path/to/headers") #换成头文件所在目录如果有多个目录，每一个目录写一行然后在源文件中使用 #include <文件名> 包含

2.将对应的头文件或文件夹复制到项目根目录，然后在源文件中使用 #include "文件名" 包含

3.在源文件内直接使用 #include "相对路径或绝对路径" 包含


链接：https://www.zhihu.com/question/313373365/answer/1631977302








为什么qnp2fond中problem.h文件中14行 #include "problem.h"包含自己？









