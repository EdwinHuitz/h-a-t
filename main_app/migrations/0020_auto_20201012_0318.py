# Generated by Django 3.1.2 on 2020-10-12 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_auto_20201012_0152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listcomment',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='managercomment',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='unitcomment',
            options={'ordering': ['-date']},
        ),
    ]
