# Generated by Django 4.0.5 on 2022-07-05 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0011_alter_darmanjo_form_information_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='darmangar',
            name='choices',
            field=models.CharField(choices=[('طلاق', 'طلاق'), ('فرزند', 'فرزند'), ('خانواده', 'خانواده')], default=1, max_length=20),
        ),
    ]