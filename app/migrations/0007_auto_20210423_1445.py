# Generated by Django 2.2.20 on 2021-04-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210423_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bany',
            name='datum_odbanovani',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moderovani',
            name='datum_odebrani_trestu',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
