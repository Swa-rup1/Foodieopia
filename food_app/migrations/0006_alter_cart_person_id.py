# Generated by Django 4.2.5 on 2023-09-30 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0005_order_orderitem_order_items_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='person_id',
            field=models.IntegerField(null=True),
        ),
    ]