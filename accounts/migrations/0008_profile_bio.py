# Generated by Django 4.1.7 on 2023-05-28 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_profile_hostel_alter_profile_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(help_text='Enter a brief description of yourself', max_length=150, null=True),
        ),
    ]
