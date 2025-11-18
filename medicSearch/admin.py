from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('user', 'user__is_active', 'role', 'birth', 'specialities_list', 'addresses_list')
    list_filter = ('user__is_active',)
    readonly_fields = ('user',)
    search_fields = ('user__username',)

    fieldsets = (
        ('Usuário', {
            'fields' : ('user', 'birthday', 'image')
        }),
        ('Função', {
            'fields' : ('role',) 
        }),
        ('Extras', {
            'fields' : ('specialities', 'addresses')
        })
    )

    def birth(self, obj):
        if obj.birthday:
            return obj.birthday.strftime("%d/%m/%Y")
        
    def specialities_list(self, obj):
        return [i.name for i in obj.specialities.all()]
    
    def addresses_list(self, obj):
        return [i.name for i in obj.addresses.all()]


# Register your models here.
admin.site.register(Rating)
admin.site.register(Speciality)
admin.site.register(DayWeek)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(Profile, ProfileAdmin)
