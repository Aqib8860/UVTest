# Generated by Django 3.2.10 on 2022-05-20 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_alter_city_capital'),
    ]

    operations = [
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_location', models.CharField(max_length=50)),
                ('population', models.CharField(max_length=20)),
            ],
        ),
    ]