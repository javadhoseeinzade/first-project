# Generated by Django 4.0.5 on 2022-07-03 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0003_darmanjo_form_information'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='darmanjo_form',
            name='rel_info',
        ),
        migrations.AddField(
            model_name='darmanjo_form',
            name='rel_info',
            field=models.ManyToManyField(to='Forms.darmangar'),
        ),
    ]