# Generated by Django 3.2.8 on 2022-01-27 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20220126_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='sample',
            field=models.FileField(blank=True, null=True, upload_to='book_samples/'),
        ),
    ]
