# Generated by Django 2.2.28 on 2023-11-14 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_auto_20231113_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='chambre_occupee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.Chambre'),
        ),
        migrations.AlterField(
            model_name='chambre',
            name='id_chambre',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='id_client',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
