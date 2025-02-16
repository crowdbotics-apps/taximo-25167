# Generated by Django 2.2.19 on 2021-03-21 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
        ('taxi_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField()),
                ('price', models.FloatField()),
                ('status', models.CharField(max_length=10)),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('timestamp_depart', models.DateTimeField()),
                ('timestamp_arrive', models.DateTimeField()),
                ('tip', models.FloatField(blank=True, null=True)),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookingtransaction_driver', to='taxi_profile.DriverProfile')),
                ('dropoff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookingtransaction_dropoff', to='location.MapLocation')),
                ('pickup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookingtransaction_pickup', to='location.MapLocation')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookingtransaction_user', to='taxi_profile.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_driver', to='taxi_profile.DriverProfile')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rating_user', to='taxi_profile.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='message_booking', to='booking.BookingTransaction')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_driver', to='taxi_profile.DriverProfile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_user', to='taxi_profile.UserProfile')),
            ],
        ),
    ]
