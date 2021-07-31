from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(max_length=150,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name="category"
        verbose_name_plural="categories"
    def get_url(self):
        return reverse("cat_prod",args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    desc=models.TextField()
    price=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    available=models.BooleanField()
    stock=models.IntegerField()
    img=models.ImageField(upload_to='products')

    def get_url(self):
        return reverse("profunction", args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)