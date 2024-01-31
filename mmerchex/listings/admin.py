from django.contrib import admin
from listings.models import Band, Prod

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')

admin.site.register(Band, BandAdmin)

class ProdAdmin(admin.ModelAdmin):
    list_display = ('title', 'prix', 'description','band')
    
admin.site.register(Prod , ProdAdmin)