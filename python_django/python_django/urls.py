"""python_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# 必须是django.conf.urls 下的include
from django.conf.urls import include
# from myDjango.views import index
import myDjango.views as views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^myDjango/', include("myDjango.urls" , namespace="myDjango"))
    # url(r'^test/', views.index, name="test"),
    # url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
]
