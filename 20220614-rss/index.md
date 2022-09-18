# 用RSS回到开放的互联网


<!--more-->

<p><img src="https://img.shields.io/badge/last%20modified-2022--8--28-ff69b4?style=flat" > <img src="https://img.shields.io/badge/Words-5048-yellow?style=flat" >  <img src="https://img.shields.io/badge/13%20minutes-lightgray?style=flat" ></p>

<p><img src="https://img.shields.io/badge/Status-updating-blue?style=flat" ></p>

## 为什么 RSS?

我经常会在失眠的夜晚，刷着小红书，瞪着眼睛体验大数据为我们精心策划的人生。我们好像一下子就习惯了很容易看到喜欢的内容的生活，久而久之，我都快忘记了小时候站在报刊亭前，面对着琳琅满目我从没听说过的杂志们的兴奋感。因为在哥哥家里看到《看电影》的杂志，我开始一发不可收拾地爱上看电影；因为在初中的书店偶然买到一本《Hobby Japan》，我得以一窥模型的隐秘世界，或许这也是我对会做模型的建筑系产生向往的原因之一。当然，我明白现在要接触到这些信息比那个时候要容易太多，你总可以找到无论多么冷门的电影资源，大佬们制作的做模型的视频也比比皆是。然而，什么能比得上我站在杂志店的那个充满期待和惊喜的瞬间呢？

回到正题，你们有没有发现小红书的推荐非常好训练？我经常故意折腾这个明目张胆的推荐算法。只要故意表现出对某个关键词的兴趣——比如多次打开巴哥的视频，或者常看看劝转行的流泪经验帖，小红书左上角的第一个推荐就会是同样的话题。这是在去年计划去重庆时，我从 gyw 的小红书上发现的——他的第一个推荐永远都是妹妹（他说他成长了，现在不是了）。另一个特别好训练的是 YouTube 的推荐算法，有时候，我甚至觉得我的兴趣都被它控制了，偶然看完的拆鱼的视频会让主页上 [1]/[3] 的超链接都是东亚海鲜市场现场拆鱼讲解。在这些我们熟悉并且喜爱的事情上，太容易耗费太多的时间，毕竟，大脑的本能的偏好占据了很重要的决策优先级。

## 什么是 RSS?

RSS 全称是 `Really Simple Syndication` ，是一种简单易用的为用户提供信息聚合方式的格式规范。通过将想获取信息的网站的 RSS 源载入到客户端中，用户就可以在不打开网站的前提下，用阅读模式浏览文章推送，在牺牲了一些网站精美设计的同时，也让用户可以更加专注在内容上。另外，这让我们夺回了对信息源的主动权。

在搭建博客的过程中，我逐渐了解了一下 RSS 在电脑上的用法。很久之前在 `Kindle` 上用过（时代的眼泪），不过也没有坚持下来，主要是当时的信息来源也很单一，无非是知乎、豆瓣这些本身信息量就过载了的平台。而现在收集了很多 blog 以及网站之后，如何紧跟每个页面的更新，就成为一个相当有必要的内容。

除了一些日常更新的网站之外，newsletter 也是非常常见的信息源，而且与 RSS 相比，newsletter 更常见一些，很多资讯网站没有 RSS 或者缺少维护，但依旧会提供 每日/每周/每月的 newsletter 订阅服务。之前，我会在邮箱客户端将一些日常使用的信源划入 newsletter 的群组，但依旧在添加新的订阅和一段时间忘记查看——谁会没有经历过一周疏于管理邮箱的恐惧呢——方面尤其不够方便。好在现在 newsletter 也可以迁移到 RSS 上来。

国内平台上的讯息尤其难以订阅，例如微信公众号。尽管我相当不喜欢公众号（大量的垃圾信息，难以管理分组，以及让人感动的提醒机制），不过还是有一些优质的作者把公众号作为主要的内容平台。微信公众号有着十分强大的反爬机制，这当然是国内各大厂商日渐高企的信息壁垒下建立自己的内容闭环生态圈所必须设置的自我保护的障碍，这也导致微信公众号转为 RSS 源困难极高，而且现在可行的方法，不久的未来可能就会失效。目前有替代性的方法可以实现简单的 RSS 提醒，先记录在这里（2022-07-19）。

## Get Started

对使用者来说，RSS 的使用流程大致是这样的：

{{< mermaid >}}
graph LR;
    A(订阅网站) -->|按文档要求传递 ID| B(制作订阅源)
    B -->|传递订阅源| C(RSS客户端)
    C --> D(阅读)
{{< /mermaid >}}

