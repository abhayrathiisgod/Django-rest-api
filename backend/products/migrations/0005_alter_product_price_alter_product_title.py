# Generated by Django 5.0.3 on 2024-04-08 05:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_alter_product_price_alter_product_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name="product",
            name="title",
            field=models.CharField(default=" Enter Your Title ", max_length=50),
        ),
    ]
