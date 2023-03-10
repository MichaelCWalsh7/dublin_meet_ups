# Generated by Django 4.1.4 on 2022-12-18 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=254, null=True)),
                ('location', models.CharField(blank=True, max_length=254, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.CharField(max_length=24, null=True)),
                ('people', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_url', models.CharField(blank=True, max_length=254, null=True)),
                ('online', models.BooleanField(default=False)),
            ],
        ),
    ]
