# Generated by Django 3.2.7 on 2022-01-05 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logitem',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='照片'),
        ),
    ]
