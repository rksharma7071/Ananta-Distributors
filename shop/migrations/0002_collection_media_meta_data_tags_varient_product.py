# Generated by Django 4.2.6 on 2023-11-09 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products')),
            ],
        ),
        migrations.CreateModel(
            name='Meta_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Varient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('compare_at_price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('category', models.CharField(max_length=50)),
                ('pro_type', models.CharField(max_length=50)),
                ('vender', models.CharField(max_length=50)),
                ('collections', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.collection')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.media')),
                ('meta_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.meta_data')),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.tags')),
                ('varient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.varient')),
            ],
        ),
    ]
