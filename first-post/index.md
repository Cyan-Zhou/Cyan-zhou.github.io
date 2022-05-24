# hugo+github page搭建博客备忘录


<!--more-->

打算搭建博客的想法已经有两三年了，一直到最近对代码不再一无所知，而且待业在家才终于决定着手搭建一个简单的博客。之前大概看过squarespace、cargo这类SaaS平台，考虑到第一：这类平台价格太贵，用来做作品集比较划算，只是做博客的话其实没有必要；第二：可玩性不高，作为比较成熟的建站平台，完善的用户体验带来的是弱DIY感。所以最近在网上冲浪的时候偶然发现hugo+github page搭建博客好像并不是很难，用了大概三天时间成功让博客能打开了（其实全过程只需要不到二十分钟...但是遇到了一些奇怪的bug，大概重复了快十次才搭建成功）。这里主要记录一下：搭建流程、遇到的问题，这样之后添加其他内容也很容易。

### 基本操作流程{#Chapter-1}

1. 安装 [Hugo]^(开源静态网站生成工具) 和[Git]^(开源分布式版本控制系统)；
2. 在GitHub新建repository；
3. 通过hugo搭建本地的博客文件框架，之后用git推到github上



### 安装Hugo & Git

1. Hugo的安装在：[Install Hugo](https://gohugo.io/getting-started/installing/) 有详细指南，或者直接在[Hugo GitHub Release Page](https://github.com/gohugoio/hugo/releases) 下载最新版的extended版本，我在*2022/05/21*安装的是[hugo_extended_0.99.1_Windows-64bit.zip](https://github.com/gohugoio/hugo/releases/download/v0.99.1/hugo_extended_0.99.1_Windows-64bit.zip) ，解压后把hugo.exe文件放到指定的安装目录，比如`D:/Program Files/Hugo/bin`，然后打开**win+R &rarr; sysdm.cpl &rarr; Advanced &rarr; Environment Variables &rarr; System variables - path **  添加进去，用cmd输入`Hugo version` 如果显示则成功
2. 直接下载[Git](https://git-scm.com/) 一路下一步

### GitHub新建仓库

作为为了博客才注册GitHub的真正新手，大概理解GitHub是怎么工作的耗费了不少调整的时间，光是不断重头再来新建仓库就做了十遍有余。

1. 新建一个库，这里注意三点：
   1. repository name必须是username.github.io，用户名大小写不敏感
   2. 添加一个README文档，倒也不那么重要就是了 :(far fa-grin-tears):
   3. **新手踩坑**，这里设置了`:(fas fa-code-branch): main`作为默认branch，但搭建博客的很多教程依旧基于master的分支来同步文档。这是因为2020年10月1日以后Github把新建仓库的默认分支从master改为main了，其实只需要在仓库的设置里把**branch**和**pages** 中的有关设置从main改为master即可
   4. 另外这里可以注意一下SSH的问题，网上教程很多，出现问题修改一下就行

### 生成Hugo的网站文件

##### 	新建Hugo网站

1. 新建一个最顶层的文件夹用来放置所有相关文档，比如`E://HugoWebsite`

2. 在cmd输入hugo new site [blog folder name]，生成一套文件框架

3. 选择主题，我直接使用的是LoveIt

 ```bash
 # 切换目录到博客文件夹
 cd [blog folder name]
 # 切换到主题文件夹
 cd themes
 # 下载主题
 git clone https://github.com/dillonzq/LoveIt.git LoveIt
 ```

4. 修改根目录下的config.toml, [LoveIt作者的基本概念](https://hugoloveit.com/zh-cn/theme-documentation-basics/)里的**2.3 基础配置** 和**3.1 网站配置** 两个部分基本囊括了可以修改的部分，直接复制到config中，修改需要修改的部分即可。这里需要注意这连个部分的配置参考中有重复的部分，`[markup]`的部分就有所重合

5. 另外，config中修改头像的话，相对路径指的是blog根目录下的static文件夹，例如，在config中头像的地址为`/images/avatar.png`， 那么它的绝对路径为`E://HugoWebsite/[Blog Folder name]/images/avatar.png`  

 > 图片压缩的快捷操作是用ffmpeg, 在cmd中切换到图片所在文件夹后，使用
 > `ffmpeg -i input.jpg -vf “scale=1920:-1” output.jpg` 
 > 就可以等比例调整图片大小，再也不用打开ps了


##### 	作出修改

​		通常会修改一些配置文件，或者新建or修改博客文章

```bash
#1.在blog name的根目录里右键打开 Git Bash Here
#2.注意不同主题存放博客的位置不同，例如LoveIt存放在posts中，因此使用hugo new posts, 而其他一些主题可能存放在post或者其他名字的文件夹下
hugo new posts/first-post.md
#3.打开hugo server来预览效果，localhost:1313/
hugo server -D
#4.注意，如果有博客中draft为true的话，这里使用hugo serve 是看不到新建的博文的，另一种方式是 hugo serve --buildDrafts， 目的都是overwrite这里draft的参数，但是在在线版本还是要记得修改draft的值为false
#5.如果一切ok的话ctrl+C，之后生成Public文件夹下的用来同步的文件结构
hugo
#6.这一步结束后应该会出现public文件夹，里面的文件就是打算部署的版本
```

### 部署到GitHub远程仓库

##### 第一次运行需要

```bash
# 在Bash中进入public，初始化git库
git init
# Initialized empty Git repository in ...
# 把git本地仓库关联到远程仓库
git remote add origin git@github.com:[username]/[username].github.io.git
# 查看修改状态
git status
# 添加修改过的文件，这里.也可以替换为-A，其实这一步我一开始失败了很多次，修改了config文件以后git add并不会增加修改后的文件，后来不知道多了哪一步操作以后就好了
git add .
# 添加提交内容说明信息，推荐"yyyy/mm/dd-hh:mm"
git commit -m "first commit"
# 提交修改
git push -u origin master
# 这里有可能第一次失败，事实是我也遇到过一次，但后来就没有再出现，出现这样的问题可以参考“渣渣的夏天”的说明
```

### 日常操作

1. #### 新建或修改文章

``` bash
# 当前工作目录：E:\HugoWebsite\[Blog Folder Name]
# 新建文章
hugo new posts/Second.md
#修改
# 本地预览
hugo server -D
# 构建网站文档
hugo
# 切换目录
cd public
git add .
git commit -m "yyyy/mm/dd-hh:mm"
git push origin master
```

2. #### 删除文章

``` bash
# 当前工作目录：E:\HugoWebsite\[Blog Folder Name]
# 在blog/content/posts，blog/public下找到文章删除，后者并不重要，因为public中除了.git文件夹以外的文件都会在hugo命令中重建
hugo server -D
hugo
cd public
git add .
git commit -m "yyyy/mm/dd-hh:mm"
git push origin master
```

### 其他操作

#### 添加favicon

给网页增加一个icon图标，在标签页和书签栏都可以有更个性化的显示。

1. 首先在[favicon generator](https://realfavicongenerator.net/) 里可以上传自己选择的图片（260*260左右），然后一路下一步，在这里下载package
2. 把package里的东西解压到`/themes/LoveIt/exampleSite/static/` （不同主题可能路径不同，我也是试了很多次，只要找到每个static不停地试就差不多），官方文档里只需要放在`/static` 目录，不过我失败了，不知道是什么问题。至于底下这段代码，[Bright's Blog](https://ibrights.github.io/post/blog20210527/) 说可以复制到某个html文件里，但`LoveIt`不需要，如果用前面的步骤没有显示也可以试试
3. 最后`Hugo Server -D`察看有没有更改成功就好了

![favicon](/first_post/favicon.png)

#### admonition用法

一共12个样式，用起来很方便，这里用到了shortcodes的扩展

```markdown
{{</* admonition type=tip title="the name you want" open=true */>}}
Write something here
{{</* /admonition */>}}

# 或者

{{</* admonition tip "the name you want" true */>}}
Write something here
{{</* /admonition */>}}
```

{{<admonition note "Note" true >}}
type = note
{{< /admonition >}}

{{<admonition abstract "Abstract" true >}}
type = abstract
{{< /admonition >}}

{{<admonition info "Info" true >}}
type = info
{{< /admonition >}}

{{<admonition tip "Tip" true >}}
type = tip
{{< /admonition >}}

{{<admonition success "Success" true >}}
type = success
{{< /admonition >}}

{{<admonition question "Question" true >}}
type = question
{{< /admonition >}}

{{<admonition warning "Warning" true >}}
type = warning
{{< /admonition >}}

{{<admonition failure "Failure" true >}}
type = failure
{{< /admonition >}}

{{<admonition danger "Danger" true >}}
type = danger
{{< /admonition >}}

{{<admonition bug "Bug" true >}}
type = bug
{{< /admonition >}}

{{<admonition example "Example" true >}}
type = example
{{< /admonition >}}

{{<admonition quote "Quote" true >}}
type = quote
{{< /admonition >}}

#### 设置评论区

评论区我用的是[Valine]^(简洁高效的无后端评论系统)，过程并不复杂，但也有容易忽视的bug

1. 先在LeanCloud注册国际版账号，获取相关参数，这一步的具体操作可以看[Hugo个人博客添加Valine评论系统](https://shangzg.top/2021-10-19-hugo%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2%E6%B7%BB%E5%8A%A0valine%E8%AF%84%E8%AE%BA%E7%B3%BB%E7%BB%9F/) 
2. 在config文件里配置打开评论，注意要先打开评论，再打开valine的评论，填入appId, appKey, serverURLs，其他的参数参考[valine的官方文档](https://valine.js.org/configuration.html) 
3. 这一步完了以后我天真地以为就出现评论了，但localhost的预览并没有，尝试了第一步里的链接中修改comment.html的操作，也没有生效，最后终于找到是因为hugo server默认环境是development, 而hugo 的默认环境是production
4. 失败，回头再说

### 查阅文档

* [Markdown基本语法](https://www.markdown.xyz/basic-syntax/) 和[Markdown速查表](https://www.markdown.xyz/cheat-sheet/)
* [LoveIt主题作者的博客](https://hugoloveit.com/zh-cn) 以及两篇基本文档[基本概念](https://hugoloveit.com/zh-cn/theme-documentation-basics/) [内容](https://hugoloveit.com/zh-cn/theme-documentation-content/) (内有一些特殊的扩展语法)

### Reference

* [渣渣的夏天的搭建教程，很详细](https://zz2summer.github.io/github-pages-hugo-%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/#%E5%85%AB%E7%BB%86%E8%8A%82%E4%BC%98%E5%8C%96)
* [Claven's blog的记录，讲了域名的流程以及切换到docs的好处，之后再看](https://z24z.com/post/2021/github-pages-for-blog/)
* [评论值得一看，可能会有一些问题的解答](https://zhuanlan.zhihu.com/p/57361697)
* [这个视频讲的很清楚了](https://www.bilibili.com/video/BV1x64y117PX?spm_id_from=333.337.search-card.all.click)
* [Nanshu Wang的教程，主题不同，也有一些新的功能指南](http://nanshu.wang/post/2015-01-31/)
* [雨临Lewis的主题美化和功能增强，超长文，值得研究](https://lewky.cn/posts/hugo-3.2.html/)
* [八荒山人的博客，优化Hugo+LoveIt](https://www.bahuangshanren.tech/2021-2/)
* [风月的博客，Hugo的教程，也很长](https://kuang.netlify.app/blog/hugo.html)
* [Hugo框架中文文档 短代码](https://www.andbible.com/post/hugo-content-management-shortcodes/)
* [给Hugo个人博客添加Valine评论系统](https://shenshilei1022.gitee.io/post/e277/)
* [Hugo搭建博客（一）— 基本设置](https://cloud.tencent.com/developer/article/1722255)
* [[转] 使用Waline搭建博客评论系统](https://blog.h1msk.cc/2021/09/25/%E4%BD%BF%E7%94%A8Waline%E6%90%AD%E5%BB%BA%E5%8D%9A%E5%AE%A2%E8%AF%84%E8%AE%BA%E7%B3%BB%E7%BB%9F/) 写了很详细的vercel配置指南
* [Hugo系列(3.1) - LoveIt主题美化与博客功能增强 · 第二章](https://lewky.cn/posts/hugo-3.1.html/) Waline替代Valine的评论系统

### 总结

* 就目前来看，博客是具有实用性的，但市面少有好用的产品，或者是古旧的新浪博客，或者就是这种需要一定代码的方式，难度并不大，但对于对计算机陌生的新手来说还是有些复杂
* 之后需要搞定切换主题和设置第二个库的方法，或许可以拿来做作品集网站


