# Generated by Django 3.0.5 on 2020-04-12 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yes_no_app', '0002_auto_20191204_0613'),
    ]

    operations = [
        migrations.CreateModel(
            name='DelDb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('del_itm', models.CharField(max_length=200)),
                ('del_num', models.IntegerField(verbose_name=models.CharField(max_length=200))),
            ],
        ),
    ]
