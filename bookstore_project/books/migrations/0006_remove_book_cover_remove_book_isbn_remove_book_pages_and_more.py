# Generated by Django 5.1.6 on 2025-03-13 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='book',
            name='isbn',
        ),
        migrations.RemoveField(
            model_name='book',
            name='pages',
        ),
        migrations.RemoveField(
            model_name='book',
            name='published_date',
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=10),
            preserve_default=False,
        ),
    ]
