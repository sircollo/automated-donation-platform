# Generated by Django 4.0.4 on 2022-07-05 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adp', '0006_remove_donations_donor_id_donations_donor_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donations',
            name='type_of_donation',
        ),
    ]