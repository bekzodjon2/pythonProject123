# Generated by Django 5.0.1 on 2024-01-17 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lavozim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='hodim',
            name='lavozim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.lavozim'),
        ),
    ]
