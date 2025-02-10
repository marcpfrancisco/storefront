from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProductAdmin
from store.models import Product
from tags.models import TaggedItem

# Register your models here.
class TagInline(GenericTabularInline):
  autocomplete_fields = ['tag']
  min_num = 1
  max_num = 3
  model = TaggedItem
  extra = 0
  
class CustomProductAdmin(ProductAdmin):
  inlines = [TagInline]

admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)