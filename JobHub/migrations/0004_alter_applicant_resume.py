# Generated by Django 5.0.5 on 2024-05-12 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobHub', '0003_applicant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='resume',
            field=models.FileField(upload_to=''),
        ),
    ]
