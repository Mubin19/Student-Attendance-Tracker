# Generated by Django 4.0.6 on 2022-08-03 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geofence', '0005_alter_student_macaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classs', models.CharField(choices=[('MBA', 'MBA'), ('MCA', 'MCA')], max_length=50)),
                ('intime', models.TimeField()),
                ('outtime', models.TimeField()),
            ],
        ),
    ]
