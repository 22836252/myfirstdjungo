# Generated by Django 3.0.3 on 2020-02-19 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_post_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='brand',
            field=models.CharField(default='自有品牌', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='stock',
            field=models.IntegerField(default=0, max_length=3),
        ),
    ]
