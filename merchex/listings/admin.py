from django.contrib import admin

from listings.models import Band

from listings.models import Title

class BandAdmin(admin.ModelAdmin): # we insert these two lines…
    list_display = ('name', 'year_formed', 'genre') # list the fields we want on the list display

admin.site.register(Band, BandAdmin) # we edit this line, adding a second argument

class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'band', 'year', 'types')

admin.site.register(Title, TitleAdmin)
