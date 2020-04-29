from django.db import models
from django.utils.text import slugify
from api.utils import translate, get_random_string


class Category(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=512, null=True)
    slug = models.SlugField(max_length=64, blank=True, unique=True)
    # parent = models.TreeForeignKey('Category', on_delete=models.CASCADE, related_name='categories')

    def save(self, *args, **kwargs):
        if self.id is None:
            self.slug = self.create_unique_slug(self.title)
        super(Category, self).save(*args, **kwargs)

    def display_custom_fields(self):
        return None

    def create_unique_slug(self, title):
        slug = slugify(title, allow_unicode=True)
        slug = translate(slug)
        is_not_unique = Category.objects.filter(slug=slug).exists()
        while is_not_unique:
            slug += get_random_string(size=4)
            is_not_unique = Category.objects.filter(slug=slug).exists()
        return slug

    def __str__(self):
        return f'Категория {self.title}'



class CustomField(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField('Имя кастомного поля', max_length=64)
    description = models.TextField('Описание кастомного поля', blank=True)
    field_type = models.CharField('Тип кастомного поля', blank=True, default='Text', max_length=64)

class CustomFieldValue(models.Model):
    custom_field = models.ForeignKey(CustomField, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    value = models.TextField('Значение кастомного поля')