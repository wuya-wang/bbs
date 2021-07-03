from django.db import models
from api.models import User


# 自定义基类
class BaseModel(models.Model):
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    state = models.BooleanField(verbose_name="删除", default=True)

    class Meta:
        abstract = True


class UpLoad(BaseModel):
    file = models.FileField(verbose_name="文件", null=True)
    type = models.CharField(verbose_name="文件后缀", max_length=512, null=True, blank=True)
    filename = models.CharField(verbose_name="文件名称", max_length=512, null=True, blank=True)
    filetype = models.CharField(verbose_name="文件类型", max_length=512, null=True, blank=True)
    filesize = models.CharField(verbose_name="文件大小", max_length=512, null=True, blank=True)
    filepath = models.CharField(verbose_name="文件路径", max_length=512, null=True, blank=True)
    uploader = models.ForeignKey(verbose_name="上传者", to=User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "upload"

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        pass

