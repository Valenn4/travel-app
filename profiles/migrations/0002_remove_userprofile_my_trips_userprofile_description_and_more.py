# Generated by Django 4.2.3 on 2023-07-26 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='my_trips',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(default='No has seleccionado ninguna descripcion', max_length=300),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='following',
            field=models.JSONField(blank=True, default={'followings': []}),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image_portate',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image_profile',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nacionality',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('images', models.JSONField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=150)),
                ('date', models.DateTimeField(auto_now=True)),
                ('likes', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
