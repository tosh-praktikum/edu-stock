# Generated by Django 2.2 on 2021-06-26 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210626_1115'),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='account',
        ),
        migrations.AddField(
            model_name='order',
            name='currency',
            field=models.ForeignKey(default='RUB', on_delete=django.db.models.deletion.CASCADE, related_name='buy_orders', to='stock.Currency'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='seller_account',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='sell_orders', to='accounts.Account'),
            preserve_default=False,
        ),
    ]