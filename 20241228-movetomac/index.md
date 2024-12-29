# 博客环境搬运 Mac 笔记


<!--more-->

<p><img src="https://img.shields.io/badge/last%20modified-2022--0--0-ff69b4?style=flat" > <img src="https://img.shields.io/badge/Words-00-yellow?style=flat" >  <img src="https://img.shields.io/badge/00%20minutes-lightgray?style=flat" ></p>

最近新添置了 Mac Mini 替换服役了 7 年的 windows 主机，除了文件和软件搬运外，一直拖着没有解决的问题就是博客的配置。恰好最近和 ChatGPT 的协作越来越深入，在博客配置上，我预测 GPT 可以帮我解决不少博客配置上我不了解的问题。所以博客搬运就在和 GPT 的协作对话中开始了。

## 基本软件下载

首先要搞定的是 hugo、git 的配置问题，mac 平台上要下载 homebrew ，然后安装 hugo

> Homebrew 是一个 **包管理器**，用于在 macOS 上安装和管理命令行工具和软件。它的操作完全基于 **终端（Terminal）**，而不是通过图形化界面，因此你需要通过命令行与它交互。


我本来想把博客挂载在 NAS 上，这样可以实现跨设备的文件管理，但是后面发现可行性上有问题，我们先按照这个目标配置，后面在揭晓问题在哪里。

打开Nas的AFP服务，在 **Synology DSM** 中，前往“控制面板 -> 文件服务”，启用 **AFP** 协议

nas的地址是 /Volumes/folder-name, 可以直接把文件夹拖入到terminal，就可以快速输入文件夹对应的路径。

安装hugo，git和picgo。git可以按照git官网的指引，通过brew安装即可

```
brew install hugo 
hugo version

```

安装picgo的时候遇到了没想到的困难（都怪之前配置picgo的时候没有记录教程），磕磕绊绊终于搞定了，其实也并不复杂。我希望实现的功能是在vs code 写md 文档的时候，可以实现剪贴板上传，并且把URL按照需要的格式返回到剪贴板中。

Step1: 安装 picgo，需要重点完成几个配置：

* 图床设置部分：选择自己用的云服务，配置API。我是用的腾讯云，这里需要录入 COS版本、secretid、secretKey、bucket、appId、存储区域几个字段。其中需要特别关注 secretKey是在腾讯云创建api密钥的时候才能看到的，我只能从windows picgo的配置文件中捞到之前的secretKey，要妥善保存。

* picgo 设置部分，可以修改上传的快捷键，并且让picgo开机自启，上传后自动复制URL

* 插件部分。不清楚是不是因为网络原因，我无法在picgo直接搜索下载插件，最后只能下载插件到本地安装。我安装的是 rename-file 的插件，主要解决存储桶中文件管理的自动重命名文件的问题，要单独配置下格式，这个是我用的命名方法，`{y}/{m}/{d}-{h}_{i}_{m}-{origin}_{rand:3}` 

``` html

# 我希望实现的代码，是一段简单的html，规定了图片的尺寸、标注。其中 $url 是picgo的自定义链接可以识别的图片链接的替换符。
<center><a data-fancybox="gallery" href="$url"><img src="$url" width="1000"></a>
<style>
p.title {line-height:100%; font-size:15px; color:black; font-weight:bold;}
p.source {line-height:100%; font-size:13px; color:gray;}
</style>
<p class="title">
this is title 
</p>
<p class="source">
this is source
</p>
</center>


# 但是因为picgo的链接部分不接受换行，而且直接修改json的话，还是会被设置中配置的url覆写，所以能实现的效果只可能是下面这样，不含换行符号

# 输入在picgo设置界面
<center><a data-fancybox="gallery" href="$url"><img src="$url" width="1000"></a> <style> p.title {line-height:100%; font-size:15px; color:black; font-weight:bold;} p.source {line-height:100%; font-size:13px; color:gray;} </style> <p class="title"> this is title </p> <p class="source"> this is source </p> </center>

# 输出
<center><a data-fancybox="gallery" href="$url"><img src="$url" width="1000"></a> <style> p.title {line-height:100%; font-size:15px; color:black; font-weight:bold;} p.source {line-height:100%; font-size:13px; color:gray;} </style> <p class="title"> this is title </p> <p class="source"> this is source </p> </center>
```

## 在visual studio实现实时预览

在 Visual studio上偶然发现有一款插件 Front Matter，似乎是静态网站必用的神器。在marketplace下载安装 FM 以后，就会看到vs code出现FM的logo。进行一些基本配置以后（重点是选择content文件夹，以及选择hugo或者你使用的静态服务），FM主要有2个作用：

* 可视化界面配置front matter，实现tag管理，以及易懂的界面
* 在hugo server -D 命令执行以后，可以通过 Open preview 直接看到目前正在编辑的文章的网页渲染。



<center><a data-fancybox="gallery" href="https://images-1319077775.cos.ap-guangzhou.myqcloud.com/2024/12/29-16_02_12-20241229160214_d8d.png"><img src="https://images-1319077775.cos.ap-guangzhou.myqcloud.com/2024/12/29-16_02_12-20241229160214_d8d.png" width="1000"></a>
<style>
p.title {line-height:100%; font-size:15px; color:black; font-weight:bold;}
p.source {line-height:100%; font-size:13px; color:gray;}
</style>
<p class="source">
vs code 中实时渲染的效果
</p>
</center>


