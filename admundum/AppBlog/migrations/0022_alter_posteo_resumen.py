# Generated by Django 5.1.4 on 2025-01-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0021_delete_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='resumen',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
