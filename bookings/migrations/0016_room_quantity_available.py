# Generated by Django 5.1.4 on 2025-01-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0015_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='quantity_available',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
