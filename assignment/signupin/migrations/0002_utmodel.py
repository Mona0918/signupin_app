# Generated by Django 4.1 on 2023-04-22 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signupin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UTModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype', models.CharField(choices=[('Patient', 'PATIENT'), ('Doctor', 'DOCTOR')], default='Patient', max_length=20)),
            ],
        ),
    ]
