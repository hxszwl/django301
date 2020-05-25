from django.db import models


# Create your models here.


class Jtsb1(models.Model):
    id = models.AutoField(primary_key=True)
    时间 = models.DateTimeField(auto_now=True)
    A相电压 = models.FloatField(default=0, null=True)
    B相电压 = models.FloatField(default=0, null=True)
    C相电压 = models.FloatField(default=0, null=True)
    A相电流 = models.FloatField(default=0, null=True)
    B相电流 = models.FloatField(default=0, null=True)
    C相电流 = models.FloatField(default=0, null=True)
    总有功电度 = models.FloatField(default=0, null=True)
    总无功电度 = models.FloatField(default=0, null=True)
    当月有功电度 = models.FloatField(default=0, null=True)
    当月无功电度 = models.FloatField(default=0, null=True)
    环境温度1 = models.FloatField(default=0, null=True)
    环境温度2 = models.FloatField(default=0, null=True)
    环境温度3 = models.FloatField(default=0, null=True)
    环境温度4 = models.FloatField(default=0, null=True)
    环境温度5 = models.FloatField(default=0, null=True)
    环境温度6 = models.FloatField(default=0, null=True)
    环境温度7 = models.FloatField(default=0, null=True)
    环境温度8 = models.FloatField(default=0, null=True)
    环境温度9 = models.FloatField(default=0, null=True)
    环境温度10 = models.FloatField(default=0, null=True)
    环境温度11 = models.FloatField(default=0, null=True)
    环境温度12 = models.FloatField(default=0, null=True)
    环境湿度1 = models.FloatField(default=0, null=True)
    环境湿度2 = models.FloatField(default=0, null=True)
    flag1 = models.IntegerField(null=True)
    flag2 = models.IntegerField(null=True)
    flag3 = models.IntegerField(null=True)
    flag4 = models.IntegerField(null=True)

    class Meta:
        db_table = 'jtsb1'

class Page_list(models.Model):
    names = models.CharField(max_length=15)
    class Meta:
        db_table = 'shebei_name1'