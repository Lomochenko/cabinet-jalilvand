# Generated by Django 5.1.5 on 2025-02-04 13:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='عنوان دسته بندی')),
                ('photo', models.ImageField(upload_to='category/', verbose_name='عکس دسته بندی')),
                ('url_title', models.CharField(max_length=200, unique=True, verbose_name='عنوان انگلیسی در url')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, editable=False, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Products.category', verbose_name='دسته بندی والد')),
            ],
            options={
                'verbose_name': 'دسته بندی محصولات',
                'verbose_name_plural': 'دسته بندی های محصولات',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='عنوان محصول')),
                ('photo', models.ImageField(upload_to='products/', verbose_name='عکس محصول')),
                ('is_first', models.BooleanField(default=False, verbose_name='نمایش در صفحه اول')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'محصولات',
                'verbose_name_plural': 'محصولات',
                'ordering': ('id',),
            },
        ),
    ]
