# Generated by Django 2.1.1 on 2018-10-18 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181018_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bomsheet',
            name='father',
        ),
        migrations.AddField(
            model_name='bomsheet',
            name='father',
            field=models.ManyToManyField(related_name='fatherItem', to='blog.ItemSheet'),
        ),
        migrations.RemoveField(
            model_name='bomsheet',
            name='son',
        ),
        migrations.AddField(
            model_name='bomsheet',
            name='son',
            field=models.ManyToManyField(related_name='sonItem', to='blog.ItemSheet'),
        ),
    ]
