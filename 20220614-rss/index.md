# 用RSS回到开放的互联网


<!--more-->

<img src="https://img.shields.io/badge/last%20modified-2022--06--15-ff69b4?style=flat" >   <img src="https://img.shields.io/badge/Hugo version-0.100.1-blue?style=flat" >    <img src="https://img.shields.io/badge/Status-updating-blue?style=flat" >

## Why RSS?

我经常会在失眠的夜晚，刷着小红书，痛恨大数据为我们精心策划的人生。好像我们一下子就习惯了很容易看到喜欢的内容的生活，久而久之，我都快忘记了小时候站在报刊亭前，面对着琳琅满目我从没听说过的杂志们的兴奋感。因为在哥哥家里看到《看电影》的杂志，我开始一发不可收拾地爱上看电影；因为在初中的书店偶然买到一本《Hobby Japan》，我得以一窥模型的隐秘世界，或许这也是我对会做模型的建筑系产生向往的原因之一。当然，我明白现在要接触到这些信息比那个时候要容易太多，你总可以找到无论多么冷门的电影资源，大佬们制作的做模型的视频也比比皆是。然而，什么能比得上我站在杂志店的那个充满期待和惊喜的瞬间呢？

回到正题，你们有没有发现小红书的推荐非常好训练？我经常故意折腾这个明目张胆的推荐算法。只要故意表现出对某个关键词的兴趣——比如多次打开巴哥的视频，或者常看看劝转行的流泪经验帖，小红书左上角的第一个推荐就会是同样的话题。这是在去年计划去重庆时，我从 gyw 的小红书上发现的——他的第一个推荐永远都是美女。另外一个特别好训练的是 YouTube 的人工智能，有时候，我甚至觉得我的兴趣都被它控制了，因为偶然看到一个拆鱼的视频，从那以后，我的主页上总有 [1]/[3] 的东亚海鲜市场视频。因为在这些我们熟悉的事情上耗费了太多的时间，毕竟，在选择将要做的事情上，大脑的本能的偏好占据了很重要的决策优先级。

RSS 全称是 `Really Simple Syndication` ，是一种简单易用的为用户提供信息聚合方式的格式规范。通过将想获取信息的网站的 RSS 源载入到客户端中，用户就可以在不打开网站的前提下，用阅读模式浏览文章推送，在牺牲了一些网站精美设计的同时，也让用户可以更加专注在内容上。另外，这让我们夺回了对信息源的主动权。

在搭建博客的过程中，我逐渐了解了一下 RSS 在电脑上的用法。很久之前在 `Kindle` 上用过（时代的眼泪），不过也没有坚持下来，主要是当时的信息来源也很单一，无非是知乎、豆瓣这些本身信息量就过载了的平台。而现在收集了很多 blog 以及网站之后，如何紧跟每个页面的更新，就成为一个相当有必要的内容。

## 设置流程

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

### 建筑|设计

