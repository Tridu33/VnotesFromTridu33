# cygwin




```cmd
$ mount
D:/OCaml64/bin on /usr/bin type ntfs (binary,auto)
D:/OCaml64/lib on /usr/lib type ntfs (binary,auto)
D:/OCaml64 on / type ntfs (binary,auto)
C: on /cygdrive/c type ntfs (binary,posix=0,user,noumount,auto)
D: on /cygdrive/d type ntfs (binary,posix=0,user,noumount,auto)
G: on /cygdrive/g type iso9660 (binary,posix=0,user,noumount,auto)
H: on /cygdrive/h type vfat (binary,posix=0,user,noumount,auto)

```


D:\OCaml64\home\HUMAN HOME家目录就是本地这个文件位置

D:\OCaml64
```bash
Cygwin-Terminal.ico  Cygwin.ico  cygdrive  etc   lib   sbin  usr
Cygwin.bat           bin         dev       home  proc  tmp   var

```


跳转硬盘任意位置：

```bash
 cd /cygdrive/d
 cd /cygdrive/d/tridu33
 cd /cygdrive/c
```

在 Cygwin 中以路径 /cygdrive/c/Windows来访问Windows 下的 C:\Windows 目录。实际上， Cygwin 提供 cygpath 命令来实现 Windows 平台和 Cygwin 之间目录名称的变换，如下所示：












