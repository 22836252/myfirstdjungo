from django.db import models

from django.utils import timezone

# Create your models here. 注意縮排
class Post(models.Model):
    product_category=models.CharField(max_length=200, default='A0001')
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    brand = models.CharField(max_length=200, default='自有品牌')
    image= models.CharField(max_length=200 , default='')
    image1= models.CharField(max_length=200 , default='')
    image2= models.CharField(max_length=200 , default='')
    pub_date = models.DateTimeField(default=timezone.now)
    abstract= models.CharField(max_length=200 , default='')
    price = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    stock = models.IntegerField(max_length=None , default=0)
    
    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
