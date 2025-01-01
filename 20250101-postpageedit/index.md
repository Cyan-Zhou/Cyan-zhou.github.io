# 博客目录页面优化记录


<!--more-->

<p><img src="https://img.shields.io/badge/last%20modified-2025--1--1-ff69b4?style=flat" > <img src="https://img.shields.io/badge/Words-403-yellow?style=flat" >  <img src="https://img.shields.io/badge/02%20minutes-lightgray?style=flat" ></p>

趁新年假期，在GPT的协助下修改博客目录页面长期存在的bug。

2年前配置博客的时候，当时在网页查询各种教程的辅助下，胡乱调整代码，把目录页按照自己想要的风格做了一些代码上的修改（具体修改处已经记不清了），但是一直存在很多bug。

<center><a data-fancybox="gallery" href="https://images-1319077775.cos.ap-guangzhou.myqcloud.com/2025/01/01-18_20_01-202501011820231_dcf.png"><img src="https://images-1319077775.cos.ap-guangzhou.myqcloud.com/2025/01/01-18_20_01-202501011820231_dcf.png" width="1000"></a> <style> p.title {line-height:100%; font-size:15px; color:black; font-weight:bold;} p.source {line-height:100%; font-size:13px; color:gray;} </style> <p class="title"> 这就是之前的界面，很明显排版上有很多问题 </p> <p class="source">  </p> </center>

一直想系统学习前端知识，搞明白整个博客的架构，然后再做更好的修改。但是一方面没有时间，另一方面系统学习对个人的时间和精力要求太高，目的仅仅是博客管理的情况下，确实难度太高。现在有了GPT的协助，我可以让GPT告诉我博客里某个文件的功能是什么，它的代码应该怎么理解，很大程度上减轻了学习的负担，而且目的性更强。在和GPT的讨论下，我完成了界面的优化修改。

<center><a data-fancybox="gallery" href="https://images-1319077775.cos.ap-guangzhou.myqcloud.com/2025/01/01-23_09_01-202501012309006_cab.png"><img src="https://images-1319077775.cos.ap-guangzhou.myqcloud.com/2025/01/01-23_09_01-202501012309006_cab.png" width="1000"></a> <style> p.title {line-height:100%; font-size:15px; color:black; font-weight:bold;} p.source {line-height:100%; font-size:13px; color:gray;} </style> <p class="title"> 我和GPT的沟通 </p> <p class="source"> GPT-4o </p> </center>


<center><a data-fancybox="gallery" href="https://images-1319077775.cos.ap-guangzhou.myqcloud.com/2025/01/01-22_32_01-202501012232000_75f.png"><img src="https://images-1319077775.cos.ap-guangzhou.myqcloud.com/2025/01/01-22_32_01-202501012232000_75f.png" width="1000"></a> <style> p.title {line-height:100%; font-size:15px; color:black; font-weight:bold;} p.source {line-height:100%; font-size:13px; color:gray;} </style> <p class="title"> 修改后的结果 </p> <p class="source"> </p> </center>

具体来说，一共需要修改3个文件

### 文件1：创建flexbox.css

在 /assets 文件夹中新建一个css文件 flexbox.css

``` css

/* Flexbox 样式：标题左对齐，换行，日期右对齐 */
.archive-item {
    display: flex;
    justify-content: space-between; /* 水平两端对齐 */
    align-items: flex-start !important; /* 子元素顶部对齐 */
    gap: 10px; /* 标题和日期之间的间距 */
    margin-bottom: 15px; /* 不同标题之间的间距 */
}

.archive-item-link {
    flex: 1;/* 标题占据剩余空间 */
    word-break: break-word; /* 长单词换行 */
    text-align: left; /* 确保标题左对齐 */
    white-space: normal; /* 标题允许换行 */
    line-height: 1.2; /* 设置行高，适当紧凑 */
    margin-right: 10px; /* 与日期保持间距 */
    overflow: visible; /* 移除溢出隐藏 */
    text-overflow: clip; /* 不使用省略号 */

}

.archive-item-date {
    flex-shrink: 0; /* 防止日期被压缩 */
    text-align: left; /* 在有限范围内左对齐 */
    min-width: 40px; /* 固定宽度 */
    margin-left: 10px; /* 日期与标题之间保持一定距离 */
    align-self: flex-start; /* 让日期单独顶部对齐 */
    font-feature-settings: "tnum"; /* 确保字体支持等宽数字 */

}

/* 移动端适配 */
@media (max-width: 768px) {
    .archive-item {
        flex-direction: column; /* 垂直布局 */
        align-items: flex-start; /* 子元素左对齐 */
    }
    .archive-item-date {
        text-align: left; /* 日期左对齐 */
        margin-top: 10px; /* 增加标题和日期的垂直间距 */
        align-self: flex-start; /* 确保在小屏幕上仍然顶部对齐 */
    }
}

```

css文件是为了更好统一管理渲染的样式，通过这个文件，定义每个模块的显示效果

* `.archive-item` 文章整体页面的格式

* `.archive-item-link` 文章链接的格式

* `.archive-item-date` 日期部分的格式

* `@media` 移动端的配置

1. PC端
``` plaintext
+----------------------------------------+
|  标题标题标题标题标题标题标题标题标题  |
|                                  日期  |
+----------------------------------------+

```

2. 移动端

``` plaintext
+----------------------------------------+
|  标题标题标题标题标题标题标题标题标题  |
|  日期                                   |
+----------------------------------------+

```

### 文件2: 修改 link.html

在/layouts/partials/head/link.html 文件中需要增加以下的代码，用于把`flexbox.css` 添加到整个文档系统中

``` html
{{- /* flexbox.CSS */ -}}
{{- $customCSS := resources.Get "css/flexbox.css" | resources.Minify | resources.Fingerprint }}
{{- partial "plugin/style.html" (dict "Source" $customCSS.Permalink "Fingerprint" $fingerprint "Preload" false) -}}


```

`resources.Get`：加载 scss/theme.scss 文件。

`resources.ToCSS`：将 SCSS 文件编译为 CSS。

`resources.Minify`：压缩 CSS 文件。

`resources.Fingerprint`：为文件生成指纹（版本号）。


在 Hugo 框架中，`layouts/partials/head/link.html` 通常负责管理网站的 `<head>` 部分，包括样式表（CSS）的加载、外部资源的引入以及其他元数据设置。

#### head 部分的作用
`<head>` 是 HTML 页面结构的一部分：
它位于 `<html>` 标签内，用来定义页面的元信息和加载资源。
`<head> `的内容在页面加载时会被浏览器优先处理。
主要功能：
定义页面标题（`<title>`）。
加载样式表（`<link>`）。
引入脚本文件（`<script>`）。
设置元数据（`<meta>`），如描述、关键字、视口设置等。

#### 为什么单独用一个文件来管理样式表？

模块化设计，Hugo 模板文件通过 partials 将功能拆分成独立的模块（如 link.html 专管样式表）。这样便于维护和扩展，避免所有代码堆积在一个大文件中。

复用性，link.html 可以在整个站点中被多个页面调用，例如首页、文章列表页、单篇文章页等。通过修改一个文件即可全局更新样式表加载逻辑。

动态加载，link.html 可以结合 Hugo Pipes 动态加载和处理 CSS 文件，例如：

* 压缩 CSS 文件。

* 生成唯一指纹（版本号），防止缓存问题。

* 按需加载不同的样式文件。


