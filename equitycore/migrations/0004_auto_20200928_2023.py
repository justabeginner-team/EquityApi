# Generated by Django 3.1.1 on 2020-09-28 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equitycore', '0003_auto_20200928_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eazzypushrequest',
            name='transaction_reference',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
