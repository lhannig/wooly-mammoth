# Generated by Django 2.1.2 on 2018-10-23 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20181023_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='yarnshop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Yarnshop'),
        ),
    ]
