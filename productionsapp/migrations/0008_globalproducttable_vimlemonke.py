# Generated by Django 5.1.2 on 2024-11-20 20:13

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productionsapp', '0007_rename_achieved_packingdata_achieved_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalProductTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, null=True)),
                ('hash', models.CharField(max_length=5, null=True)),
                ('batch_number', models.CharField(max_length=20, null=True)),
                ('start_time', models.TimeField(null=True)),
                ('stop_time', models.TimeField(null=True)),
                ('batch_time', models.TimeField(null=True)),
                ('whiting_quantity', models.FloatField(null=True)),
                ('whiting_batch_number', models.FloatField(null=True)),
                ('magadi_quantity', models.FloatField(null=True)),
                ('magadi_batch_number', models.FloatField(null=True)),
                ('sulphonic_acid_quantity', models.FloatField(null=True)),
                ('sulphonic_acid_batch_number', models.CharField(max_length=20, null=True)),
                ('batch_size', models.FloatField(null=True)),
                ('pressure', models.FloatField(null=True)),
                ('done_by', models.CharField(max_length=20, null=True)),
                ('checked_by', models.CharField(max_length=20, null=True)),
                ('verified_by', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VimLemonKe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tcca_quantity', models.FloatField(null=True)),
                ('tcca_batch_number', models.CharField(max_length=20, null=True)),
                ('lime_perf_quantity', models.FloatField(null=True)),
                ('lime_perf_batch_number', models.CharField(max_length=20, null=True)),
                ('global_table', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='productionsapp.globalproducttable')),
            ],
        ),
    ]