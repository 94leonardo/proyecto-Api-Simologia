# Generated by Django 5.2.3 on 2025-06-21 04:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(max_length=100, unique=True)),
                ('magnitude', models.DecimalField(decimal_places=1, max_digits=4)),
                ('place', models.CharField(max_length=255)),
                ('time', models.DateField()),
                ('tsunami', models.BooleanField()),
                ('mag_type', models.CharField(max_length=10)),
                ('title', models.TextField()),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='sismos.feature')),
            ],
        ),
    ]
