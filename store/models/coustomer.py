from django.db import models


class coustomer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    # This function is use for saving the new coustomer information from singup page in database

    def register_user(self):
        self.save()

    # This function is Check same email address coustomer is already registered or not
    def isexist(self):
        if coustomer.objects.filter(email=self.email):
            return True
        else:
            return False
