# ip
maitube
maitube.com/7/1.php











几个高精度IP定位网站：
https://ip.rtbasia.com/
https://www.opengps.cn/Data/IP/LocHighAcc.aspx
http://www.ipplus360.com/
http://chaipip.com/

IP信息综合查询：
https://www.ipip.net/ip.html
https://bgp.he.net/






127.0.0.1是本机的环回地址。所有**127.x.x.x**都是环回地址。从127.0.0.0 到 127.255.255.255 均予以保留。此地址块中的任何地址都将环回到本地主机中。此地址块中的任何地址都绝不会出现在任何网络中。

0.0.0.0代表本机上任何IP地址。

>IPv4地址分为A、B、C、D、E五类，出去特殊作用的D、E两类，剩下的A、B、C三类地址是我们常见的IP地址段。A类地址的容量最大，可以容纳16777214个主机，B类地址可以容纳65534个主机，C类地址可以容纳254个主机。
>在这三类地址中，绝大多数的IP地址都是**公有地址**，需要向国际互联网信息中心申请注册。但是在IPv4地址协议中预留了3个IP地址段，作为**私有地址**，供组织机构内部使用。
>这三个地址段分别位于A、B、C三类地址内：
>
>- A类地址：10.0.0.0--10.255.255.255
>- B类地址：**172.16.0.0--172.31.255.255** 
>- 局域网在选取使用私有地址时，一般会按照实际需要容纳的主机数来选择私有地址段。常见的局域网由于容量小，一般选择C类的192.168.0.0作为地址段使用，一些大型企业就需要使用B类甚至A类地址段作为内部网络的地址段。
>- C类地址：**192.168.0.0--192.168.255.255**

下文中192.168.X.X.的是大学宿舍区附近服务器的内网 `ip`地址---C类地址
下文寝室网络向外访问基本都要连续经过这四个ip地址：
0.0.0.0//笔记本广播
127.0.0.1//笔记本环回地址
172.17.64.1//本地局域网
172.26.10.131
//https://www.ip138.com/iplookup.asp?ip=172.26.10.131&action=2 查到“本地局域网”。但是如果使用网站 https://www.chaipip.com/ 查到172-26-10-131是天安门中山公园。

冒号后的“端口号不怎么重要”

`cmd`命令行`netstat -a`查询的`ip`地址信息：

- `netstat -a`或--all 显示所有连线中的Socket。
- `netstat -n`或--numeric 直接使用IP地址，而不通过域名服务器。










