# Generated by Django 4.0.5 on 2022-07-08 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0014_choice_model_delete_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice_model',
            name='information',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Forms.info'),
        ),
    ]
