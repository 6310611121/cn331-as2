# Generated by Django 4.1.1 on 2022-09-17 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_delete_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='year',
        ),
    ]
