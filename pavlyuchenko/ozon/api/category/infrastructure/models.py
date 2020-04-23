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
