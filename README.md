Coffee site powered by Django
================================

Need to describe the directory structure here (use Two Scoops as reference).

Requirements
------------
All requirements files are in the "requirements" sub-directory. To install all requirements, make a new virtual environment, and then:

```
pip install -r requirements/base.txt
```

Another non-pip installable requirement is django-ratings, which has not been updated to be Django 1.5 compatible (with the custom user models).
It is a very small change, and multiple users have made it. This requirement needs to be installed from git (clone the repo and then copy the app):

```
https://github.com/deepakprakash/django-ratings
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

App Layout
------

The layout is mostly based on concepts from the "Two Scoops" Django book.

- `base` has models and views common across apps (roasters, coffees, coffee bags, etc.).
- `coffee_journal` has models and views for the coffee journal (purchased coffee bags).
- `coffee_ratio` has models and views for coffee preparation methods.
- `templates` holds all HTML templates that are rendered by views.
- `static` holds all static content - Twitter Bootstrap, JQuery, CSS stylesheets, static (non-user) images, etc.

Database
------

To support all features of django-south, we are using Postgresql 9.2.

See http://www.if-not-true-then-false.com/2012/install-postgresql-on-fedora-centos-red-hat-rhel/ for installation details.
