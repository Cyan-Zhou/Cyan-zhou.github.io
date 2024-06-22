# 记 NAS 文件迁移


<!--more-->

<p><img src="https://img.shields.io/badge/last%20modified-2024--6--22-ff69b4?style=flat" > <img src="https://img.shields.io/badge/Words-1734-yellow?style=flat" >  <img src="https://img.shields.io/badge/10%20minutes-lightgray?style=flat" ></p>

最近又面临一段物欲爆棚的时期，心愿单上有不少电子产品，正好最近面临严重的手机空间不足，为了一劳永逸解决手机容量问题，在 618 购入了群晖 DS 423+，替代 bro 送给我的西数 Ex2 Ultra。

# 为什么选择 DS 423+ 

首先在品牌上基本没有犹豫，虽然最近国产出了不少新的 NAS品牌，比如绿联、极空间，传统 NAS 品牌也有威联通，但是因为觉得软件的生态和长期稳定性还是 NAS 使用最重要的特点，所以群晖依然是第一选择。

机型上，因为觉得 NAS 还是可以用的更久一些，避免没几年就因为容量不足还要升级装备，所以想选择一款 4 盘位的主机，DS 423+ 基本就是最佳选择，Intel 处理器预留了可玩性，增加了 4G 的原装内存，全套下来也不到 4000。另外买了一张 8T 的西数红盘，加上原来的 2 个 6T 红盘，20T 的总容量应该可以用很长一段时间了。

<center><a data-fancybox="gallery" href="https://images-1319077775.cos.ap-guangzhou.myqcloud.com/2024/06/23-00_08_06-weixin2_8c6.jpg"><img src="https://images-1319077775.cos.ap-guangzhou.myqcloud.com/2024/06/23-00_08_06-weixin2_8c6.jpg" width="1000"></a>
<style>
p.title {line-height:100%; font-size:15px; color:black; font-weight:bold;}
p.source {line-height:70%; font-size:1px; color:gray;}
</style>
<p class="title">
刚好有一个空间放 NAS，ID 好评
</p>
<p class="source">

</p></center>


# 文件迁移


之前我用西数 Ex2 Ultra 主要是整合几个硬盘上的电影、音乐和电子书文件，主机端可以随时查看电子书，Apple TV 通过 infuse 访问电影，体验不错，但也仅限于家庭内共享，外网访问的速度就很慢了，而且用户界面上，西数感觉也有几年没有更新过 UI 设计。

如何把 4T 文件从 Ex2 Ultra 迁移到群晖中，是遇到的第一个问题。

其实一开始就搞了翻车的操作，我满心以为硬盘里的数据可以跨平台读取，从西数里拆出 2 块硬盘就放进了群晖中。开机设置，直到安装系统提醒我磁盘数据会全部擦除的时候，我才意识到还需要迁移文件。于是重新把硬盘安装回西数，开始思考怎么迁移文件。原 2 块 6T 磁盘上大概有 4T 的文件，如果从西数迁移到外置硬盘，再从外置硬盘迁移到群晖，且不论硬盘有没有这么大空间，光是文件迁移的时间都够我整一个月。

在找了各种解决方案之后，一个方案渐渐成型：将西数、群晖通过网线连接到路由器的 LAN 口，就可以实现数据迁移，直接从西数搬运到群晖。文件迁移完以后再把下岗的硬盘重新挂载到群晖上。方案整体结构很简单，但是没想到遇到了不少问题，也顺便让我学习一些基础的网络配置知识。

第一个问题是没办法登录光猫和路由器的控制面板，在解决这个问题的过程中， [路由器、交换机、光猫的概念](https://blog.csdn.net/weixin_43025343/article/details/138181467?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522171906707116800182745408%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=171906707116800182745408&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-138181467-null-null.142^v100^pc_search_result_base3&utm_term=%E5%85%89%E7%8C%AB%20%E8%B7%AF%E7%94%B1%E5%99%A8&spm=1018.2226.3001.4187)，[光猫和路由器的区别](https://blog.csdn.net/weixin_49171365/article/details/132306283?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522171906707116800182745408%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=171906707116800182745408&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-132306283-null-null.142^v100^pc_search_result_base3&utm_term=%E5%85%89%E7%8C%AB%20%E8%B7%AF%E7%94%B1%E5%99%A8&spm=1018.2226.3001.4187) 两篇文章帮我快速了解了光猫和路由器的工作原理。

众所周知，移动光猫的默认 ip 是 192.168.1.1，华为路由器的默认 ip 是 192.168.3.1，但是我无论如何也没办法登录到这两个地址。幸好，华为还可以从 App 登录，至少让我知道设备应该是没问题，可能是某个设置有变化。几个月前，因为家里的 WiFi 速度慢，我曾经折腾过光猫和路由器一次，所以这次的反常设置应该是由那次设置引起的。

我突然从 App 发现路由器我设置的是 PPPoE 拨号，而不是自动获取 ip 地址。就猜到，可能因为我们家的光猫是调制解调+路由一体机，我把光猫就改成了桥接模式，自然也就没办法搜索到它的 ip 地址。

下面就是路由器的 ip 地址问题，非常诡异。路由器肯定不是桥接模式，所以按理来说没有道理搜不到。我还以为是华为智联的问题，但是家里只有一台路由器，也不应该是智联的原因。从电脑的 WiFi 设置，突然发现了端倪 —— WiFi 的 ip 地址是 192.168.0.1 ！原来是几个月前，因为每次 NAS 断电会被路由器重新分配 ip 地址，infuse 要重新设置网盘访问，所以我索性把路由器和 NAS 的 ip 地址都固定了。

<center><a data-fancybox="gallery" href="https://images-1319077775.cos.ap-guangzhou.myqcloud.com/2024/06/22-23_01_06-20240622230114_83c.png"><img src="https://images-1319077775.cos.ap-guangzhou.myqcloud.com/2024/06/22-23_01_06-20240622230114_83c.png" width="1000"></a>
<style>
p.title {line-height:100%; font-size:15px; color:black; font-weight:bold;}
p.source {line-height:70%; font-size:1px; color:gray;}
</style>

<p class="title">
鬼知道我看到这个界面的时候有多兴奋
</p>
<p class="source">

</p></center>

解决了这些问题，实际上只是帮助我弄明白这些电子设备之间的关系。此时电脑上可以看到 2 个 NAS，尽管他们之间是通过网线连接的，但是文件传输的速度只有 10+ MB/s，明显太慢。恰好，之前买了一根 5 米的网线，于是把网线从路由器的最后一个 LAN 口连接到了主板。此时新的问题出现了，虽然以太网已经连接上，但是没有数据传输。在排查未果以后，复制之前的思路，从以太网的设置界面查看 ipv4 的地址，果然！不知道什么时候，这台电脑的以太网 ip 和 DNS 都是手动设置过的（可能是之前还在学校的时候，因为要用 ipv6 所以做了很多手动设置），改为自动获取以后，文件传输终于来到了 60-80 MB/s 的水平。4T 文件终于周日一天应该可以传输完成。


{{< admonition note "See you later" false >}}

未完待续

{{< /admonition >}}

