# Generated by Django 4.2.20 on 2025-03-08 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phnumber', models.CharField(max_length=19)),
                ('degree', models.CharField(max_length=30)),
            ],
        ),
    ]
