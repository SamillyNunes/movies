# Generated by Django 4.0.4 on 2022-05-11 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('zipCode', models.CharField(max_length=9)),
                ('number', models.IntegerField()),
                ('neighborhood', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MovieModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('isAvailable', models.BooleanField()),
                ('gender', models.CharField(choices=[('AN', 'Animation'), ('AC', 'Action'), ('TH', 'Thriller')], default='AN', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='PersonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('cpf', models.CharField(max_length=15)),
                ('has_debits', models.BooleanField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.addressmodel')),
                ('located_movies', models.ManyToManyField(to='api.moviemodel')),
            ],
        ),
    ]
