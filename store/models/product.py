from django.db import models
from .category import category
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=150, default='')
    Category = models.ForeignKey(category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='products_img/')


#show all Product from the database
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    
# Show product by its category
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(Category = category_id)
        else:
            return Product.objects.all(); 