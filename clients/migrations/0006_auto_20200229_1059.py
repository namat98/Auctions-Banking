# Generated by Django 2.0 on 2020-02-29 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_acceptcleint'),
    ]

    operations = [
        migrations.AddField(
            model_name='acceptcleint',
            name='bank',
            field=models.CharField(default='Demir', max_length=100),
        ),
        migrations.AddField(
            model_name='acceptcleint',
            name='collateral',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='clients.Collateral'),
        ),
        migrations.AddField(
            model_name='acceptcleint',
            name='credit_history',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='clients.Credit_History'),
        ),
        migrations.AddField(
            model_name='acceptcleint',
            name='credit_line',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='clients.Credit_line'),
        ),
    ]
