# Generated by Django 2.2.20 on 2021-04-23 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210423_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bany',
            name='datum_odbanovani',
            field=models.DateTimeField(null=True),
        ),
    ]