import csv

from unipath import Path

from base.models import Roaster, Coffee, Store

FIXTURE_ROOT = Path(__file__).ancestor(1)

roaster_file = csv.DictReader(file(FIXTURE_ROOT.child("roasters.csv")))

for roaster in roaster_file:

    for k, v in roaster.iteritems():
        if not v:
            roaster[k] = None
    
    r = Roaster(**roaster)
    r.save()


coffee_file = csv.DictReader(file(FIXTURE_ROOT.child("coffees.csv")))

for coffee in coffee_file:

    for k, v in coffee.iteritems():
        if not v:
            coffee[k] = None
    
    r = Coffee(**coffee)
    r.save()

store_file = csv.DictReader(file(FIXTURE_ROOT.child("stores.csv")))

for store in store_file:

    for k, v in store.iteritems():
        if not v:
            store[k] = None
    
    r = Store(**store)
    r.save()
