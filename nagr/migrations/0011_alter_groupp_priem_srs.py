# Generated by Django 4.1.1 on 2022-10-05 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0010_alter_groupp_amount_of_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupp',
            name='priem_SRS',
            field=models.FloatField(blank=True, null=True, verbose_name='Прием СРС'),
        ),
    ]
