# Generated by Django 5.0.1 on 2024-01-18 18:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0004_rename_turi_portfolio_turlari'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='Turlari',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.turi'),
        ),
    ]
