# Generated by Django 3.2.14 on 2022-07-13 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beneficiary',
            old_name='name',
            new_name='beneficiary_name',
        ),
    ]