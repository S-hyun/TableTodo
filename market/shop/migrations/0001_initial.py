# Generated by Django 2.2.3 on 2019-07-10 02:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartegory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('title', models.CharField(max_length=100, verbose_name='제품명')),
                ('image', models.ImageField(upload_to='products/')),
                ('delivery', models.IntegerField(choices=[(1, '택배거래'), (2, '직거래'), (3, '택배/직거래')])),
                ('description', models.TextField(verbose_name='제품 설명')),
                ('price', models.IntegerField(verbose_name='제품 가격')),
                ('active', models.BooleanField(default=True, verbose_name='구매 가능')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category_products', to='shop.Cartegory', verbose_name='카테고리')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='my_products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
