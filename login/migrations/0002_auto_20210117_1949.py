# Generated by Django 3.1.5 on 2021-01-17 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='user_id',
            field=models.CharField(default=False, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='loginuser',
            name='user_pw',
            field=models.CharField(default=False, max_length=256),
        ),
    ]