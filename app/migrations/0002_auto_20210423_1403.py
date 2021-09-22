# Generated by Django 2.2.20 on 2021-04-23 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bany',
            name='hrac_id',
            field=models.ForeignKey(on_delete=None, to='app.Hraci'),
        ),
        migrations.AlterField(
            model_name='bugy',
            name='hrac_id',
            field=models.ForeignKey(on_delete=None, to='app.Hraci'),
        ),
        migrations.AlterField(
            model_name='moderovani',
            name='hrac_id',
            field=models.ForeignKey(on_delete=None, to='app.Hraci'),
        ),
        migrations.CreateModel(
            name='Typy_bugu',
            fields=[
                ('bug_id', models.IntegerField(primary_key=True, serialize=False)),
                ('nazev', models.CharField(max_length=20)),
                ('popis', models.CharField(max_length=50)),
                ('bug_typ', models.ForeignKey(on_delete=None, to='app.Bany')),
            ],
        ),
        migrations.CreateModel(
            name='Typy_banu',
            fields=[
                ('ban_id', models.IntegerField(primary_key=True, serialize=False)),
                ('nazev', models.CharField(max_length=20)),
                ('popis', models.CharField(max_length=50)),
                ('ban_typ', models.ForeignKey(on_delete=None, to='app.Bany')),
            ],
        ),
    ]
