# Generated by Django 4.1.7 on 2023-05-28 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pictures/'),
        ),
    ]
