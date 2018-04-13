from django.db import models

# Create your models here.

# 创建数据库步骤，在项目的目录下cmd
# python manage.py makemigrations
# python manage.py migrate

# 查看创建的表结构的sql语句，myDjango为应用名称
# python manage.py sqlmigrate myDjango 0001


class Article(models.Model):

    title = models.CharField(max_length=32, default="title")
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(null=True)

    # 打印article的标题
    def __str__(self):
        return self.title
