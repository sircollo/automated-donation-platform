# Generated by Django 3.2.14 on 2022-07-11 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adp', '0002_auto_20220711_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charity',
            name='date_formed',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='charity',
            name='deadline',
            field=models.DateField(),
        ),
    ]