# Generated by Django 4.1.6 on 2023-03-02 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]