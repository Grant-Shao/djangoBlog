# Generated by Django 2.1.1 on 2018-10-18 12:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_auto_20181018_2008'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Articles',
            new_name='ArticleSheet',
        ),
        migrations.RenameModel(
            old_name='Comments',
            new_name='CommentSheet',
        ),
        migrations.RenameModel(
            old_name='Tags',
            new_name='TagSheet',
        ),
        migrations.RenameModel(
            old_name='Types',
            new_name='TypeSheet',
        ),
    ]
