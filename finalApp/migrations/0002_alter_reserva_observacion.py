# Generated by Django 4.1 on 2022-12-20 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='observacion',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
