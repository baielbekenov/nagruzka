# Generated by Django 4.1.1 on 2022-10-07 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0022_alter_groupp_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupp',
            name='teacher',
        ),
    ]
