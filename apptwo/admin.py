from django.contrib import admin
from .models import SampleApp
from .models import SampleModelTwo

# admin.site.unregister(SampleApp)
# admin.site.register(SampleModelTwo)


from django.apps import apps

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
# Register your models here.
