# Generated by Django 4.0.6 on 2022-08-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geofence', '0003_alter_student_division'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='macaddress',
            field=models.BigIntegerField(),
        ),
    ]
