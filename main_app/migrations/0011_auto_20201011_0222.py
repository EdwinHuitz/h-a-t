# Generated by Django 3.1.2 on 2020-10-11 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20201011_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenities',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]