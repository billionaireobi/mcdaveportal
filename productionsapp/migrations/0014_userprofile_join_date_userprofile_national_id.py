# Generated by Django 5.1.2 on 2024-12-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productionsapp', '0013_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='join_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='national_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]