# Generated by Django 5.0.5 on 2024-05-11 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JobHub', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='employer_id',
            new_name='employer',
        ),
    ]
