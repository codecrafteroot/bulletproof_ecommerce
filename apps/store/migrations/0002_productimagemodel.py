# Generated by Django 4.2.4 on 2023-08-06 00:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/product/picture/', verbose_name='product image')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_images', to='store.productmodel')),
            ],
            options={
                'verbose_name': 'ProductImage',
                'verbose_name_plural': 'ProductImages',
                'db_table': 'product_image',
                'ordering': ('uuid',),
            },
        ),
    ]
