# Generated by Django 2.2.7 on 2020-05-03 11:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200427_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Female'), (1, 'Male')]),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user',
            field=models.OneToOneField(on_delete='CASCADE', related_name='info', to=settings.AUTH_USER_MODEL),
        ),
    ]
