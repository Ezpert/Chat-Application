# Generated by Django 4.2.6 on 2023-10-29 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_delete_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]
