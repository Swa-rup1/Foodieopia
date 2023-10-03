# Generated by Django 4.2.5 on 2023-09-28 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0003_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.CharField(max_length=100)),
                ('collection_price', models.IntegerField()),
                ('collection_image', models.ImageField(upload_to='media/pooja_app/images/collections/')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=300)),
                ('item_price', models.IntegerField()),
                ('item_image', models.ImageField(upload_to='media/pooja_app/images/items/')),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food_app.collection')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='first', max_length=50)),
                ('lastName', models.CharField(default='last', max_length=30)),
                ('username', models.CharField(default='user', max_length=30)),
                ('password', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='cart',
            name='item_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food_app.item'),
        ),
        migrations.AddField(
            model_name='cart',
            name='person_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food_app.person'),
        ),
    ]