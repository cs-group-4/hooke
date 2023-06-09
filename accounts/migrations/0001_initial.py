# Generated by Django 4.2.1 on 2023-05-23 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=14)),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(max_length=100)),
                ('hostel', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('program', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=5)),
            ],
        ),
    ]
