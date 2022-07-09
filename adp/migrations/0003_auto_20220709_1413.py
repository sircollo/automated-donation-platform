# Generated by Django 3.2.14 on 2022-07-09 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adp', '0002_charity_current_amount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anonymousdonation',
            options={'verbose_name_plural': 'Anonymous Donations'},
        ),
        migrations.AlterModelOptions(
            name='beneficiary',
            options={'verbose_name_plural': 'Beneficiaries'},
        ),
        migrations.AlterModelOptions(
            name='charity',
            options={'verbose_name_plural': 'Charities'},
        ),
        migrations.AlterModelOptions(
            name='donations',
            options={'verbose_name_plural': 'Donations'},
        ),
        migrations.AlterModelOptions(
            name='donor',
            options={'verbose_name_plural': 'Donors'},
        ),
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name_plural': 'Feedback'},
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name_plural': 'Posts'},
        ),
    ]
