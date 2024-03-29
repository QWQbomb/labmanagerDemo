# Generated by Django 3.1.6 on 2021-03-17 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labDemo', '0010_auto_20210217_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='startTime',
            field=models.DateTimeField(null=True, verbose_name='开始时间'),
        ),
        migrations.AlterField(
            model_name='project',
            name='checkPer',
            field=models.CharField(max_length=20, verbose_name='项目检查员'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pjName',
            field=models.CharField(max_length=20, verbose_name='项目名称'),
        ),
        migrations.AlterField(
            model_name='project',
            name='remark',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='project',
            name='responPer',
            field=models.CharField(max_length=20, verbose_name='项目负责人'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='approvalPer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labDemo.user', verbose_name='批准人'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='rePer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labDemo.perinfo', verbose_name='预约人'),
        ),
    ]
