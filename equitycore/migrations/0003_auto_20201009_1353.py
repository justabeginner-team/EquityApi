# Generated by Django 3.1.1 on 2020-10-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equitycore', '0002_auto_20201008_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eazzypushrequest',
            name='transaction_status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]