1. [Divisare](https://divisare.com/)

    <img src="https://img.shields.io/badge/Status-日更-76BA99?style=flat" > 很有名的罗马的建筑杂志。

2. [afaasia](https://afasiaarchzine.com/)

    <img src="https://img.shields.io/badge/Status-日更-76BA99?style=flat" > 应该是西班牙的建筑网站，让我对他们很有好感的地方是他们的 RSS 分得很清晰。

3. [The Architecture Review](https://www.architectural-review.com/)

    <img src="https://img.shields.io/badge/Status-日更-76BA99?style=flat" > ar 应该不用介绍了。

1. [HIC](http://hicarquitectura.com/)

   <img src="https://img.shields.io/badge/Status-更新频率2--5篇/周-76BA99?style=flat" > 西班牙建筑博客，有些文章是西语，持续更新。

1. [SUBTILITAS](https://subtilitas.tumblr.com/)

   <img src="https://img.shields.io/badge/Status-更新频率1--15篇/周-76BA99?style=flat" > 分享世界各地住宅案例。

1. [OfHouses](https://ofhouses.com/)

   <img src="https://img.shields.io/badge/Status-更新频率11--20篇/月-76BA99?style=flat" > 罗马尼亚建筑师 Daniel Tudor Munteanu 运营的网站，正如它的副标题中所写到的 "A collection of Old Forgotten Houses."，OfHouses 直到今日还在不断更新这些曝光度很低的世界各地住宅。

1. [SOCKS](https://socks-studio.com/)

   <img src="https://img.shields.io/badge/Status-更新频率1--3篇/月-76BA99?style=flat" > 不用多说了，SOCKS 尽管更新速度有些慢，前一阵服务器还过期了，不过发布的内容一直都很不错，谁看谁知道。

3. [Senses Atlas](https://www.sensesatlas.com/)

   <img src="https://img.shields.io/badge/Status-更新频率1--10篇/年-76BA99?style=flat" > 内容很丰富的设计网站，建筑、城市、cartography 等内容居多。
   
3. [TEXTURALITY](https://texturality.tumblr.com/post/654096609978826752/crafted-works-studio-timber-cabin-drenthe)

    <img src="https://img.shields.io/badge/Status-似乎停更-76BA99?style=flat" > 比较杂的建筑博客，偏向 landscape 和 craft。
   
3. [SSPADONI AA](https://spadoniaa.com/)

   <img src="https://img.shields.io/badge/Status-2021年停更-76BA99?style=flat" > Francisco Spadoni 的事务所官网，他们的设计有一种微妙的轻盈感，很喜欢。
   
4. [fisheye magazine](https://www.fisheyemagazine.fr/en/)

    <img src="https://img.shields.io/badge/Status-2021年停更-76BA99?style=flat" > 法国的线上摄影杂志。
    
4. [OSSO magazine](http://ossomagazine.com/)

    <img src="https://img.shields.io/badge/Status-2021年停更-76BA99?style=flat" > 意大利的线上设计杂志，选取的资讯风格很独特。页面基本都是意大利语，以我蹩脚的意语水平基本只能看图。
    
13. [Concept Model](https://conceptmodel.tumblr.com/)

     <img src="https://img.shields.io/badge/Status-2021年停更-76BA99?style=flat" > 分享各种建筑模型的网站。

13. [Volume64 CubeLab](https://volume64blog.com/about/)

    <img src="https://img.shields.io/badge/Status-2019年停更-76BA99?style=flat" > 英国一群 MArch 学生运营的 diagram 网站，只通过 4 * 4 * 4 的体积呈现一个概念化的题目。

15. [Drawing ARCHITECTURE](https://drawingarchitecture.tumblr.com/)

     <img src="https://img.shields.io/badge/Status-2016年停更-76BA99?style=flat" > 关注建筑表现，图纸还都挺酷的。

16. [volume control](https://volume-control.tumblr.com/)

     <img src="https://img.shields.io/badge/Status-2015年停更-76BA99?style=flat" > 分享体量感很强的建筑。

18. [koozArch](https://koozarch.com/)

    <img src="https://img.shields.io/badge/Status-No%20RSS%20Feed%20yet-76BA99?style=flat" > 也是我经常看的网站，最近更新了一次页面风格。

19. [Monoskop](https://monoskop.org/Monoskop)

    <img src="https://img.shields.io/badge/Status-No%20RSS%20Feed%20yet-76BA99?style=flat" > 2004 年成立的设计平台，经常会发布一些文章和图片，官网有 RSS 订阅的链接，但是或许因为没人用，很久不更新的缘故，不能抓取到文章。

20. [Arquitectura Viva](https://arquitecturaviva.com/en)

    <img src="https://img.shields.io/badge/Status-No%20RSS%20Feed%20yet-76BA99?style=flat" > 也不用介绍了，在官网首页上放纪念已故建筑师栏目据我所知也只有 AV。

### 政治

1. [The Funambulist](https://thefunambulist.net/)

   <img src="https://img.shields.io/badge/Status-No%20RSS%20Feed%20yet-76BA99?style=flat" > Activism 线上杂志，每期的选题都很有意思，pan-africanism, weaponized infrastructure, design & racism，都是我从这个杂志上了解到的。

### 其他

1. [掘火](https://space.bilibili.com/353238687?spm_id_from=333.337.search-card.all.click)

   <img src="https://img.shields.io/badge/Status-更新频率1--3篇/周-76BA99?style=flat" > 掘火的 bilibili 视频频道，大家看起来。

1. [Mountain Beltway](https://blogs.agu.org/mountainbeltway/)

   <img src="https://img.shields.io/badge/Status-更新频率1--5篇/月-76BA99?style=flat" > 一个地质学爱好者的个人博客，经常记录一些他在美国自然公园遇到的地质学现象。

3. [Land Before Time](https://landbeforetime.home.blog/)

   <img src="https://img.shields.io/badge/Status-似乎停更-76BA99?style=flat" > 从地图视角研究水文、地质和历史的关系。作者是个谷歌地图重度爱好者，还有一个 YouTube Channel: [Zero Control](https://www.youtube.com/c/ZeroControl) 来发布一些谷歌地球研究的直播视频。
   
4. [King Gizzard And The Lizard Wizard YouTube Channel](https://www.youtube.com/c/KingGizzardAndTheLizardWizard)

   <img src="https://img.shields.io/badge/Status-更新频率1--5篇/月-76BA99?style=flat" > 尽管 YouTube 的订阅十分类似 RSS 的订阅界面，按理来说不应该在 YouTube 和 RSS 阅读器重复一样的信息，但是实在太喜欢 King Gizzard and the Lizard Wizard，破个例。

   

## 参考文献

1. [RSSHub 的官方文档](https://docs.rsshub.app/)
2. [高效获取信息，你需要这份 RSS 入门指南](https://sspai.com/post/56391)
