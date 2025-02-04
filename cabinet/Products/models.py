from django.db import models
from slugify import slugify


# Create your models here.


class Category(models.Model):
    parent = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE,
                               verbose_name='دسته بندی والد')
    title = models.CharField(max_length=200, db_index=True, verbose_name='عنوان دسته بندی')
    photo = models.ImageField(upload_to='category/', verbose_name='عکس دسته بندی')
    url_title = models.CharField(max_length=200, unique=True, verbose_name='عنوان انگلیسی در url')
    slug = models.SlugField(verbose_name='عنوان در url', blank=True, editable=False, allow_unicode=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.url_title, allow_unicode=True, separator='_')
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی محصولات'
        verbose_name_plural = 'دسته بندی های محصولات'
        ordering = ('id',)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    title = models.CharField(max_length=200, db_index=True, verbose_name='عنوان محصول')
    photo = models.ImageField(upload_to='products/', verbose_name='عکس محصول')
    is_first = models.BooleanField(default=False, verbose_name='نمایش در صفحه اول')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصولات'
        verbose_name_plural = 'محصولات'
        ordering = ('id',)
