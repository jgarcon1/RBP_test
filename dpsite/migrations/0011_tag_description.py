# Generated by Django 2.0.6 on 2018-07-26 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpsite', '0010_auto_20180726_0612'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]