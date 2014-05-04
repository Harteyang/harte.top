---
layout: post
title: "Jekyll增加RSS功能"
date: 2014-05-04 21:30
categories: Blog
---

正如上一篇 [从Octopress换到Jekyll](http://blog.tankywoo.com/blog/2014/05/03/change-from-octopress-to-jekyll.html) 最后提到的，Jekyll没有RSS输出。

不过增加RSS功能并不麻烦，Github上已经有[轮子](https://github.com/snaptortoise/jekyll-rss-feeds)了。

我只使用了其中的 `feed.xml` ，其余的对我作用不大。

把这个文件放到整个Jekyll目录的根下，然后编辑`_config.yml`，增加如下字段:

	name: "Blog · Tanky Woo"
	description: "Tanky Woo's Blog, focus on Python, Linux, Gentoo, Mac OS, Vim, Open Source and so on."
	url: "http://blog.tankywoo.com"

然后在`_layouts/default.html`的`<head>`里增加:

	{% raw %}
	<link rel="alternate" type="application/rss+xml" title="{{ site.name }}" href="{{ site.url }}/feed.xml">
	{% endraw %}

增加上面一行可以使RSS阅读器找到RSS文件的位置。

然后重新生成静态输出就可以了。


