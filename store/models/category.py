from django.db import models

class category(models.Model):
    name = models.CharField(max_length=20)
    
    
#show all Categorys from the database
    @staticmethod
    def get_all_categorys():
        return category.objects.all()
    
        
    # show the category name
    def __str__(self):
        return self.name