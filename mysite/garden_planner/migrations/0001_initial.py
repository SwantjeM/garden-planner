# Generated by Django 4.2.6 on 2023-10-05 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_type', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date added to DB')),
            ],
        ),
        migrations.CreateModel(
            name='Seed_inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seed_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date added to DB')),
                ('rating', models.IntegerField(default=0)),
                ('plant_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='garden_planner.plant_info')),
            ],
        ),
    ]