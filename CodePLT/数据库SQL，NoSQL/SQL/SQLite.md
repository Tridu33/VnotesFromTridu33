# 1. SQLite





[菜鸟SQLite教程https://www.runoob.com/sqlite/sqlite-tutorial.html](https://www.runoob.com/sqlite/sqlite-tutorial.html)





# 2. SQLite 教程

SQLite 是一个软件库，实现了自给自足的、无服务器的、零配置的、事务性的 SQL 数据库引擎。SQLite 是在世界上最广泛部署的 SQL 数据库引擎。SQLite 源代码不受版权限制。

本教程将告诉您如何使用 SQLite 编程，并让你迅速上手。

**[现在开始学习 SQLite！](https://www.runoob.com/sqlite/sqlite-intro.html)**

## 2.1. 谁适合阅读本教程？

本教程有助于初学者了解 SQLite 数据库引擎相关的基础知识和先进理念。

## 2.2. 阅读本教程前，你需要了解的知识：

在开始使用本教程提供的各类实例进行练习之前，您需要了解什么是数据库，尤其是 RDBMS，以及什么是计算机编程语言。

## 2.3. 编译/执行 SQLite 程序

如果您想要通过 SQLite DBMS 编译/执行 SQL 程序，但是您没有相关设置，那么可以访问 [compileonline.com](http://www.compileonline.com/execute_sql_online.php "在线编译 SQL")。您只需进行简单的点击动作，即可在高端的服务器上体验真实的编程经验。这是完全免费的在线工具。

## 2.4. SQLite 函数参考手册

本教程提供了所有重要的内置的 SQLite 函数的参考手册。

[SQLite 常用函数](https://www.runoob.com/sqlite/sqlite-functions.html)

## 2.5. SQLite 有用的资源

本教程列出了 SQLite 数据库网站和书籍。

#### 2.5.1.1. SQLite 有用的网站

-   [SQLite Home Page](http://www.sqlite.org/) \- SQLite 官方网站提供了最新的 SQLite 安装版本，最新的 SQLite 资讯以及完整的 SQLite 教程。
    
-   [PHP SQLite3](http://www.php.net/manual/en/book.sqlite3.php) \- 网站提供了 SQLite 3 数据库的 PHP 支持的完整细节。
    
-   [SQLite JDBC Driver:](https://bitbucket.org/xerial/sqlite-jdbc) \- SQLite JDBC，由 Taro L. Saito 开发的，是一个用于 Java 中访问和创建 SQLite 数据库文件的库。
    
-   [DBD-SQLite-0.31](http://search.cpan.org/~msergeant/DBD-SQLite-0.31/) \- SQLite Perl driver 驱动程序与 Perl DBI 模块一起使用。
    
-   [DBI-1.625](http://search.cpan.org/~timb/DBI/) \- Perl DBI 模块为包括 SQLite 在内的任何数据库提供了通用接口。
    
-   [SQLite Python](http://docs.python.org/2/library/sqlite3.html) \- sqlite3 python 模块由 Gerhard Haring 编写的。它提供了与 DB-API 2.0 规范兼容的 SQL 接口。



```sql
SQLite version 3.26.0 2018-12-01 12:34:55
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> .help
.archive ...             Manage SQL archives
.auth ON|OFF             Show authorizer callbacks
.backup ?DB? FILE        Backup DB (default "main") to FILE
.bail on|off             Stop after hitting an error.  Default OFF
.binary on|off           Turn binary output on or off.  Default OFF
.cd DIRECTORY            Change the working directory to DIRECTORY
.changes on|off          Show number of rows changed by SQL
.check GLOB              Fail if output since .testcase does not match
.clone NEWDB             Clone data into NEWDB from the existing database
.databases               List names and files of attached databases
.dbconfig ?op? ?val?     List or change sqlite3_db_config() options
.dbinfo ?DB?             Show status information about the database
.dump ?TABLE? ...        Render all database content as SQL
.echo on|off             Turn command echo on or off
.eqp on|off|full         Enable or disable automatic EXPLAIN QUERY PLAN
.excel                   Display the output of next command in a spreadsheet
.exit ?CODE?             Exit this program with return-code CODE
.expert                  EXPERIMENTAL. Suggest indexes for specified queries
.fullschema ?--indent?   Show schema and the content of sqlite_stat tables
.headers on|off          Turn display of headers on or off
.help ?-all? ?PATTERN?   Show help text for PATTERN
.import FILE TABLE       Import data from FILE into TABLE
.imposter INDEX TABLE    Create imposter table TABLE on index INDEX
.indexes ?TABLE?         Show names of indexes
.limit ?LIMIT? ?VAL?     Display or change the value of an SQLITE_LIMIT
.lint OPTIONS            Report potential schema issues.
.load FILE ?ENTRY?       Load an extension library
.log FILE|off            Turn logging on or off.  FILE can be stderr/stdout
.mode MODE ?TABLE?       Set output mode
.nullvalue STRING        Use STRING in place of NULL values
.once (-e|-x|FILE)       Output for the next SQL command only to FILE
.open ?OPTIONS? ?FILE?   Close existing database and reopen FILE
.output ?FILE?           Send output to FILE or stdout if FILE is omitted
.print STRING...         Print literal STRING
.prompt MAIN CONTINUE    Replace the standard prompts
.quit                    Exit this program
.read FILE               Read input from FILE
.restore ?DB? FILE       Restore content of DB (default "main") from FILE
.save FILE               Write in-memory database into FILE
.scanstats on|off        Turn sqlite3_stmt_scanstatus() metrics on or off
.schema ?PATTERN?        Show the CREATE statements matching PATTERN
.selftest ?OPTIONS?      Run tests defined in the SELFTEST table
.separator COL ?ROW?     Change the column and row separators
.sha3sum ...             Compute a SHA3 hash of database content
.shell CMD ARGS...       Run CMD ARGS... in a system shell
.show                    Show the current values for various settings
.stats ?on|off?          Show stats or turn stats on or off
.system CMD ARGS...      Run CMD ARGS... in a system shell
.tables ?TABLE?          List names of tables matching LIKE pattern TABLE
.testcase NAME           Begin redirecting output to 'testcase-out.txt'
.timeout MS              Try opening locked tables for MS milliseconds
.timer on|off            Turn SQL timer on or off
.trace FILE|off          Output each SQL statement as it is run
.vfsinfo ?AUX?           Information about the top-level VFS
.vfslist                 List all available VFSes
.vfsname ?AUX?           Print the name of the VFS stack
.width NUM1 NUM2 ...     Set column widths for "column" mode





```

SQLite3不支持存储过程：

[https://www.sqlite.org/whentouse.html](https://www.sqlite.org/whentouse.html)
[https://stackoverflow.com/questions/3402841/does-sqlite-support-store-procedures](https://stackoverflow.com/questions/3402841/does-sqlite-support-store-procedures)






```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```


```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```


```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```


```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```


```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```


```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```


```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```




```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```





```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```



```sql



```







































bash


```bash
For more information on a specific command, type HELP command-name
ASSOC          Displays or modifies file extension associations.
ATTRIB         Displays or changes file attributes.
BREAK          Sets or clears extended CTRL+C checking.
BCDEDIT        Sets properties in boot database to control boot loading.
CACLS          Displays or modifies access control lists (ACLs) of files.
CALL           Calls one batch program from another.
CD             Displays the name of or changes the current directory.
CHCP           Displays or sets the active code page number.
CHDIR          Displays the name of or changes the current directory.
CHKDSK         Checks a disk and displays a status report.
CHKNTFS        Displays or modifies the checking of disk at boot time.
CLS            Clears the screen.
CMD            Starts a new instance of the Windows command interpreter.
COLOR          Sets the default console foreground and background colors.
COMP           Compares the contents of two files or sets of files.
COMPACT        Displays or alters the compression of files on NTFS partitions.
CONVERT        Converts FAT volumes to NTFS.  You cannot convert the
               current drive.
COPY           Copies one or more files to another location.
DATE           Displays or sets the date.
DEL            Deletes one or more files.
DIR            Displays a list of files and subdirectories in a directory.
DISKPART       Displays or configures Disk Partition properties.
DOSKEY         Edits command lines, recalls Windows commands, and
               creates macros.
DRIVERQUERY    Displays current device driver status and properties.
ECHO           Displays messages, or turns command echoing on or off.
ENDLOCAL       Ends localization of environment changes in a batch file.
ERASE          Deletes one or more files.
EXIT           Quits the CMD.EXE program (command interpreter).
FC             Compares two files or sets of files, and displays the
               differences between them.
FIND           Searches for a text string in a file or files.
FINDSTR        Searches for strings in files.
FOR            Runs a specified command for each file in a set of files.
FORMAT         Formats a disk for use with Windows.
FSUTIL         Displays or configures the file system properties.
FTYPE          Displays or modifies file types used in file extension
               associations.
GOTO           Directs the Windows command interpreter to a labeled line in
               a batch program.
GPRESULT       Displays Group Policy information for machine or user.
GRAFTABL       Enables Windows to display an extended character set in
               graphics mode.
HELP           Provides Help information for Windows commands.
ICACLS         Display, modify, backup, or restore ACLs for files and
               directories.
IF             Performs conditional processing in batch programs.
LABEL          Creates, changes, or deletes the volume label of a disk.
MD             Creates a directory.
MKDIR          Creates a directory.
MKLINK         Creates Symbolic Links and Hard Links
MODE           Configures a system device.
MORE           Displays output one screen at a time.
MOVE           Moves one or more files from one directory to another
               directory.
OPENFILES      Displays files opened by remote users for a file share.
PATH           Displays or sets a search path for executable files.
PAUSE          Suspends processing of a batch file and displays a message.
POPD           Restores the previous value of the current directory saved by
               PUSHD.
PRINT          Prints a text file.
PROMPT         Changes the Windows command prompt.
PUSHD          Saves the current directory then changes it.
RD             Removes a directory.
RECOVER        Recovers readable information from a bad or defective disk.
REM            Records comments (remarks) in batch files or CONFIG.SYS.
REN            Renames a file or files.
RENAME         Renames a file or files.
REPLACE        Replaces files.
RMDIR          Removes a directory.
ROBOCOPY       Advanced utility to copy files and directory trees
SET            Displays, sets, or removes Windows environment variables.
SETLOCAL       Begins localization of environment changes in a batch file.
SC             Displays or configures services (background processes).
SCHTASKS       Schedules commands and programs to run on a computer.
SHIFT          Shifts the position of replaceable parameters in batch files.
SHUTDOWN       Allows proper local or remote shutdown of machine.
SORT           Sorts input.
START          Starts a separate window to run a specified program or command.
SUBST          Associates a path with a drive letter.
SYSTEMINFO     Displays machine specific properties and configuration.
TASKLIST       Displays all currently running tasks including services.
TASKKILL       Kill or stop a running process or application.
TIME           Displays or sets the system time.
TITLE          Sets the window title for a CMD.EXE session.
TREE           Graphically displays the directory structure of a drive or
               path.
TYPE           Displays the contents of a text file.
VER            Displays the Windows version.
VERIFY         Tells Windows whether to verify that your files are written
               correctly to a disk.
VOL            Displays a disk volume label and serial number.
XCOPY          Copies files and directory trees.
WMIC           Displays WMI information inside interactive command shell.

For more information on tools see the command-line reference in the online help.

C:\SQLite>

```






















