# Shortcode的几点应用


<!--more-->

<p><img src="https://img.shields.io/badge/last%20modified-2025--5--24-ff69b4?style=flat" > <img src="https://img.shields.io/badge/Words-300-yellow?style=flat" >  <img src="https://img.shields.io/badge/1%20minutes-lightgray?style=flat" ></p>

最近发现shortcode很好用，能比较好减轻我的博客编辑负担，chatGPT的帮助下添加了图片的shortcode工具

# test 测试

## 单张图片

添加时间：2025/5/24

### 示例代码

``` 
{{</* imgbox src="图片链接" width="800" title="图片标题" source="图片来源" */>}} 
``` 


### 教程

#### 需求 

| 参数        | 是否必填     |默认值|说明|
|-------------|----------|----|-----|
| src       | ✅    |无|图片链接|
| width        | ❌     |100%|图片宽度（如 800，单位像素）|
| title        | ❌     |无|图片下方标题文本|
| source        | ❌     |无|图片下方来源或说明文本|


在 layouts/shortcodes/ 文件夹下创建 imgbox.html

```
your-site/
├── layouts/
│   └── shortcodes/
│       └── imgbox.html
```

写入以下 Shortcode 模板内容：

```html
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
```

#### 示例效果
``` 
{{</* imgbox src="图片链接" width="800" title="图片标题" source="图片来源" */>}} 
``` 

博客页面上就会自动渲染为：居中大图（800px 或默认填满）；支持 Fancybox 点击放大；下方自动带有可选的标题与来源信息；不需要手写 HTML，每次都能省很多时间。

另外，把 Picgo的设置中自定义链接的格式改为 `{{</* imgbox src="$url" width="800" title="" source="" */>}}`，就可以实现picgo自动复制链接到剪贴板。

> 和以前picgo的代码 `<center><a data-fancybox="gallery" href="$url"><img src="$url" width="1000"></a> <style> p.title {line-height:100%; font-size:15px; color:black; font-weight:bold;} p.source {line-height:100%; font-size:13px; color:gray;} </style> <p class="title"> this is title </p> <p class="source"> this is source </p> </center>` 对比还是有巨大收益的

## 多栏排版

除此之外，我还想实现多栏排版的功能


### 示例代码

#### 3张图片并排

```
{{</* multicol layout="2fr 2fr 2fr" */>}}
{{</* colbox
  type="image"
  src="/images/avocado128.png"
  title="图一标题"
  source="图一来源"
  desc="图一描述"
  height="150"
*/>}}
这里是图一的说明，可以使用 **加粗** 或 [链接](#)。
{{</* /colbox */>}}
{{</* colbox
  type="image"
  src="/images/avocado128.png"
  title="图二标题"
  source="图二来源"
  desc="图二描述"
  height="150"
*/>}}
这里是图二说明。
{{</* /colbox */>}}
{{</* colbox
  type="image"
  src="/images/avocado128.png"
  title="图三标题"
  source="图三来源"
  desc="图三描述"
  height="150"
*/>}}
图三内容描述。
{{</* /colbox */>}}
{{</* /multicol */>}}

```

示例

