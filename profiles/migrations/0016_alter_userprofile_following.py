# Generated by Django 4.2.3 on 2023-07-25 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_userprofile_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='following',
            field=models.JSONField(blank=True, default="{'following':[]}", null=True),
        ),
    ]