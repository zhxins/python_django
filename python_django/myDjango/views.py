# *_* coding:utf8 *_*
from django.shortcuts import render
from django.http import HttpResponse

from . import models
# Create your views here.
# 执行响应的代码所在模块，逻辑处理的主要地点


def index(request):
    """跳转到主页，展示博客列表"""

    # 从数据库中获取pk=1的数据对象
    articles = models.Article.objects.all()
    # 页面跳转，往前台传值我字典类型

    return render(request, 'index.html', {"articles": articles})
    # return HttpResponse("hello,django")


def article_page(request, article_id):
    """跳转到博客详情页面"""
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'article_page.html', {"article": article})


def article_addgage(request, article_id):
    """跳转到博客新增页面"""
    if str(article_id) == '0':
        return render(request, "article_add.html")
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'article_add.html', {"article": article})


def article_add(request):
    """博客新增和修改方法，用articel_id 区分"""
    title = request.POST['title']
    content = request.POST['content']
    article_id = request.POST['article_id']
    if article_id == '0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'index.html', {"articles": articles})

    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'article_page.html', {"article": article})
