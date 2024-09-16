# Generated by Django 5.1 on 2024-09-15 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='created_at',
            new_name='transaction_date',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='current_value',
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='invested_value',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='total_value',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='portfolioitem',
            name='purchase_price',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='portfolioitem',
            name='quantity',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='price',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='quantity',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]
