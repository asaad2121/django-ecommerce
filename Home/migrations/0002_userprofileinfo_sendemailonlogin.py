# Generated by Django 3.1.7 on 2021-03-31 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='sendEmailOnLogin',
            field=models.BooleanField(default=True),
        ),
    ]
