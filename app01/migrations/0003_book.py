# Generated by Django 2.1 on 2019-05-16 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_press'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('book_id', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=32)),
                ('pub_date', models.DateField()),
                ('press', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.Press')),
            ],
            options={
                'verbose_name_plural': '书籍表',
            },
        ),
    ]