# Generated by Django 4.2.6 on 2023-10-08 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='subject',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
