from django.contrib import admin
from receipes.utils import ReceipeModelAdminStuffs
from import_export.admin import ImportExportModelAdmin
from receipes.models import Receipe, Ingredient, Cuisine
from receipes.models import PremiumReceipe, NonPremiumReceipe, PrivateReceipe
from receipes.models import PublicReceipe, SubmitedReceipe, NonSubmitedReceipe







class IngredientAdmin(ImportExportModelAdmin):
    list_display = ['name', 'quantity', 'added_on']
    list_filter = ['added_on']
    search_fields = ['name', 'quantity', 'added_on']
    
    date_hierarchy = 'added_on'






class CuisineAdmin(ImportExportModelAdmin):
    list_display = ['name', 'added_on']
    list_filter = ['added_on']
    search_fields = ['name', 'other_details', 'added_on']
    
    date_hierarchy = 'added_on'









class ReceipeAdmin(ReceipeModelAdminStuffs):
    list_display = ['name', 'category', 'cuisine', 'added_on']
    list_filter = ['is_public', 'is_premium', 'is_submited', 'added_on']
    
    
    




"""Below are proxy models admin customizations"""

class PremiumAdmin(ReceipeModelAdminStuffs):
    list_display = ['name', 'category', 'cuisine', 'is_premium', 'added_on']
    list_filter = ['is_public', 'is_submited', 'added_on']


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = Receipe.objects.filter(is_premium=True)
        return qs








class NonPremiumAdmin(ReceipeModelAdminStuffs):
    list_display = ['name', 'category', 'cuisine', 'is_premium', 'added_on']
    list_filter = ['is_public', 'is_submited', 'added_on']


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = Receipe.objects.filter(is_premium=False)
        return qs







class PrivateAdmin(ReceipeModelAdminStuffs):
    list_display = ['name', 'category', 'cuisine', 'is_public', 'added_on']
    list_filter = ['is_premium', 'is_submited', 'added_on']


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = Receipe.objects.filter(is_public=False)
        return qs







class PublicAdmin(ReceipeModelAdminStuffs):
    list_display = ['name', 'category', 'cuisine', 'is_public', 'added_on']
    list_filter = ['is_premium', 'is_submited', 'added_on']


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = Receipe.objects.filter(is_public=True)
        return qs








class SubmitedAdmin(ReceipeModelAdminStuffs):
    list_display = ['name', 'category', 'cuisine', 'is_submited', 'added_on']
    list_filter = ['is_public', 'is_premium', 'added_on']


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = Receipe.objects.filter(is_submited=True)
        return qs








class NonSubmitedAdmin(ReceipeModelAdminStuffs):
    list_display = ['name', 'category', 'cuisine', 'is_submited', 'added_on']
    list_filter = ['is_public', 'is_premium', 'added_on']


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = Receipe.objects.filter(is_submited=False)
        return qs













admin.site.register(Receipe, ReceipeAdmin)
admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(Ingredient, IngredientAdmin)

admin.site.register(PremiumReceipe, PremiumAdmin)
admin.site.register(NonPremiumReceipe, NonPremiumAdmin)

admin.site.register(PrivateReceipe, PrivateAdmin)
admin.site.register(PublicReceipe, PublicAdmin)

admin.site.register(SubmitedReceipe, SubmitedAdmin)
admin.site.register(NonSubmitedReceipe, NonSubmitedAdmin)





