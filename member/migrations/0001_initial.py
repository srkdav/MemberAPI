# Generated by Django 3.0.8 on 2020-07-07 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cust_id', models.IntegerField(primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=200, null=True)),
                ('tz', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('activity_id', models.IntegerField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now_add=True)),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='member.Customer')),
            ],
        ),
    ]
