# 1. js调用bat文件







**dos下创建bat文件更改IP**

（创建一个文件后缀改成.bat在Windows上就可以双击运行）

  

set addr=192.168.101.101

  
set mask=255.255.255.0  
  
set gateway=192.168.101.1  
  
set dns=202.96.69.38  
  
netsh interface ip set address name="本地连接" source=static addr=%addr% mask=%mask% gateway=%gateway%  
  

netsh interface ip set dns "本地连接" source=static addr=%dns%

  

**dos下创建bat文件打开目录**

@start "" "C:\\wamp\\www"

  

**dos下创建bat文件对PLSQL Developer进行转码后在运行**  

@echo off  
set path=F:\\app\\Administrator\\product\\instantclient\_10\_2  
set ORACLE\_HOME=F:\\app\\Administrator\\product\\instantclient\_10_2  
set TNS\_ADMIN=F:\\app\\Administrator\\product\\instantclient\_10_2  
set NLS_LANG=AMERICAN_AMERICA.AL32UTF8  
@start "" "D:\\yingyong\\PLSQL Developer\\plsqldev.exe"

  

**dos下创建bat文件启动应用程序wampserver**  

@start "" "C:\\wamp\\wampmanager.exe"












































