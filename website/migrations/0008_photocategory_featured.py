# Generated by Django 2.0 on 2017-12-19 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20171219_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='photocategory',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]