# Generated by Django 3.2.10 on 2022-05-20 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0006_auto_20220520_1213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='language2',
            old_name='language',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='language2',
            name='city',
        ),
        migrations.RemoveField(
            model_name='language2',
            name='country',
        ),
        migrations.RemoveField(
            model_name='language2',
            name='state',
        ),
        migrations.AddField(
            model_name='population2',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='language', to='apis.language2'),
        ),
    ]
