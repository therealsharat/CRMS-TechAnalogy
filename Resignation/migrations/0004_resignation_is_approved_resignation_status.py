# Generated by Django 4.0.1 on 2022-01-14 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resignation', '0003_resignation_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='resignation',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='resignation',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=25),
        ),
    ]