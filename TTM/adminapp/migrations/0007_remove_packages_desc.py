# Generated by Django 5.0 on 2024-03-02 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_rename_packages1_packages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packages',
            name='desc',
        ),
    ]
