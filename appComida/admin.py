from django.contrib import admin
from .models import *

# Register your models here.

# usuario admin : admin
# password admin : Superadmin

admin.site.register(Perros)
admin.site.register(Gatos)
admin.site.register(Snacks)