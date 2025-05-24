# 20250524 Shortcodeplayground


<!--more-->

## 单张图片

1. 在 layouts/shortcodes/ 文件夹下创建 imgbox.html
路径大概是：

复制
编辑
your-site/
├── layouts/
│   └── shortcodes/
│       └── imgbox.html
2. 写入以下 Shortcode 模板内容：
html
复制
编辑
<center>
  <a data-fancybox="gallery" href="{{ .Get "src" }}">
    <img src="{{ .Get "src" }}" 
         {{ with .Get "width" }}width="{{ . }}"{{ else }}style="width: 100%;"{{ end }} />
  </a>

  {{ if or (.Get "title") (.Get "source") }}
    <style>
      p.title {
        line-height: 100%;
        font-size: 15px;
        color: black;
        font-weight: bold;
        margin: 0.5em 0 0 0;
      }
      p.source {
        line-height: 100%;
        font-size: 13px;
        color: gray;
        margin: 0;
      }
    </style>
    {{ with .Get "title" }}<p class="title">{{ . }}</p>{{ end }}
    {{ with .Get "source" }}<p class="source">{{ . }}</p>{{ end }}
  {{ end }}
</center>
✅ 使用说明
参数	是否必填	默认值	说明
src	✅	无	图片链接
width	❌	100%	图片宽度（如 800，单位像素）
title	❌	无	图片下方标题文本
source	❌	无	图片下方来源或说明文本

✅ 示例效果预期
你在文章中写：

markdown
复制
编辑
{{< imgbox src="图片链接" width="800" title="长安街夜景" source="摄影：张三" >}}
博客页面上就会自动渲染为：

居中大图（800px 或默认填满）；

支持 Fancybox 点击放大；

下方自动带有可选的标题与来源信息；

不需要手写 HTML，每次都能省很多时间。


## 多栏排版
路径
将这两个文件分别放在你的 Hugo 项目路径：

markdown
复制
编辑
your-hugo-site/
└── layouts/
    └── shortcodes/
        ├── multicol.html
        └── colbox.html
✅ 文件一：multicol.html（多栏容器）
html
复制
编辑
<div style="
  display: grid;
  grid-template-columns: repeat({{ .Get "columns" | default "3" }}, 1fr);
  gap: 20px;
  max-width: 1000px;
  margin: 2em auto;
">
  {{ .Inner }}
</div>
✅ 支持参数：
columns：你想要的列数，比如 2、3、4，默认是 3

✅ 文件二：colbox.html（每栏内容模块）
html
复制
编辑
<div style="text-align: center;">
  {{ if .Get "src" }}
    <a data-fancybox="gallery" href="{{ .Get "src" }}">
      <img src="{{ .Get "src" }}" style="width: 100%; height: auto; border-radius: 8px; margin-bottom: 0.5em;">
    </a>
  {{ end }}

  {{ if .Get "title" }}
    <p style="font-size: 15px; font-weight: bold; margin: 0.2em 0;">{{ .Get "title" }}</p>
  {{ end }}

  {{ if .Get "source" }}
    <p style="font-size: 13px; color: gray; margin: 0;">{{ .Get "source" }}</p>
  {{ end }}

  <div style="font-size: 14px; text-align: left; line-height: 1.6; margin-top: 0.5em;">
    {{ .Inner | markdownify }}
  </div>
</div>
✅ 支持参数：
src：图片链接（可点击放大）

title：标题

source：来源说明

内容区域：支持 markdown 格式的描述文字




✅ 效果特点：
图片自动填满每栏宽度，保持等比缩放

分栏数自定义，自动均分宽度

每栏支持标题、来源和自由描述

图片可 Fancybox 放大（需启用 params.fancybox = true）

{{< multicol columns="3" >}}

{{< colbox
  src="https://example.com/pic1.jpg"
  title="图一标题"
  source="图一来源"
>}}
这里是图一的说明，可以使用 **加粗** 或 [链接](#)。
{{< /colbox >}}

{{< colbox
  src="https://example.com/pic2.jpg"
  title="图二标题"
  source="图二来源"
>}}
这里是图二说明。
{{< /colbox >}}

{{< colbox
  src="https://example.com/pic3.jpg"
  title="图三标题"
  source="图三来源"
>}}
图三内容描述。
{{< /colbox >}}

{{< /multicol >}}



{{< admonition note "See you later" false >}}

持续更新..

{{< /admonition >}}

