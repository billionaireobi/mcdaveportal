# Generated by Django 5.1.2 on 2024-11-05 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productionsapp', '0002_alter_crqsdata_options_remove_crqsdata_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crqsdata',
            old_name='datetime',
            new_name='date',
        ),
    ]