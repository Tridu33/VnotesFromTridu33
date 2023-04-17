# github显示图片失败

[修改host办法：https://blog.csdn.net/qq_38232598/article/details/91346392](https://blog.csdn.net/qq_38232598/article/details/91346392)


```
https://raw.githubusercontent.com/Tridu33/MaxPlusAlgebra_TK_ABC_MN/master/pic/2.png
```

-   199.232.68.133


得到上述网址以后打开[IPAddress.com](https://www.ipaddress.com/)这个网站，在搜索框输入它的域名，就是`https://`到`com`那一部分，俗称二级域名






```C:\Windows\System32\drivers\etc\hosts```


这里文中查到的ip:

```
# GitHub Start 
140.82.113.3      github.com
140.82.114.20     gist.github.com

151.101.184.133    assets-cdn.github.com
151.101.184.133    raw.githubusercontent.com
151.101.184.133    gist.githubusercontent.com
151.101.184.133    cloud.githubusercontent.com
151.101.184.133    camo.githubusercontent.com
151.101.184.133    avatars0.githubusercontent.com
199.232.68.133     avatars0.githubusercontent.com
199.232.28.133     avatars1.githubusercontent.com
151.101.184.133    avatars1.githubusercontent.com
151.101.184.133    avatars2.githubusercontent.com
199.232.28.133     avatars2.githubusercontent.com
151.101.184.133    avatars3.githubusercontent.com
199.232.68.133     avatars3.githubusercontent.com
151.101.184.133    avatars4.githubusercontent.com
199.232.68.133     avatars4.githubusercontent.com
151.101.184.133    avatars5.githubusercontent.com
199.232.68.133     avatars5.githubusercontent.com
151.101.184.133    avatars6.githubusercontent.com
199.232.68.133     avatars6.githubusercontent.com
151.101.184.133    avatars7.githubusercontent.com
199.232.68.133     avatars7.githubusercontent.com
151.101.184.133    avatars8.githubusercontent.com
199.232.68.133     avatars8.githubusercontent.com

# GitHub End

```

刷新缓存

```
ipconfig /displaydns # 显示dns缓存 

ipconfig /flushdns # 刷新DNS记录 

ipconfig /renew # 重请从DHCP服务器获得IP 

```


















