from django.contrib import admin

from .models import Pizza, Topping, Pasta, Salad, DinnerPlatter, Sub, Addition

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
admin.site.register(Sub)
admin.site.register(Addition)