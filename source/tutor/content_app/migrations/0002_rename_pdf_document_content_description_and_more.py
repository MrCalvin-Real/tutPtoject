# Generated by Django 4.2.6 on 2023-10-08 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PDF',
            new_name='Document',
        ),
        migrations.AddField(
            model_name='content',
            name='description',
            field=models.TextField(blank=True, max_length=400),
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
    ]
