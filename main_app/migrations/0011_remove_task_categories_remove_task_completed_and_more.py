# Generated by Django 4.2.2 on 2023-06-11 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_remove_favoritequote_quote_text_favoritequote_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.DeleteModel(
            name='FavoriteQuote',
        ),
    ]
