# Generated by Django 4.2.4 on 2023-09-01 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['pub_date']},
        ),
    ]
