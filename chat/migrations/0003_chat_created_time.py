# Generated by Django 4.1.6 on 2023-03-02 12:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_chat_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
