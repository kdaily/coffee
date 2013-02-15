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
    purch_location = models.CharField('Purchase location', max_length=200)
    date_roast = models.DateField('Roast Date')
    date_purch = models.DateField('Purchase Date')
    amount = models.FloatField()
    altitude = models.IntegerField()
    notes = models.TextField()

    def __unicode__(self):
        return "%s, %s, %s" % (self.name, self.roaster, self.finca)
