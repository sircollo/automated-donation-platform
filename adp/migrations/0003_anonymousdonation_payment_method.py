# Generated by Django 3.2.14 on 2022-07-07 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adp', '0002_anonymousdonation'),
    ]

    operations = [
        migrations.AddField(
            model_name='anonymousdonation',
            name='payment_method',
            field=models.CharField(default='Paypal', max_length=30),
        ),
    ]