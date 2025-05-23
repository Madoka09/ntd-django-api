# Generated by Django 5.2 on 2025-04-17 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('population', models.IntegerField(null=True)),
                ('terrains', models.CharField(blank=True, max_length=500, null=True)),
                ('climates', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
