# Generated by Django 4.2.3 on 2023-08-13 15:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_livingroom_nacionality'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livingroom',
            old_name='create_by',
            new_name='created_by',
        ),
        migrations.AlterField(
            model_name='livingroom',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
