# Generated by Django 5.1.2 on 2024-11-03 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CRQSData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('week', models.PositiveIntegerField()),
                ('hours', models.DecimalField(decimal_places=2, help_text='Total hours worked', max_digits=5)),
                ('batch_number', models.CharField(max_length=50)),
                ('assessor', models.CharField(help_text='Person responsible for assessment', max_length=100)),
                ('variant', models.CharField(max_length=50)),
                ('sku', models.CharField(help_text='Stock Keeping Unit', max_length=50, verbose_name='SKU')),
                ('issue_description', models.TextField(blank=True, null=True)),
                ('number_of_samples', models.PositiveIntegerField()),
                ('count_of_issues', models.PositiveIntegerField()),
                ('score', models.DecimalField(decimal_places=2, help_text='Quality assessment score', max_digits=5)),
                ('temperature', models.DecimalField(decimal_places=2, help_text='Temperature recorded during production', max_digits=5)),
                ('speed', models.DecimalField(decimal_places=2, help_text='Production line speed', max_digits=5)),
                ('parameter', models.CharField(help_text='Production parameter observed', max_length=50)),
                ('property', models.CharField(help_text='Production property', max_length=50)),
                ('issue', models.CharField(help_text='Specific issue identified', max_length=100)),
                ('comment', models.TextField(blank=True, help_text='Additional comments', null=True)),
            ],
            options={
                'verbose_name': 'Production Data',
                'verbose_name_plural': 'Production Data',
                'ordering': ['-date', 'batch_number'],
            },
        ),
    ]