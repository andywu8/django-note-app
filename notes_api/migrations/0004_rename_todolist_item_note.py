# Generated by Django 4.2.6 on 2023-10-17 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes_api', '0003_note_user_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='todolist',
            new_name='note',
        ),
    ]
