from django.db import models

# Create your models here.

class Coffee(models.Model):
    """DB model for coffee.

    """

    name = models.CharField(max_length=500)
    roaster = models.CharField(max_length=500)
    grower = models.CharField(max_length=500)
    finca = models.CharField(max_length=500)
    varietal = models.CharField(max_length=200)
    date_roast = models.DateField('Roast Date', auto_now_add=True)
    date_purch = models.DateField('Purchase Date', auto_now_add=True)
    amount = models.FloatField()
