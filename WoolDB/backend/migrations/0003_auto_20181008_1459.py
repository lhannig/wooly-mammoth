# Generated by Django 2.0 on 2018-10-08 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20181005_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finishedobject',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='projectidea',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='swatch',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]