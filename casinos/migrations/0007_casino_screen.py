# Generated by Django 3.1.1 on 2021-05-25 10:21

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0006_auto_20210525_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='casino',
            name='screen',
            field=easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to='upload/img/screens/', verbose_name='Screen Shot'),
        ),
    ]
