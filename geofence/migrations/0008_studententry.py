# Generated by Django 4.0.6 on 2022-08-03 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geofence', '0007_remove_student_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studententry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('macadd', models.CharField(max_length=200)),
            ],
        ),
    ]
