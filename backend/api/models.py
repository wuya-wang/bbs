from django.db import models
from django.contrib.auth.models import AbstractUser


# 自定义基类
class BaseModel(models.Model):
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    state = models.BooleanField(verbose_name="删除", default=True)

    class Meta:
        abstract = True


# 自定义用户字段
class User(AbstractUser):
    telephone = models.CharField(verbose_name="电话号码", max_length=20, null=True, blank=True)
    avatar = models.CharField(
        verbose_name="头像", default="/media/avatars/avatar.png", max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username


# 标签
class Tag(BaseModel):
    tag = models.CharField(verbose_name="标签", max_length=128, blank=True)

    def __str__(self):
        return self.tag

    class Meta:
        db_table = 'tag'


# 帖子
class Post(BaseModel):
    title = models.CharField(verbose_name="标题", max_length=128, blank=True)
    text = models.CharField(verbose_name="内容", max_length=512, blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "post"
