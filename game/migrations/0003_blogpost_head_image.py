# Generated by Django 3.1.1 on 2020-09-24 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20200924_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='head_image',
            field=models.ImageField(default=2, upload_to='images/'),
            preserve_default=False,
        ),
    ]
