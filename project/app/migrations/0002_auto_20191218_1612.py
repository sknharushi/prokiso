# Generated by Django 3.1 on 2019-12-18 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='sex',
        ),
        migrations.AddField(
            model_name='item',
            name='type',
            field=models.IntegerField(choices=[(1, '落とした'), (2, '拾った')], default=1, verbose_name='タイプ'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=30, verbose_name='品目'),
        ),
    ]
