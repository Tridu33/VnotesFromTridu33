PS C:\WINDOWS\system32> $paths = (dir Env:\PSModulePath).Value.Split(";")
PS C:\WINDOWS\system32> Test-Path -Path $paths[0]

True

PS C:\WINDOWS\system32> $paths

C:\Users\shinelon\Documents\WindowsPowerShell\Modules
C:\Program Files\WindowsPowerShell\Modules
C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules
下载的showUI复制到第一个路径就能安装！
PS C:\WINDOWS\system32> Import-Module ShowUI
Get-ChildItem : 找不到路径“C:\Users\shinelon\Documents\WindowsPowerShell\Modules\ShowUI\StyleSystem\Styles”，因为该路
径不存在。
所在位置 C:\Users\shinelon\Documents\WindowsPowerShell\Modules\ShowUI\StyleSystem\Import-UIStyle.ps1:33 字符: 33
+ ... ($style in (Get-ChildItem -Force -Filter *.style -Path $psScriptRoot\ ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Users\shinel...leSystem\Styles:String) [Get-ChildItem], ItemNotFound
   Exception
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.GetChildItemCommand

Use-UiStyle : No Style named Current found
所在位置 C:\Users\shinelon\Documents\WindowsPowerShell\Modules\ShowUI\ShowUI.psm1:229 字符: 5
+     Use-UiStyle "Current"
+     ~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Write-Error], WriteErrorException
    + FullyQualifiedErrorId : Microsoft.PowerShell.Commands.WriteErrorException,Import-UIStyle
    报错如上
www.drdobbs.com/windows/building-gui-applications-in-powershell/240049898


**入门级别**

　　1\. 像文件系统那样操作Windows Registry——cd hkcu:  
　　2\. 在文件里递回地搜索某个字符串——dir –r | select string "searchforthis"   
　　  
　　3\. 使用内存找到五个进程——ps | sort –p ws | select –last 5  
　　4\. 循环（停止，然后重启）一个服务，如DHCP——Restart-Service DHCP  
　　5\. 在文件夹里列出所有条目——Get-ChildItem – Force  
　　6\. 递归一系列的目录或文件夹——Get-ChildItem –Force c:\\directory –Recurse  
　　7\. 在目录里移除所有文件而不需要单个移除——Remove-Item C:\\tobedeleted –Recurse  
　　8\. 重启当前计算机——(Get-WmiObject -Class Win32_OperatingSystem -ComputerName .).Win32Shutdown(2)

　　**收集信息**

　　9\. 获取计算机组成或模型信息——Get-WmiObject -Class Win32_ComputerSystem  
　　10\. 获取当前计算机的BIOS信息——Get-WmiObject -Class Win32_BIOS -ComputerName .  
　　11\. 列出所安装的修复程序（如QFE或Windows Update文件）——Get-WmiObject -Class Win32_QuickFixEngineering -ComputerName .  
　　12\. 获取当前登录计算机的用户的用户名—— Get-WmiObject -Class Win32_ComputerSystem -Property UserName -ComputerName .  
　　13\. 获取当前计算机所安装的应用的名字——Get-WmiObject -Class Win32_Product -ComputerName . | Format-Wide -Column 1  
　　14\. 获取分配给当前计算机的IP地址——Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Filter IPEnabled=TRUE -ComputerName . | Format-Table -Property IPAddress  
　　15\. 获取当前机器详细的IP配置报道——Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Filter IPEnabled=TRUE -ComputerName . | Select-Object -Property \[a-z\]* -ExcludeProperty IPX*,WINS*  
　　16\. 找到当前计算机上使用DHCP启用的网络卡——Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Filter "DHCPEnabled=true" -ComputerName .  
　　17\. 在当前计算机上的所有网络适配器上启用DHCP——Get-WmiObject -Class Win32\_NetworkAdapterConfiguration -Filter IPEnabled=true -ComputerName . | ForEach-Object -Process {$\_.EnableDHCP()}

　　**软件管理**

　　18\. 在远程计算机上安装MSI包——(Get-WMIObject -ComputerName TARGETMACHINE -List | Where-Object -FilterScript {$_.Name -eq "Win32_Product"}).Install(\\\MACHINEWHEREMSIRESIDES\\path\\package.msi)  
　　19\. 使用基于MSI的应用升级包升级所安装的应用——(Get-WmiObject -Class Win32\_Product -ComputerName . -Filter "Name='name\_of\_app\_to\_be\_upgraded'").Upgrade(\\\MACHINEWHEREMSIRESIDES\\path\\upgrade_package.msi)  
　　20\. 从当前计算机移除MSI包——(Get-WmiObject -Class Win32\_Product -Filter "Name='product\_to_remove'" -ComputerName . ).Uninstall()  
　　机器管理  
　　21\. 一分钟后远程关闭另一台机器——Start-Sleep 60; Restart-Computer –Force –ComputerName TARGETMACHINE  
　　22\. 添加打印机——(New-Object -ComObject WScript.Network).AddWindowsPrinterConnection(\\\printerserver\\hplaser3)  
　　23\. 移除打印机——(New-Object -ComObject WScript.Network).RemovePrinterConnection("\\\printerserver\\hplaser3 ")  
　　24\. 进入PowerShell会话——invoke-command -computername machine1, machine2 -filepath c:\\Script\\script.ps1
[showUI](https://github.com/ShowUI/ShowUI)










www.cnblogs.com/ceachy/archive/2013/03/08/PowerShell_Script_Module.html














