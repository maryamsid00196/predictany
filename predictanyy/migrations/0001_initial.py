# Generated by Django 4.2.4 on 2024-03-19 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YouTubeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=100)),
                ('channel_id', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('video_link', models.URLField()),
                ('channel_title', models.CharField(max_length=200)),
                ('published_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]
