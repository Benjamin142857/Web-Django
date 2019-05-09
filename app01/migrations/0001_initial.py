# Generated by Django 2.1 on 2019-05-09 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=16)),
            ],
            options={
                'verbose_name_plural': '用户表',
            },
        ),
    ]
