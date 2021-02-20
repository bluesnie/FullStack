from django.db import models

# Create your models here.


class Table1(models.Model):
    content = models.PositiveIntegerField(verbose_name="数据内容")

    class Meta:
        verbose_name = "表1"
        verbose_name_plural = verbose_name


class Table2(models.Model):
    content = models.PositiveIntegerField(verbose_name="数据内容")

    class Meta:
        verbose_name = "表2"
        verbose_name_plural = verbose_name
