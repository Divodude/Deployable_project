# Generated by Django 4.2.15 on 2025-02-27 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foto', '0019_alter_profile_embedding'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='uploads',
        ),
        migrations.AddField(
            model_name='profile',
            name='uploads',
            field=models.ManyToManyField(blank=True, to='foto.dataset'),
        ),
    ]