为了避免 RSSHub 因为使用人数过多导致的过载和延迟问题，我们使用 [Heroku](https://dashboard.heroku.com/) 来免费搭建自己的 RSSHub 的服务器

1. 注册 Heroku 账号并完成激活
2. 跳转到 [RSSHub 模板](https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2FDIYgod%2FRSSHub) 页面，设置部署 RSSHub 的服务器，`Appname` 填写你的服务器的名称，直接部署。看到下面 Deploy to Heroku 打勾以后就说明部署成功，这时点击 `view`
   <a data-fancybox="gallery" href="/20220614-rss/image-20220615000900957.png"><img src="/20220614-rss/image-20220615000900957.png" ></a>
3. 安装 [RSSHub Radar](https://chrome.google.com/webstore/detail/rsshub-radar/kefjpfngnndepjbopdmoebkipbgkggaa) 到 chrome，这是一款自动抓取订阅源的插件
4. 把点击 `view` 以后出现的 url 粘贴到 `RSSHub Radar` 设置界面的 `自定义 RSSHub 域名` 一栏。在一键订阅下使用的阅读器打勾。这样可以直接把订阅源订阅到你使用的阅读器中
5. 接下来就是快乐使用啦，我现在用的是 inoreader，注册以后，在想找订阅源的网站（比如某个b站用户的主页）点击 RSSHub，然后把订阅源传输到 inoreader 上就好了。还可以用 feedbro。

另外，有一些网站有反爬机制，我们看到的往往只是摘要，如果你使用也是 inoreader 的话，点击你想读的文章上面的这个咖啡图标，就可以爬取到全文啦。一个 RSS 阅读器如果没有爬取全文的功能，那可以说和不用 RSS 没什么两样。

<a data-fancybox="gallery" href="/20220614-rss/image-20220615003708807.png"><img src="/20220614-rss/image-20220615003708807.png" ></a>

如果不想让某篇文章被 rss 抓到的话，只需要在每篇文章设置里输入 `hiddenFromSearch: true` 就可以了

### 订阅公众号

目前有一些提供微信公众号订阅的项目或者网站，由于微信持续更新的反爬机制，有一些失效的同时又会有新的方式出现。Feeddd 目前还算好用。使用 Huginn 似乎是更好的办法，但是因为我时常阅读的公众号并不多，所以目前并没有太大的需求。

#### Feeddd

1. 在 [Feeddd 的订阅列表](https://cdn.jsdelivr.net/gh/feeddd/feeds/feeds_all_rss.txt) 中搜索你想看的公众号，然后在 URL 中复制最后的一串唯一识别码。例如 `地球知识局` 的 URL 中 https://api.feeddd.org/feeds/612f95702b6da10dfaecc477 那段 `612f95702b6da10dfaecc477`

2. 在 Inoreader 中粘贴 ` https://rsshub.app/wechat/feeddd/` + `唯一识别码`

#### CareerEngine

1. 在 [CareerEngine](https://search.careerengine.us/) 中搜索你想看的公众号，进入公众号页面后，可以在公众号的磁贴上找到 `RSS 订阅` 的链接。

2. 在 Inoreader 中粘贴这个链接的 URL

### 订阅 newsletter

订阅 newsletter 是通过 [Kill-the-Newsletter](https://kill-the-newsletter.com/) 提供虚拟邮箱地址的服务实现的。

1. 在 [Kill-the-Newsletter](https://kill-the-newsletter.com/) 中输入你想订阅的 newsletter 名称作为标记

2. 然后会生成一个虚拟的邮箱地址和一个 URL

3. 把虚拟的邮箱地址复制进你想要订阅的网站的 subscribe 框中。这一步相当于在网站中录入了这个虚拟的收件信息

4. 再把 URL 复制进 Inoreader 中，这样一来，网站的 newsletter 就会被发送到生成的虚构邮箱中，再通过 Inoreader 抓取到。

## 推荐阅读

这里推荐一些我订阅的栏目。有一部分还没有 RSS 的订阅接口，先写在这里，如果之后有开放接口或者我学会写了以后再更新接口的 url。另外，也可以参考 [RSSHub](https://docs.rsshub.app/) 的官方文档查询感兴趣的路由和网站的接口信息。

### 科技

1. [MIT 科技评论](https://www.mittrchina.com/)
   
   <img src="https://img.shields.io/badge/Status-日更-76BA99?style=flat" > `MIT Technology Review` 在中国唯一官方授权网站。关注了热榜以后让我回忆起初中一定会买的《科学美国人》杂志。读了这么多年建筑以后，我感觉很多建筑领域的论文其难懂程度远超一些生物、物理、科技方面的前沿论文，但是，在这个榜单上几乎没有建筑方面的研究报道。

2. [人人都是产品经理](http://www.woshipm.com/)
   
   <img src="https://img.shields.io/badge/Status-日更-76BA99?style=flat" > 关注这个网站并不是因为我想当产品经理（来不及了），而是发现这个站点的热门文章可以从 PM 的角度或多或少提供一些对互联网未来和当下的展望与反思。我粗浅理解的 PM 或许是互联网产业的中层枢纽，向下直达用户，向上也需要对新的热点和未来趋势有准确的判断。当然，某种程度上它的文章也有“公众号化”的趋势，这大概是简中互联网无法避免的短期未来，深度不够，广度……更是不能奢求，但好在我是外行，看什么都有意思。

3. [少数派](https://sspai.com/)
   
   <img src="https://img.shields.io/badge/Status-日更-76BA99?style=flat" > 之前经常在冲浪的时候看到过少数派的文章，有时会让我想到消失的 `好奇心日报` ，因为是作者制的网站，文章类别比较杂，推荐类文章和测评类文章比较多。

4. [阮一峰的网络日志](https://www.ruanyifeng.com/blog/)
   
   <img src="https://img.shields.io/badge/Status-周更-76BA99?style=flat" > 只遗憾没有更早知道阮老师的这个博客，他的 `科技爱好者周刊` 知识面极广，精选后的超链接又可以让我进一步了解感兴趣的话题。在很长一段时间里都会是我的良师益友。有人吐槽他的技术文章有各种各样的问题，但我认为他的知识的准确性或许值得质疑，不过归根结底，我们也不应该期望在一个个人博客里看到多么正确权威的东西，借用一句 web3 的经典表述，do your own research，通常来讲，愿意开眼看世界的人，远少于闭门造车者。

5. [HackerNoon.com](https://medium.com/hackernoon)
   
   <img src="https://img.shields.io/badge/Status-Newsletter%20available-76BA99?style=flat" > <img src="https://img.shields.io/badge/已取关-FFEA11?style=flat" > Medium 平台上的科技博主，每天更新的量非常大。有有趣的东西可以看看。已取关，推送过多，制造信息焦虑。

6. [Metaletter](https://www.metaversal.gg/metaletters)
   
   <img src="https://img.shields.io/badge/Status-Newsletter%20available-76BA99?style=flat" > 一个元宇宙方向的 Newsletter，最近停止更新了，但用 Dailyio 替代了内容，目前来看也不错

### 建筑|设计

1. [Divisare](https://divisare.com/)
   
    <img src="https://img.shields.io/badge/Status-日更-76BA99?style=flat" > 很有名的罗马的建筑杂志。

2. [afaasia](https://afasiaarchzine.com/)
   
    <img src="https://img.shields.io/badge/Status-日更-76BA99?style=flat" > 应该是西班牙的建筑网站，让我对他们很有好感的地方是他们的 RSS 分得很清晰。

3. [The Architecture Review](https://www.architectural-review.com/)
   
    <img src="https://img.shields.io/badge/Status-日更-76BA99?style=flat" > ar 应该不用介绍了。

4. [HIC](http://hicarquitectura.com/)
   
   <img src="https://img.shields.io/badge/Status-更新频率2--5篇/周-76BA99?style=flat" > <img src="https://img.shields.io/badge/已取关-FFEA11?style=flat" > 西班牙建筑博客，有些文章是西语，持续更新。但始终不能载入图片，不能满足快速浏览的目的。

5. [SUBTILITAS](https://subtilitas.tumblr.com/)
   
   <img src="https://img.shields.io/badge/Status-更新频率1--15篇/周-76BA99?style=flat" > 分享世界各地住宅案例。

6. [OfHouses](https://ofhouses.com/)
   
   <img src="https://img.shields.io/badge/Status-更新频率11--20篇/月-76BA99?style=flat" > 罗马尼亚建筑师 Daniel Tudor Munteanu 运营的网站，正如它的副标题中所写到的 "A collection of Old Forgotten Houses."，OfHouses 直到今日还在不断更新这些曝光度很低的世界各地住宅。

7. [SOCKS](https://socks-studio.com/)
   
   <img src="https://img.shields.io/badge/Status-更新频率1--3篇/月-76BA99?style=flat" > 不用多说了，SOCKS 尽管更新速度有些慢，前一阵服务器还过期了，不过发布的内容一直都很不错，谁看谁知道。

8. [Senses Atlas](https://www.sensesatlas.com/)
   
   <img src="https://img.shields.io/badge/Status-更新频率1--10篇/年-76BA99?style=flat" > 内容很丰富的设计网站，建筑、城市、cartography 等内容居多。

9. [TEXTURALITY](https://texturality.tumblr.com/post/654096609978826752/crafted-works-studio-timber-cabin-drenthe)
   
    <img src="https://img.shields.io/badge/Status-似乎停更-76BA99?style=flat" > 比较杂的建筑博客，偏向 landscape 和 craft。

10. [SSPADONI AA](https://spadoniaa.com/)
    
    <img src="https://img.shields.io/badge/Status-2021年停更-76BA99?style=flat" > Francisco Spadoni 的事务所官网，他们的设计有一种微妙的轻盈感，很喜欢。

11. [fisheye magazine](https://www.fisheyemagazine.fr/en/)
    
     <img src="https://img.shields.io/badge/Status-2021年停更-76BA99?style=flat" > 法国的线上摄影杂志。

12. [OSSO magazine](http://ossomagazine.com/)
    
     <img src="https://img.shields.io/badge/Status-2021年停更-76BA99?style=flat" > 意大利的线上设计杂志，选取的资讯风格很独特。页面基本都是意大利语，以我蹩脚的意语水平基本只能看图。

13. [Concept Model](https://conceptmodel.tumblr.com/)
    
     <img src="https://img.shields.io/badge/Status-2021年停更-76BA99?style=flat" > 分享各种建筑模型的网站。

14. [Volume64 CubeLab](https://volume64blog.com/about/)
    
    <img src="https://img.shields.io/badge/Status-2019年停更-76BA99?style=flat" > 英国一群 MArch 学生运营的 diagram 网站，只通过 4 * 4 * 4 的体积呈现一个概念化的题目。

15. [Drawing ARCHITECTURE](https://drawingarchitecture.tumblr.com/)
    
     <img src="https://img.shields.io/badge/Status-2016年停更-76BA99?style=flat" > 关注建筑表现，图纸还都挺酷的。

16. [volume control](https://volume-control.tumblr.com/)
    
     <img src="https://img.shields.io/badge/Status-2015年停更-76BA99?style=flat" > 分享体量感很强的建筑。

17. [koozArch](https://koozarch.com/)
    
    <img src="https://img.shields.io/badge/Status-Newsletter%20available-76BA99?style=flat" > 也是我经常看的网站，最近更新了一次页面风格。

18. [Monoskop](https://monoskop.org/Monoskop)
    
    <img src="https://img.shields.io/badge/Status-No%20RSS%20Feed%20yet-76BA99?style=flat" > 2004 年成立的设计平台，经常会发布一些文章和图片，官网有 RSS 订阅的链接，但是或许因为没人用，很久不更新的缘故，不能抓取到文章。

19. [Arquitectura Viva](https://arquitecturaviva.com/en)
    
    <img src="https://img.shields.io/badge/Status-No%20RSS%20Feed%20yet-76BA99?style=flat" > 也不用介绍了，在官网首页上放纪念已故建筑师栏目据我所知也只有 AV。

### 观点

1. [The Funambulist](https://thefunambulist.net/)

   <img src="https://img.shields.io/badge/Status-Newsletter%20available-76BA99?style=flat" > Activism 线上杂志，每期的选题都很有意思，pan-africanism, weaponized infrastructure, design & racism，都是我从这个杂志上了解到的。

2. [Steve说每周通讯](https://steve.hedwig.pub/)

   <img src="https://img.shields.io/badge/Status-Newsletter%20available-76BA99?style=flat" >基本每周都会更新，Steve 是一位心理咨询师，关注的内容侧重于社会学和一些时事政治的文章分享

3. [华盛顿邮报](https://www.wsj.com/news/rss-news-and-feeds)

   <img src="https://img.shields.io/badge/Status-Newsletter%20available-76BA99?style=flat" >华盛顿邮报的官方 RSS feed，分为六类，可以选择性食用。信息量很大，每个栏目一天基本会有 10+ 篇文章推送

4. [Axios AM](https://www.axios.com/newsletters)

   <img src="https://img.shields.io/badge/Status-Newsletter%20available-76BA99?style=flat" > 可以订阅日更的美国新闻 Newsletter，Mike Allen 负责内容的挑选，我比较喜欢它对于新闻本身的剖析，短小，但却指明一些重要事件的原因和它的影响。

5. [香港01](https://www.hk01.com/)

   <img src="https://img.shields.io/badge/Status-更新频率1--40 篇/日-76BA99?style=flat" >香港01是 16 年新成立的新媒体，19 年在香港的时候常在地铁上看，当时常能看到同时看到同一个事件两个完全不同角度的报道。相对来讲，属于香港中立媒体（现在呈现出亲建制和泛民记者两开花的局面），我主要关注「国际」和「中国」两个栏目，了解一下发生了什么，很粗略，但比起内地媒体还是高了一大截。可以作为一个初步的新闻筛选器，深度相当有限。

6. [纽约时报中文网](https://cn.nytimes.com/)

   <img src="https://img.shields.io/badge/Status-更新频率1--10篇/日-76BA99?style=flat" >比起 01 要更有深度，某些议题可能会刺痛一些人的心，不过这些观点需要被我们知道。[周看：从驻华记者到《纽约时报》主编](https://cn.nytimes.com/business/20220420/joseph-kahn-new-york-times/) 这篇文章讲了纽约时报中文网的诞生，和它所秉持的媒体之道。

### 其他

1. [掘火档案](https://space.bilibili.com/353238687?spm_id_from=333.337.search-card.all.click)
   
   <img src="https://img.shields.io/badge/Status-更新频率1--3篇/周-76BA99?style=flat" > 掘火的 bilibili 视频频道，大家看起来。

2. [Mountain Beltway](https://blogs.agu.org/mountainbeltway/)
   
   <img src="https://img.shields.io/badge/Status-更新频率1--5篇/月-76BA99?style=flat" > 一个地质学爱好者的个人博客，经常记录一些他在美国自然公园遇到的地质学现象。

3. [Land Before Time](https://landbeforetime.home.blog/)
   
   <img src="https://img.shields.io/badge/Status-似乎停更-76BA99?style=flat" > 从地图视角研究水文、地质和历史的关系。作者是个谷歌地图重度爱好者，还有一个 YouTube Channel: [Zero Control](https://www.youtube.com/c/ZeroControl) 来发布一些谷歌地球研究的直播视频。

4. [King Gizzard And The Lizard Wizard YouTube Channel](https://www.youtube.com/c/KingGizzardAndTheLizardWizard)
   
   <img src="https://img.shields.io/badge/Status-更新频率1--5篇/月-76BA99?style=flat" > 尽管 YouTube 的订阅十分类似 RSS 的订阅界面，按理来说不应该在 YouTube 和 RSS 阅读器重复一样的信息，但是实在太喜欢 King Gizzard and the Lizard Wizard，破个例。

## 小结

RSS 有几点显著的优点：

* 整合不同平台上的各种信息来源，减少平台切换带来的管理成本和时间成本。例如，我们可以把感兴趣的 YouTube 博主、新闻门户网站以及有趣的 newsletter 整合到一个页面中。

* 到达你眼前的信息被剥离了网站设计、广告等等内容，信息被以统一的文本+图片格式呈现。

* 为庞杂的信息增加一道筛选的关卡。信息来源从平台算法推荐的瀑布流收窄到某些被信任的博主。这就相当于从信任某个出版公司的出版书籍，到信任这个公司里某个编辑的作品，在信息流失的同时也提高了品质。

当然，RSS 不会是这个信息混乱时代的解药。尽管 RSS 被称为「互联网开放精神」的原教旨追随者，也的确解决了当下许多信息流筛选的效率问题，但它的缺陷不能被忽视。事实上，已经有用户发现了这点，例如这篇 [终于还是放下了RSS](https://ittang.com/2021/08/14/after_giving_up_the_rss_subscription/) 中，作者就指出了 RSS 几点缺陷。

* 对于不能主动筛选自己的信息来源、定期清理订阅源的人来说，RSS 并不能真正避免「回音室效应」和信息茧房。

* RSS 并不能有效帮助你的订阅方得到收益，包括但不限于广告收入、点击量和页面的反馈。

* RSS 不能在根本上改变碎片化阅读的现状。这就像把各个来源的拼图收集起来，也并不能拼凑出一个完整的图案一样，最终，我们还是需要回到严肃的学习路径上来。

## 参考文献

1. [RSSHub 的官方文档](https://docs.rsshub.app/)
2. [高效获取信息，你需要这份 RSS 入门指南](https://sspai.com/post/56391)
3. [带你走进RSS订阅，了解RSS为什么没落](https://www.douban.com/note/704272467/?_i=8238190IIok5uP)
4. [我所使用过的微信公众号文章转 RSS 的方法](https://www.zmonster.me/2020/04/17/wechat-articles-rss-solution.html)
