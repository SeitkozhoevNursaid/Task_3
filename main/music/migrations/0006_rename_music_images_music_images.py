# Generated by Django 5.0.2 on 2024-03-04 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_remove_musicimg_post_music_music_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='music_images',
            new_name='images',
        ),
    ]