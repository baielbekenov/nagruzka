# Generated by Django 4.1.1 on 2022-10-06 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0015_alter_groupp_praktika_nauchno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupp',
            name='priem_SRS',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Прием СРС'),
        ),
    ]
