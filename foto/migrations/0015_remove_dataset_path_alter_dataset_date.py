# Generated by Django 4.2.15 on 2024-09-21 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foto', '0014_alter_profile_avater'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='path',
        ),
        migrations.AlterField(
            model_name='dataset',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
