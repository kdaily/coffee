from django.db import models

# Create your models here.

class Coffee(models.Model):
    """DB model for coffee.

    """

    name = models.CharField(max_length=500)
    roaster = models.CharField(max_length=500)
    grower = models.CharField(max_length=500, blank=True)
    finca = models.CharField(max_length=500, blank=True)
    varietal = models.CharField(max_length=200, blank=True)
    purch_location = models.CharField('Purchase location', max_length=200, blank=True)
    date_roast = models.DateField('Roast Date', blank=True)
    date_purch = models.DateField('Purchase Date', blank=True)
    amount = models.FloatField(blank=True)
    altitude = models.IntegerField(blank=True)
    notes = models.TextField(blank=True)

    def __unicode__(self):
        return "%s, %s" % (self.name, self.roaster)
