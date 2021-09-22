# Generated by Django 2.2.20 on 2021-04-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_servery_zeme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bany',
            name='typ_banu',
            field=models.ForeignKey(on_delete=None, to='app.Typy_banu'),
        ),
        migrations.AlterField(
            model_name='bugy',
            name='typ_bugu',
            field=models.ForeignKey(on_delete=None, to='app.Typy_bugu'),
        ),
        migrations.AlterField(
            model_name='typy_banu',
            name='ban_typ',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='typy_bugu',
            name='bug_typ',
            field=models.CharField(max_length=20),
        ),
    ]