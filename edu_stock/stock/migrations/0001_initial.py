# Generated by Django 2.2 on 2021-06-26 11:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('name', models.CharField(max_length=255, unique=True)),
                ('identifier', models.CharField(max_length=4, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Identifier length has to be 2-4 characters in length', regex='^\\w{2,4}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='accounts.Account')),
            ],
        ),
    ]
