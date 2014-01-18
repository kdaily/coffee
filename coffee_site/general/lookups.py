from selectable.base import ModelLookup
from selectable.registry import registry


from .models import Roaster

class RoasterLookup(ModelLookup):

    model = Roaster

    search_field = 'name__icontains'

registry.register(RoasterLookup)
