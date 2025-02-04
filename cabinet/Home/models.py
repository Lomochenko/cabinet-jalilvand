from django.db import models


# Create your models here.

class FirstContent(models.Model):
    title = models.CharField(max_length=128, verbose_name='نام سایت')
    photo = models.ImageField(upload_to='logo/', verbose_name='لوگو')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'نام و لوگو'
        verbose_name_plural = 'نام و لوگو'


class AboutUs(models.Model):
    description = models.TextField(verbose_name='توضیحات مجموعه')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return f' متن  {self.id}'

    class Meta:
        verbose_name = 'درباره'
        verbose_name_plural = 'درباره ما'


class TextAnimation(models.Model):
    title = models.CharField(max_length=156, verbose_name='نام عکس')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return f' متن  {self.id}'

    class Meta:
        verbose_name = 'متن روان'
        verbose_name_plural = 'متن روان'


class Gallery(models.Model):
    title = models.CharField(max_length=128, verbose_name='نام عکس')
    photo = models.ImageField(upload_to='gallery/', verbose_name='عکس')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return f' متن  {self.id}'

    class Meta:
        verbose_name = 'گالری'
        verbose_name_plural = 'گالری ما'


class Answer(models.Model):
    question = models.CharField(max_length=256, verbose_name='پرسش')
    answer = models.TextField(verbose_name='پاسخ')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'پرسش'
        verbose_name_plural = 'پرسش و پاسخ'


class ContactUs(models.Model):
    address = models.TextField(verbose_name='آدرس')
    location = models.URLField(max_length=1024, verbose_name='لینک گوگل مپ')
    phone = models.CharField(max_length=16, verbose_name='شماره')
    instagram = models.CharField(max_length=48, verbose_name='اینستاگرام')
    whatsapp = models.URLField(max_length=256, verbose_name='لینک واتس آپ')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.instagram

    class Meta:
        verbose_name = 'راه ارتباطی'
        verbose_name_plural = 'راه ارتباطی'
