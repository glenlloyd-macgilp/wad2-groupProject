# Generated by Django 3.0.4 on 2020-03-20 17:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ptfinderApp', '0003_auto_20200320_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='t_username',
        ),
        migrations.AddField(
            model_name='trainer',
            name='t_account',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booking',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 20, 17, 8, 34, 358992)),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='img',
            field=models.ImageField(blank=True, default=None, upload_to='trainerProfile_images'),
        ),
        migrations.AlterField(
            model_name='trainer_comment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 20, 17, 8, 34, 358992)),
        ),
    ]