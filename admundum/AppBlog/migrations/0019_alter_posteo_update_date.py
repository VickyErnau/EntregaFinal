# Generated by Django 5.1.4 on 2025-01-26 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0018_remove_posteo_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
