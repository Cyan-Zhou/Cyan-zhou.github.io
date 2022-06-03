#  Hugo + GitHub Pages 搭建博客备忘录


<!--more-->

<img src="https://img.shields.io/badge/last%20modified-2022--05--30-ff69b4?style=flat" >   <img src="https://img.shields.io/badge/Hugo version-0.99.1-blue?style=flat" >    <img src="https://img.shields.io/badge/Status-updating-blue?style=flat" >

打算搭建博客的想法已经有两三年了，一直到最近对代码不再一无所知，而且待业在家才终于决定着手搭建一个简单的博客。之前大概看过 Squarespace、Cargo 这类 SaaS 平台，考虑到

* 第一点：这类平台价格太贵，用来做作品集比较划算，只是做博客的话其实没有必要
* 第二点：可玩性不高，作为比较成熟的建站平台，完善的用户体验带来的是弱DIY感

所以最近在网上冲浪的时候偶然发现 Hugo + GitHub Pages 搭建博客好像并不是很难，用了大概三天时间成功让博客能打开了（其实全过程只需要不到二十分钟...但是遇到了一些奇怪的问题，大概重复了快十次才搭建成功）。这里主要记录一下：搭建流程、遇到的问题。

### 基本操作流程{#Chapter-1}

1. 安装 [Hugo]^(开源静态网站生成工具) 和 [Git]^(开源分布式版本控制系统)；
2. 在 GitHub 新建 Repository；
3. 通过 Hugo 搭建本地的博客文件框架，之后用 Git 推到 GitHub 上



### 安装Hugo & Git