{{< multicol layout="2fr 2fr 2fr" >}}
{{< colbox
  type="image"
  src="/images/avocado128.png"
  title="图一标题"
  source="图一来源"
  desc="图一描述"
  height="150"
>}}
这里是图一的说明，可以使用 **加粗** 或 [链接](#)。
{{< /colbox >}}
{{< colbox
  type="image"
  src="/images/avocado128.png"
  title="图二标题"
  source="图二来源"
  desc="图二描述"
  height="150"
>}}
这里是图二说明。
{{< /colbox >}}
{{< colbox
  type="image"
  src="/images/avocado128.png"
  title="图三标题"
  source="图三来源"
  desc="图三描述"
  height="150"
>}}
图三内容描述。
{{< /colbox >}}
{{< /multicol >}}


#### 2张图片并排

```
{{</* multicol layout="2fr 2fr" */>}}
{{</* colbox
  type="image"
  src="/images/avocado128.png"
  title="图一标题"
  source="图一来源"
  desc="图一描述"
  height="150"
*/>}}
这里是图一的说明，可以使用 **加粗** 或 [链接](#)。
{{</* /colbox */>}}
{{</* colbox
  type="image"
  src="/images/avocado128.png"
  title="图二标题"
  source="图二来源"
  desc="图二描述"
  height="150"
*/>}}
这里是图二说明。
{{</* /colbox */>}}
{{</* /multicol */>}}

```

示例

{{< multicol layout="2fr 2fr" >}}
{{< colbox
  type="image"
  src="/images/avocado128.png"
  title="图一标题"
  source="图一来源"
  desc="图一描述"
  height="150"
>}}
这里是图一的说明，可以使用 **加粗** 或 [链接](#)。
{{< /colbox >}}
{{< colbox
  type="image"
  src="/images/avocado128.png"
  title="图二标题"
  source="图二来源"
  desc="图二描述"
  height="150"
>}}
这里是图二说明。
{{< /colbox >}}
{{< /multicol >}}




#### 左图右文并排

```
{{</* multicol layout="2fr 2fr" */>}}
{{</* colbox
  type="image"
  src="/images/avocado128.png"
  title="图一标题"
  source="图一来源"
  desc="图一描述"
  height="150"
*/>}}

{{</* /colbox */>}}
{{</* colbox
  type="text"
  title="标题"
  source="来源"
  desc="描述"
*/>}}
这里是文字说明。
{{</* /colbox */>}}

{{</* /multicol */>}}

```

示例

{{< multicol layout="2fr 2fr" >}}
{{< colbox
  type="image"
  src="/images/avocado128.png"
  title="图一标题"
  source="图一来源"
  desc="图一描述"
  height="150"
>}}

{{< /colbox >}}
{{< colbox
  type="text"
  title="标题"
  source="来源"
  desc="描述"
>}}
这里是文字说明。
{{< /colbox >}}

{{< /multicol >}}


### 教程

#### 需求

支持2栏、3栏甚至更多的显示，每栏宽度可自定义

支持文字或图片

将这两个文件分别放在你的 Hugo 项目路径：

```
your-hugo-site/
└── layouts/
    └── shortcodes/
        ├── multicol.html
        └── colbox.html
```

#### ✅ 文件一：multicol.html（多栏容器）

```html
{{ $layout := .Get "layout" | default "1fr 1fr 1fr" }}
<div style="
  display: grid;
  grid-template-columns: {{ $layout }};
  gap: 10px;
  max-width: 800px;
  margin: 2em auto;
  align-items: flex-start;
">
  {{ .Inner }}
</div>
```


✅ 支持参数：
columns：通过修改每栏的数量和相对宽度，可以调节栏数以及宽度

#### ✅ 文件二：colbox.html（每栏内容模块）

```html

<div style="text-align: left; word-break: break-word;">
    {{ if eq (.Get "type") "image" }}
      {{ if .Get "src" }}
        <a data-fancybox="gallery" href="{{ .Get "src" }}">
            <img src="{{ .Get "src" }}"
            style="height: {{ with .Get "height" }}{{ . }}px{{ else }}200px{{ end }};
                   width: auto;
                   display: block;
                   margin: 0 auto 0.5em auto;
                   border-radius: 6px;">
       
        </a>
      {{ end }}
    {{ end }}
  
    {{ if .Get "title" }}
      <p style="font-size: 15px; font-weight: bold; margin: 0.2em 0;">{{ .Get "title" }}</p>
    {{ end }}
  
    {{ if .Get "source" }}
      <p style="font-size: 13px; color: gray; margin: 0;">{{ .Get "source" }}</p>
    {{ end }}
  
    {{ if .Get "desc" }}
      <p style="font-size: 14px; line-height: 1.6; margin-top: 0.5em;">{{ .Get "desc" }}</p>
    {{ end }}
  
    {{ if .Inner }}
      <div style="font-size: 14px; line-height: 1.6; margin-top: 0.5em;">
        {{ .Inner | markdownify }}
      </div>
    {{ end }}
  </div>
  
```

#### 效果特点：

图片自动填满每栏宽度，保持等比缩放

分栏数自定义，自动均分宽度

每栏支持标题、来源和自由描述

图片可 Fancybox 放大（需启用 params.fancybox = true）

{{< multicol layout="2fr 2fr 2fr" >}}
{{< colbox
  type="image"
  src="/images/avocado128.png"
  title="图一标题"
  source="图一来源"
  desc="图一描述"
  height="150"
>}}
这里是图一的说明，可以使用 **加粗** 或 [链接](#)。
{{< /colbox >}}
{{< colbox
  type="image"
  src="/images/avocado128.png"
  title="图二标题"
  source="图二来源"
  desc="图二描述"
  height="150"
>}}
这里是图二说明。
{{< /colbox >}}
{{< colbox
  type="image"
  src="/images/avocado128.png"
  title="图三标题"
  source="图三来源"
  desc="图三描述"
  height="150"
>}}
图三内容描述。
{{< /colbox >}}
{{< /multicol >}}

## 弹出框

{{< admonition note "See you later" false >}}

持续更新..

{{< /admonition >}}


