# Generated by Django 2.2 on 2020-04-29 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsm_config', '0015_auto_20200423_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='page',
            field=models.CharField(blank=True, choices=[['list', '列表页'], ['detail', '详情页'], ['adminConfig', '页面配置面板'], ['auto', '自定义页面'], ['chart', '自定义图表']], default='list', help_text='前端功能页面的标识', max_length=200, null=True, verbose_name='页面'),
        ),
    ]