1. Hugo的安装在：[Install Hugo](https://gohugo.io/getting-started/installing/) 有详细指南，或者直接在 [Hugo GitHub Release Page](https://github.com/gohugoio/hugo/releases) 下载最新版的extended版本，我在*2022/05/21*安装的是 [hugo_extended_0.99.1_Windows-64bit.zip](https://github.com/gohugoio/hugo/releases/download/v0.99.1/hugo_extended_0.99.1_Windows-64bit.zip) ，解压后把hugo.exe文件放到指定的安装目录，比如`D:/Program Files/Hugo/bin`，然后打开**win+R &rarr; sysdm.cpl &rarr; Advanced &rarr; Environment Variables &rarr; System variables - path **  添加进去，命令行输入`Hugo version` 如果显示则成功
2. 直接下载 [Git](https://git-scm.com/) 一路下一步

### GitHub新建仓库

作为为了博客才注册GitHub的真正新手，大概理解GitHub是怎么工作的耗费了不少调整的时间，光是不断重头再来新建仓库就做了十遍有余。

1. 新建一个库，这里注意三点：
   1. Repository name必须是username.github.io，用户名大小写不敏感
   2. 添加一个README文档，倒也不那么重要就是了 :(far fa-grin-tears):
   3. **新手踩坑**，这里设置了 `:(fas fa-code-branch): main ` 作为默认分支，但搭建博客的很多教程依旧基于 `master` 的分支来同步文档。这是因为2020年10月1日以后 Github 把新建仓库的默认分支从 `master` 改为 `main` 了，其实只需要在仓库的设置里把 **branch** 和 **pages**  中的有关设置从 `main` 改为 `master` 即可
   4. 另外这里可以注意一下 `SSH` 的问题，网上教程很多，出现问题修改一下就行

### 生成Hugo的网站文件

##### 	新建Hugo网站

1. 新建一个最顶层的文件夹用来放置所有相关文档，比如`E://HugoWebsite`

2. 在命令行输入 `hugo new site [blog folder name]` ，生成一套文件框架

3. 选择主题，我直接使用的是 `LoveIt`

 ```bash
 # 切换目录到博客文件夹
 cd [blog folder name]
 # 切换到主题文件夹
 cd themes
 # 下载主题
 git clone https://github.com/dillonzq/LoveIt.git LoveIt
 ```

4. 修改根目录下的 `config.toml` , [LoveIt作者的基本概念 ](https://hugoloveit.com/zh-cn/theme-documentation-basics/)里的 **2.3 基础配置** 和 **3.1 网站配置** 两个部分基本囊括了可以修改的部分，直接复制到 `config` 中，修改需要修改的部分即可。这里需要注意这连个部分的配置参考中有重复的部分，`[markup]` 的部分就有所重合

5. 另外， ` config.toml ` 中修改头像的话，相对路径指的是blog根目录下的 `static` 文件夹，例如，在 `config.toml` 中头像的地址为 `/images/avatar.png` ， 那么它的绝对路径为 `E://HugoWebsite/[Blog Folder name]/images/avatar.png`  

 > 图片压缩的快捷操作是用 `ffmpeg` , 在命令行中切换到图片所在文件夹后，使用
 > `ffmpeg -i input.jpg -vf “scale=1920:-1” output.jpg` 
 > 就可以等比例调整图片大小，再也不用打开PhotoShop了


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
#另外，如果在 push 的时候提示fatal: unable to access ‘https://github.com/...‘，一般是因为服务器的 SSL 证书没有经过第三方机构签署，因此报错，解决方法是解除 SSL 验证就好了，使用下句
git config --global http.sslVerify "false"
```

##### 修改 repository 地址

```bash
# 有时 repository 地址更改，或者填错的情况下，可以移除旧的 origin
git remote rm origin
# 查看是否清除
git remote -v
# 添加新的 origin
git remote add origin master https://....../R.git
```

##### 修改某些设置后没有更新

在 xwi88 和毛哥的帮助下，我终于解决了 giscus 的问题。首先切换到 production 看看是不是解决了问题。如果此时预览实现了更改，而 push 到 GitHub 的页面却没有更新，问题可能是 `public` 文件夹下一些 `css` 、`js` 等文件没有实时更改

```html
# 首先使用以下命令可以让预览切换到 production 模式
hugo server -w -e production -DF
```

解决方法是可以手动删除 `public` 文件夹下除了 `.git` 文件夹以外的全部内容，然后再重新 `hugo` 生成文件夹，这样修改应该就生效了。

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

1. 首先在 [favicon generator](https://realfavicongenerator.net/) 里可以上传自己选择的图片（260*260左右），然后一路下一步，在这里下载package
2. 把package里的东西解压到`/themes/LoveIt/exampleSite/static/` （不同主题可能路径不同，我也是试了很多次，只要找到每个 `static` 不停地试就差不多），官方文档里只需要放在 `/static` 目录，不过我失败了，不知道是什么问题。至于底下这段代码，[Bright's Blog](https://ibrights.github.io/post/blog20210527/) 说可以复制到某个html文件里，但 `LoveIt` 不需要，如果用前面的步骤没有显示也可以试试
3. 最后 `Hugo Server -D` 察看有没有更改成功就好了

<a data-fancybox="gallery" href="/first_post/favicon.png"><img src="/first_post/favicon.png"></a>

#### admonition用法

一共12个样式，用起来很方便，这里用到了 `shortcodes` 的扩展

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

评论区的设置有很多选择，我尝试过 Gitalk、 [Valine]^(简洁高效的无后端评论系统)、Waline ，每个都出现了一些小问题，Valine 是评论区始终不显示，而且据说容易被匿名攻击；而 Waline 则是评论区始终加载，或许是渲染上的冲突，实在没找到修改办法。本来我是想做可以免注册或者只需要简易注册的评论系统，但问题太多。本意是考虑到 GitHub 可能并不是人人都有，没有办法，最后只好选择 GitHub 托管的评论插件 giscus，不过 giscus非常好用，基本十分钟设置完成。

1. 在 Github 上新建公开仓库，参考 [GitHub Discussions 快速入门](https://docs.github.com/cn/discussions/quickstart) ， Repository &rarr; Settings &rarr; Features &rarr; Set up discussions &rarr; Start a new discussion
2. 安装 [giscus](https://github.com/apps/giscus) 可以配置只选择存放评论的仓库，在 [giscus配置页面](https://giscus.app/zh-CN) 设置你的偏好，用来生成需要的代码，`仓库` 填写  `username/repository_name`  ， `页面discussion映射关系` 选择 `pathname` ，分类就是默认的 `announcements `  然后复制下面的代码，注意 `data-repo`  、`data-repo-id` 、 `data-category` 、 `data-category-id` 有没有自动生成
   1. 在根目录的 `/layouts/partials/` 新建 `comment.html` （其他主题有可能是 `comment` ，查看主题文档即可）把第二步生成的代码复制进去

3. 这样就设置完成了，用户只需要登陆 GitHub 账号就可以评论，评论的内容存储在创建的仓库里
4. 目前还有一个问题是主题切换时 giscus 不能自动更新

 #### 图片并排显示

Markdown 语法并不注重排版，所以图片设置中经常会出现各种令人难受的问题。如果想要让两三张图片并排显示的话，就需要用到 html 标签实现。

**单张居中**

```html
<center>
    <img src="http://dreamofbook.qiniudn.com/Zero.png">
</center>
```

固定宽度/高度，增加图注

```html
<img src="http://xxx.jpg" title="Logo" width="100" /> # height="1080" 
```

**并排居中显示**

```html
<center class="third">                      # class="half" 是两张并排
    <img src="http://xxx.jpg">
    <img src="http://yyy.jpg">
    <img src="http://zzz.jpg">
</center>
```

#### 图片放大功能

LoveIt内置了 Lightgallery 的设置，但是不知道是不是长期没有维护的原因（作者最近突然打算开始维护了！），即便在  `config.toml` 中打开 Lightgallery 也并不会打开图片放大功能。后来参考[Github Pages + Hugo 搭建个人博客](https://zz2summer.github.io/github-pages-hugo-%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/#%E5%85%AB%E7%BB%86%E8%8A%82%E4%BC%98%E5%8C%96) 大佬用 `jqury` 和 `fancybox` 实现了简单的图片放大效果。

1. 把主题中 `/themes/LoveIt/layouts/partials/footer.html` 复制到根目录下 `/layouts/partials/` 然后在最后加上：

   ```html
   <script src="https://cdn.jsdelivr.net/npm/jquery@3.4.1/dist/jquery.min.js"></script>
   
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/fancyapps/fancybox@3.5.7/dist/jquery.fancybox.min.css" />
   <script src="https://cdn.jsdelivr.net/gh/fancyapps/fancybox@3.5.7/dist/jquery.fancybox.min.js"></script>
   ```

2. 每次增加图片的时候修改一下代码，在插入图片的位置使用

   ```html
   <a data-fancybox="gallery" href="/pic_dir/picname.png"><img src="/pic_dir/picname.png"></a>
   ```


#### 访客统计功能

统计文章阅读次数用插件 busuanzi 就可以实现，[Hugo 网站访问计数插件不蒜子集成](https://xwi88.com/hugo-plugin-busuanzi/) 这个教程讲的很详细，有以下几个需要配置的地方。

1. 配置文件修改

   ```toml
    # xwi88 自定义配置 xwi88Cfg
   [params.xwi88Cfg]
     [params.xwi88Cfg.summary]
       update = true # summary 更新日期显示
     [params.xwi88Cfg.page]
       update = true # pages 更新日期显示
     [params.xwi88Cfg.busuanzi]
       enable = true
       # custom uv for the whole site
       site_uv = true
       site_uv_pre = '<i class="fa fa-user"></i>' # 字符或提示语
       site_uv_post = ''
       # custom pv for the whole site
       site_pv = true
       site_pv_pre = '<i class="fa fa-eye"></i>'
       # site_pv_post = '<i class="far fa-eye fa-fw"></i>'
       site_pv_post = ''
       # custom pv span for one page only
       page_pv = true
       page_pv_pre = '<i class="far fa-eye fa-fw"></i>'
       page_pv_post = ''
   
   ```

2. 在根目录 `/layouts/` 从主题文件复制对应文件到 `/layouts/_default/summary.html` , `/layouts/partials/footer.html` ， `/layouts/partials/plugin/busuanzi.html`（新建)，`/layouts/posts/single.html` 接下来逐一修改

3. 在 `/layouts/_default/summary.html` 文件中

   ```html
   # 基于原有的时间格式修改，首先删除原有日期显示
   #{{- with .Site.Params.dateFormat | default "2006-01-02" | .Lastmod.Format -}}
   #&nbsp;<span class="post-publish">
   	{{- printf `<time datetime="%v">%v</time>` . . | dict "Date" | T #"updatedOnDateLower" | safeHTML -}}
   #</span>
   #然后增加 xwi88 的配置
   {{- /* xwi88 config */ -}}
   {{- if .Site.Params.xwi88Cfg.summary.update -}}
   	{{- with .Site.Params.dateFormat | default "2006-01-02" | .Lastmod.Format -}}
   	&nbsp;<span class="post-publish">
   		{{- printf `<time datetime="%v">%v</time>` . . | dict "Date" | T "updatedOnDateLower" | safeHTML -}}
   	</span>
   		{{- end -}}
   	{{- end -}}
   ```

4.  在 `/layouts/partials/footer.html ` 文件中

   ```html
   #在代码块主题插入两行代码调用插件
   {{- /* busuanzi plugin */ -}}
   {{- partial "plugin/busuanzi.html" (dict "params" .Site.Params.xwi88Cfg.busuanzi "bsz_type" "footer") -}}
   ```

5. 在 `/layouts/partials/plugin/busuanzi.html` 文件中

   ```html
   {{ if .params.enable }}
       {{ if eq .bsz_type "footer" }}
           {{/* 只有 footer 才刷新，防止页面进行多次调用，计数重复; 只要启用就计数，显示与否看具体设置 */}}
           <script async src=" //busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js "></script>
       {{ end }}
   
       {{ if or (eq .params.site_pv true) (eq .params.site_uv true) (eq .params.page_pv true) }}
           {{ if eq .bsz_type "footer" }}
               <section>
                   {{ if eq .params.site_pv true }}
                       <span id="busuanzi_container_value_site_pv">
                           {{- with .params.page_pv_pre -}}
                               {{ . | safeHTML }}
                           {{ end }}
                           <span id="busuanzi_value_site_pv"></span>
                       </span>
                   {{ end }}
   
                   {{ if and (eq .params.site_pv true) (eq .params.site_uv true) }}
                       &nbsp;|&nbsp;              
                   {{ end }}
   
                   {{ if eq .params.site_uv true }}
                       <span id="busuanzi_container_value_site_uv">
                           {{- with .params.site_uv_pre -}}
                               {{ . | safeHTML }}
                           {{ end }}
                           <span id="busuanzi_value_site_uv"></span>
                       </span>
                   {{ end }}
               </section>
           {{ end }}
   
           {{/*  page pv 只在 page 显示  */}}
           {{ if and (eq .params.page_pv true) (eq .bsz_type "page-reading") }}
               <span id="busuanzi_container_value_page_pv">
                   {{- with .params.page_pv_pre -}}
                       {{ . | safeHTML }}
                   {{ end }}
                   <span id="busuanzi_value_page_pv"></span>&nbsp;
                   {{- T "views" -}}
               </span>
           {{ end }}
       {{ end }}
   {{ end }}
   
   ```

   

6. 在 `/layouts/posts/single.html` 文件中

   ```html
   # 类似第三步，先删除这两行
   # {{- with .Site.Params.dateformat | default "2006-01-02" | .Lastmod.Format -}}
   # <i class="far fa-calendar-check fa-fw"></i>&nbsp;<time datetime="{{ . }}">{{ . }}</time>&nbsp;
   # 然后复制以下内容
   {{- /* xwi88 config */ -}}
   {{- if .Site.Params.xwi88Cfg.page.update -}}
   	{{- with .Site.Params.dateformat | default "2006-01-02" | .Lastmod.Format -}}
   	<i class="far fa-calendar-check fa-fw"></i>&nbsp;<time datetime="{{ . }}">{{ . }}</time>&nbsp;
   	{{- end -}}
   {{- end -}}
   
   # 此后两行后，增加
   {{- /* busuanzi plugin */ -}}
   {{- partial "plugin/busuanzi.html" (dict "params" .Site.Params.xwi88Cfg.busuanzi "bsz_type" "page-reading") -}}
   ```


#### 插入 Shields 徽章

<img src="https://img.shields.io/badge/这就是-Shields徽章-blue?style=flat-square" >

Shields 徽章可以用来显示文章有关的一些信息（主要是看起来很好看），可以直接用 [Shields.io官网](https://shields.io/) 来设置自定义内容，之后用 markdown 语法或者 html 标签放入文章之中即可

```html
<a href="https://link-to-a-site.net"><img src="https://img.shields.io/badge/[left info]-[right info]-[color]?style=flat&logo=WeChat" >
```

可以直接修改 URL 来实现自己想要的内容和颜色，前面还可以加入链接

`color` 可以从<img src="https://img.shields.io/badge/brightgreen-brightgreen" > <img src="https://img.shields.io/badge/green-green" > <img src="https://img.shields.io/badge/yellow-yellow" > <img src="https://img.shields.io/badge/yellowgreen-yellowgreen" > <img src="https://img.shields.io/badge/orange-orange" > <img src="https://img.shields.io/badge/red-red" > <img src="https://img.shields.io/badge/blue-blue" > <img src="https://img.shields.io/badge/lightgrey-lightgrey" > <img src="https://img.shields.io/badge/blueviolet -blueviolet " > <img src="https://img.shields.io/badge/ff69b4-ff69b4" > 等十六进制颜色编码中选择

`style` 默认是 <img src="https://img.shields.io/badge/style-flat-brightgreen?style=flat" > ，其他可设置的风格包括<img src="https://img.shields.io/badge/style-flat square-brightgreen?style=flat-square" > <img src="https://img.shields.io/badge/style-plastic-brightgreen?style=plastic" > <img src="https://img.shields.io/badge/style-social-brightgreen?style=social" > <img src="https://img.shields.io/badge/style-for--the--badge-brightgreen?style=for-the-badge" >

`logo`  参考 [Simple Icons](https://simpleicons.org/) 的 logo 选择

动态小牌子的设置方法可以参考 [用 Substats 和 Shields.io 为你的个人主页定制动态数据小牌子](https://sspai.com/post/59593) 

#### 添加音乐

作者已经给出了用 Shortcode 实现音乐插入的教程 [主题文档 - music Shortcode](https://hugoloveit.com/zh-cn/theme-documentation-music-shortcode/) 基本很清楚

```html
# 如果想要插入本地文档，这里注意第一点是和图片一样放在 static 目录下，第二点是文件名最好是英文
{{ < music url="/music/music.mp3" name=music_name artist=author cover="/images/cover.jpg" > }}
# 如果插入流媒体外链的话
{{ < music auto="https://music.163.com/#/playlist?id=60198" >}}
# 自定义的方式还有
{{ < music server="netease" type="song" id="60198" >}}
其中 server = [netease, tencent, kugou, baidu], type = [song, playlist, album, search, artist]
```

这里插播一个小技巧，我有很多抓取的 `flac`  格式的音乐文件，但是文件太大，不太利于上传，所以使用

```markdown
ffmpeg -i music.flac music.mp3
```

就可以轻松转换格式。 PS：[给新手的 20 多个 FFmpeg 命令示例](https://zhuanlan.zhihu.com/p/67878761)



此外可定义的还有很多，包括 `theme `  = `#448aff` ,  `fixed `  = `false` ,  `mini `  = `false` ,  `autoplay`  = `false`,  `volume`  = `0.7`,  `mutex`  = `true` (是否自动暂停其他播放器)
如果是列表的话，还有参数  `loop`  = `all, one, none[default]`,  `order`  = `list(default), random`,  `list-folded`  = `false`,  `list-max-height`  = `340px(default)`

#### 隐藏文章

有的时候有一些把写好的文章隐藏的需求，我通过具体的 URL 可以分享给特定的人，但是这样的文章在首页是看不到的。有一些解决方案用到了加密的方法，目前来讲，还没有加密的必要。简单来说，只需要让主页面渲染时不去渲染特定页面就可以了。参考 [Creating Unlisted Content in Hugo](https://bphogan.com/2020/08/11/2020-08-11-creating-unlisted-content-in-hugo/)

1. 对需要隐藏的文章，在 Markdown 文件前增加 `unlisted: true`

2. 修改 `/layouts/_default/section.html` 

   ```html
   {{- /* Paginate */ -}}
   {{- if .Pages -}}
   	{{- $pages := .Pages.GroupByDate "2006" -}}
   	{{- with .Site.Params.section.paginate | default .Site.Params.paginate -}}
   		{{- $pages = $.Paginate $pages . -}}
   	{{- else -}}
   		{{- $pages = .Paginate $pages -}}
   	{{- end -}}
   	{{- range $pages.PageGroups -}}
   		<h3 class="group-title">{{ .Key }}</h3>
   		# 删掉 {{- range .Pages -}} ，改为下一句
   		{{- range (where .Pages ".Params.unlisted" "!=" "true") -}}
   			<article class="archive-item">
      				 <a href="{{ .RelPermalink }}" class="archive-item-link">
                       {{- .Title | emojify -}}
                   </a>
                   <span class="archive-item-date">
                       {{- $.Site.Params.section.dateFormat | default "01-02" | .Date.Format -}}
                   </span>
               </article>		
   		{{- end -}}
   ```

   

### 查阅文档

* [Markdown基本语法](https://www.markdown.xyz/basic-syntax/) 和[Markdown速查表](https://www.markdown.xyz/cheat-sheet/)
* [LoveIt主题作者的博客](https://hugoloveit.com/zh-cn) 以及两篇基本文档[基本概念](https://hugoloveit.com/zh-cn/theme-documentation-basics/) [内容](https://hugoloveit.com/zh-cn/theme-documentation-content/) (内有一些特殊的扩展语法)
* [中文文案排版指北](https://github.com/sparanoid/chinese-copywriting-guidelines) 

### Reference

* [Github Pages + Hugo 搭建个人博客](https://zz2summer.github.io/github-pages-hugo-%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/#%E5%85%AB%E7%BB%86%E8%8A%82%E4%BC%98%E5%8C%96) 搭建教程
* [用Git Pages加Hugo搭建个人博客全记录](https://z24z.com/post/2021/github-pages-for-blog/) 讲了域名的流程以及切换到 `docs` 的好处，之后再看
* [如何利用 GitHub Pages 和 Hugo 轻松搭建个人博客？](https://zhuanlan.zhihu.com/p/57361697) 评论值得一看，可能会有一些问题的解答
* [Hugo - 10分钟搭建 & 部署个人网站/博客，简历中的博客网站怎么建](https://www.bilibili.com/video/BV1x64y117PX?spm_id_from=333.337.search-card.all.click) 视频
* [Hugo静态网站生成器中文教程](http://nanshu.wang/post/2015-01-31/) 主题不同，也有一些新的功能指南
* [Hugo系列(3.2) - LoveIt主题美化与博客功能增强 · 第三章](https://lewky.cn/posts/hugo-3.2.html/) 超长文，值得研究
* [Hugo+Loveit优化记](https://www.bahuangshanren.tech/2021-2/) 优化 Hugo + LoveIt
* [风月的博客，Hugo的教程，也很长](https://kuang.netlify.app/blog/hugo.html)
* [Hugo框架中文文档 短代码](https://www.andbible.com/post/hugo-content-management-shortcodes/)
* [给Hugo个人博客添加Valine评论系统](https://shenshilei1022.gitee.io/post/e277/)
* [Hugo搭建博客（一）— 基本设置](https://cloud.tencent.com/developer/article/1722255)
* [[转] 使用Waline搭建博客评论系统](https://blog.h1msk.cc/2021/09/25/%E4%BD%BF%E7%94%A8Waline%E6%90%AD%E5%BB%BA%E5%8D%9A%E5%AE%A2%E8%AF%84%E8%AE%BA%E7%B3%BB%E7%BB%9F/) 写了很详细的 `vercel` 配置指南
* [Hugo系列(3.1) - LoveIt主题美化与博客功能增强 · 第二章](https://lewky.cn/posts/hugo-3.1.html/) Waline 替代 Valine 的评论系统
* [博客评论系统从 Utterances 迁移到 Giscus](https://www.dejavu.moe/posts/utterances-to-giscus/#fnref:3)
* [迁移博客评论系统从Utteranc.es到Giscus](https://agou-ops.cn/myBlog-2/post/%E8%BF%81%E7%A7%BB%E5%8D%9A%E5%AE%A2%E8%AF%84%E8%AE%BA%E7%B3%BB%E7%BB%9F%E5%88%B0giscus/)
* [Hugo Plugin Giscus Support](https://xwi88.com/hugo-plugin-giscus-support/)
* [手把手教你如何用Hugo构建个人静态博客(六)](https://zhuyinjun.me/2020/how-to-setup-blog-by-hugo-6/#%E6%B7%BB%E5%8A%A0%E8%AF%84%E8%AE%BA%E7%B3%BB%E7%BB%9F-giscus) 另一种方法引入 giscus
* [Hugo的文件配置和博客功能增强(一)](https://www.yexxweb.com/hugo_conf/) 修改 `_custom.scss` 的方法美化 LoveIt
* [博客搭建过程（二）](https://www.cuichacha.site/process-of-building-the-blog-2.html/) 
* [使用 Hugo 和 GitHub Pages 搭建并部署一个静态博客网站](https://blog.csdn.net/weixin_43958105/article/details/123316879) 写了 PaperMod 下 giscus 怎样实现主题自动切换
* [Markdown 简明语法参考](http://whuhan2013.github.io/blog/2015/09/19/markdown-simple-grammar/) 以后放不下图片可以参考图床的使用
* [Hugo 网站访问计数插件不蒜子集成](https://xwi88.com/hugo-plugin-busuanzi/)
* [使用Hugo框架搭建博客的过程 - 主题配置](https://www.xiaodejiyi.com/2021/01/build-blog-theme-config/)
* [构建自己的博客系统](https://www.whexy.com/posts/blog-diy) 设立一个终极目标吧！未来自己构建博客系统！

### 总结

* 就目前来看，博客是具有实用性的，但市面少有好用的产品，或者是古旧的新浪博客，或者就是这种需要一定代码的方式，但后者对于非技术专业的新手来说还是有些复杂。以我为例，修改 config 和 html 文件还算颤颤巍巍能搞得来，但 giscus 要修改 json 和 css 的时候是真的懵逼了。
* 在博客的书写中要注意兼顾Markdown语法和书写规范，即便是个人博客，也不要增加阅读上的困难，例如明确区分中英文混杂的写作规则，避免使用错误的缩略语，避免使用流行语，避免自我审查。
* 之后需要搞定切换主题和设置第二个库的方法，或许可以拿来做作品集网站。
*  `Hugo server` 默认环境是 `development` , 而 `Hugo` 的默认环境是 `production` ，值得注意。


