# Generated by Django 4.2.1 on 2023-06-11 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_remove_task_categories_remove_task_completed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='quotes',
            field=models.ManyToManyField(to='main_app.quote'),
        ),
    ]
