# Generated by Django 3.2.21 on 2023-10-04 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
