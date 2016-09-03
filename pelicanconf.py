
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Linglim'
SITENAME = "Linglim 's Blog"
#SITEURL = 'https://linglim.github.io'
SITEURL=''
DISQUS_SITENAME = '#'# 配置评论，放注册名,还没写#


TIMEZONE = 'Asia/Shanghai'
# 时间格式
DEFAULT_DATE_FORMAT = ('%Y-%m-%d(%A) %H:%M')
DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing

FEED_ALL_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# 效果是右上角有个fork me on Github，点击进入你的Github主页
# GitHub Fork Label,没生效
GITHUB_URL = u"https://github.com/linglim"
GITHUB_POSITION = "right"



# Blogroll友情链接
LINKS = (
         ('LinglimGithub', 'https://github.com/Linglim/')
         ,
         )
# menu items
MENUITEMS = [
      ('About', 'pages/about.html'),]
#CONTENT PATH
PATH = 'content'
#ARTICLE_PATHS = ['articles']
ARTICLE_URL = 'articles/{category}/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{category}/{slug}.html'


#PAGE_PATHS = ['pages']
#PAGE_URL='pages/{slug}/'
#PAGE_SAVE_AS='pages/{slug}.html'

PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

CATEGORIES_URL = 'functions/categories.html'
CATEGORIES_SAVE_AS = 'functions/categories.html'


TAGS_URL = 'functions/tags.html'
TAGS_SAVE_AS = 'functions/tags.html'

ARCHIVES_URL = 'functions/archives.html'
ARCHIVES_SAVE_AS = 'functions/archives.html'

AUTHORS_URL = 'functions/authors.html'
AUTHORS_SAVE_AS = 'functions/authors.html'


#可以显示新浪微博内容,
#~ TWITTER_USERNAME = 'farseerfc'
#~ SIDEBAR_CUSTOM = r"""
#~ <li class="nav-header"><h4><i class="icon-list-alt"></i>Weibo</h4></li>
#~ <iframe width="100%" height="550" class="share_self"  frameborder="0" scrolling="no" 
#~ src="<http://widget.weibo.com/weiboshow/index.php?language=&width=0&height=550&fansRow=1&ptype=1&speed=0&skin=2&isTitle=1&noborder=1&isWeibo=1&isFans=1&uid=1862842353&verifier=b193b9de&dpc=1>">
#~ </iframe>
#~ """

# Social widget社交连接
SOCIAL = (('LinglimGithub', 'https://github.com/Linglim'),)

DEFAULT_PAGINATION = 10#默认每一页有多少篇文章

#markdown
MD_EXTENSIONS = [
  "extra",
  "toc",
  "headerid",
  "meta",
  "sane_lists",
  "smarty",
  "wikilinks",
  "admonition",
  "codehilite(guess_lang=False,pygments_style=emacs,noclasses=True)"]
#Theme
THEME = "pelican-themes/bootstrap2"
#站长统计
CNZZ_ANALYTICS = True
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
#sitemap对爬虫友好，网站更新频率计优先级
PLUGIN_PATHS=['pelican-plugins']
PLUGINS = ['sitemap','neighbors','related_posts','global_license','summary']
#sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}
#相关文章
RELATED_POSTS_MAX=10
#content目录下任意建子目录来组织管理博客文章,这样这些目录名称就自动变成博文分类的目录了
USE_FOLDER_AS_CATEGORY = True

