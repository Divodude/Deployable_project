# Generated by Django 4.2.15 on 2024-09-07 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='images',
            field=models.ImageField(default='userimages\\WhatsApp_Image_2024-09-05_at_18.11.18_78db7bc0.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avater',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
