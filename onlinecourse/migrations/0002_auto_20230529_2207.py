# Generated by Django 3.1.3 on 2023-05-29 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='content',
            new_name='choice_text',
        ),
    ]
