# Generated by Django 2.0.6 on 2018-08-15 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpsite', '0016_merge_20180815_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagetext',
            name='related_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='File Upload'),
        ),
    ]
