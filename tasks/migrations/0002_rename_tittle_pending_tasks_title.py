# Generated by Django 5.1.6 on 2025-02-28 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pending_tasks',
            old_name='tittle',
            new_name='title',
        ),
    ]
