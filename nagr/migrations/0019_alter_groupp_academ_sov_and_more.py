# Generated by Django 4.1.1 on 2022-10-06 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0018_alter_groupp_priem_srs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupp',
            name='academ_sov',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Академ. сов.'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='aspirantura_doctorontura',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Аспирантура, Докторантура'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='kontrol_itogovyi',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Контроль/итоговый (экзамен)'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='kontrol_tekuchiy1',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Контроль/текущий (1 контр.точка)'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='kontrol_tekuchiy2',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Контроль/текущий (2 контр.точка)'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='magistratura',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Магистратура'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='normokontr',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Нормоконтр'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='offline',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Офлайн'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='online',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Онлайн'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='praktika_nauchno',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Практика/Научно-исследовательская'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='praktika_pedagog',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Практика/Педагогическая'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='praktika_predkval',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Практика/Предквал'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='praktika_proizvod',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Практика/Производ'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='praktika_uchebnay',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Практика/Учебная'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='prochie',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Прочие'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='recenzirov_KR',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Рецениров_КР'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='rukovod_KRIKP',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Руковод.КРиКП'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='rukovodstvo_dekanatom',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Руководство деканатом'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='rukovodstvo_kafedroi',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Руководство кафедрой'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='vsego_uchebnyh_chasov',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Всего учебных часов по расчету'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='zachita_konsult',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Защита вып. квал. работы/ консульт. по разделам'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='zachita_recencirovanie',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Защита вып. квал. работы/ рецензирование'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='zachita_rukovod_VKR',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Защита вып. квал. работы/ руководство ВКР'),
        ),
        migrations.AlterField(
            model_name='groupp',
            name='zachita_uchastie_v_GAK',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Защита вып. квал. работы/ участие в ГАК'),
        ),
    ]
