Coffee site powered by Django
================================

Need to describe the directory structure here (use Two Scoops as reference).

Requirements
------------
All requirements files are in the "requirements" sub-directory. To install all requirements, make a new virtual environment, and then:

```
pip install -r requirements/base.txt
```

Then, sync the database (using your own local settings file):

```
python manage.py syncdb --settings=coffee_site.settings.local_yourusername
```

Add some data using previously saved fixtures:

```
python manage.py loaddata fixtures/*.json base/fixtures/*.json coffee_journal/fixtures/*.json --settings=coffee_site.settings.local_yourusername
```

Finally, you should be up and running with:

```
python manage.py runserver --settings=coffee_site.settings.local_yourusername
```
