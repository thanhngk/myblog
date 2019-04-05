# Generated by Django 2.1.7 on 2019-02-23 05:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='images/category/default.png', upload_to='images/category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/post/default.png', upload_to='images/post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='on_publish',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2019, 2, 23, 5, 35, 23, 181984, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/profile/default.png', upload_to='images/profile'),
        ),
    ]