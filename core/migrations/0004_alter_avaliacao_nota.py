# Generated by Django 3.2.5 on 2021-07-10 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_avaliacao_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
