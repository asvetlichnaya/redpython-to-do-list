from django.contrib import admin

from lists.models import List, Item, Priority, Status


admin.site.register(List)
admin.site.register(Item)
admin.site.register(Priority)
admin.site.register(Status)
