# Generated by Django 2.1.1 on 2018-11-08 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0011_auto_20181103_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='customer',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='repository.CustomerInfo'),
            preserve_default=False,
        ),
    ]