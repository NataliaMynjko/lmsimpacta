# Generated by Django 2.1.7 on 2019-05-21 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0005_auto_20190520_2300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='semestre',
            new_name='semestres',
        ),
    ]
