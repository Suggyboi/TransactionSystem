# Generated by Django 3.1.4 on 2020-12-13 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_organiser',
            field=models.BooleanField(default=False),
        ),
    ]
