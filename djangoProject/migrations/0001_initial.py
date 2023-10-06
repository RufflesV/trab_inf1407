# Generated by Django 4.2.5 on 2023-09-29 18:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adm',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('senha', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('name', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('developer', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('administrator', models.BooleanField(default=False)),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(18)])),
                ('password', models.CharField(max_length=8)),
                ('civil_state', models.CharField(choices=[('SG', 'single'), ('MA', 'married'), ('WI', 'widow')], max_length=10)),
                ('games', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='proj.game')),
            ],
        ),
    ]
