# Generated by Django 5.1 on 2024-09-15 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
