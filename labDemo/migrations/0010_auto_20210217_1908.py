# Generated by Django 3.1.6 on 2021-02-17 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labDemo', '0009_auto_20210217_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='pjNum',
        ),
        migrations.AlterField(
            model_name='project',
            name='pjState',
            field=models.IntegerField(choices=[(0, '申请中'), (1, '申请通过'), (2, '中期检查'), (3, '结题'), (-1, '申请未通过')], default=0, verbose_name='项目状态'),
        ),
    ]
