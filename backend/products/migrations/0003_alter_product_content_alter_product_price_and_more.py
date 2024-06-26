# Generated by Django 5.0.3 on 2024-04-03 04:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_alter_product_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="content",
            field=models.CharField(
                blank=True, default=" Enter Your Content ", max_length=50
            ),
        ),
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
