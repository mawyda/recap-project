# Generated by Django 2.2 on 2019-05-07 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='summary',
            field=models.CharField(max_length=1000),
        ),
    ]