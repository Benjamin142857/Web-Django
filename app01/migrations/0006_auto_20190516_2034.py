# Generated by Django 2.1 on 2019-05-16 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20190516_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='username',
            field=models.CharField(default='aaa', max_length=32),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.CharField(default='333', max_length=12),
        ),
    ]