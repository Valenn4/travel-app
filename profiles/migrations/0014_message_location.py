# Generated by Django 4.2.3 on 2023-07-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_remove_message_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='location',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
