# Generated by Django 5.0.2 on 2024-10-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GlassHubApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('code', models.CharField(max_length=50)),
                ('order_id', models.IntegerField()),
            ],
        ),
    ]
