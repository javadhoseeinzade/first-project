# Generated by Django 4.0.5 on 2022-07-21 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0003_darmanjo_form_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='darmangar',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
