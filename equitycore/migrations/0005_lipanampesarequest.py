# Generated by Django 3.1.1 on 2020-09-29 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equitycore', '0004_auto_20200928_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='LipanampesaRequest',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('customer_country_code', models.CharField(max_length=2)),
                ('customer_phone_number', models.BigIntegerField(blank=True, null=True)),
                ('transaction_reference', models.CharField(max_length=20, null=True, unique=True)),
                ('transaction_date', models.DateTimeField(null=True)),
                ('transaction_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('transaction_description', models.CharField(blank=True, max_length=50, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'LipaNaMpesaOnline Requests',
                'db_table': 'tbl_lipanampesaonline_push',
            },
        ),
    ]