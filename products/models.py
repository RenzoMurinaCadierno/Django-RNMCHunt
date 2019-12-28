from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):

    title = models.CharField(max_length=256, unique_for_date='pub_date')
    url = models.CharField(max_length=256)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/")
    icon = models.ImageField(upload_to="images/")
    body = models.TextField(max_length="2000")

    # person who submitted or hunted the product, created by Django's
    # self User class in django.contrib.auth.models module.
    # # Product will be connected to User via 'hunter' foreign key.
    # # The ID of the User hunting the product will be stored in this model.
    # # on_delete states that if the User who created this product is
    # # deleted, then all of its related Products will be deleted.
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:80] + '...'

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def get_votes(self):
        return Vote.objects.filter(product=self)


class Vote(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
