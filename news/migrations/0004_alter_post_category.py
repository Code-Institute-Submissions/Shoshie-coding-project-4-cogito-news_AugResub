# Generated by Django 3.2.12 on 2022-03-28 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Arts', 'Arts'), ('Technology', 'Technology')], max_length=250),
        ),
    ]
