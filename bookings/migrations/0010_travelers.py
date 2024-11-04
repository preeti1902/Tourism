# Generated by Django 4.2.16 on 2024-11-04 20:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0009_alter_booking_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travelers',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('gender', models.TextField()),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travelers_info', to='bookings.booking')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
