# Generated by Django 4.0.6 on 2022-08-03 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geofence', '0004_alter_student_macaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='macaddress',
            field=models.CharField(max_length=200),
        ),
    ]
