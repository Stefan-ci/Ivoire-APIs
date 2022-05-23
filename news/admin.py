from news.models import Article
from django.contrib import admin, messages
from django.utils.translation import ngettext



class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'language', 'website', 'added_on']
    list_filter = ['is_public', 'is_premium', 'is_submited', 'added_on', 'language']
    actions = ['mark_as_public', 'mark_as_private']
    search_fields = ['title', 'summary', 'author', 'content', 'tags', 'category', 'published_on',
        'language', 'base_url', 'website', 'added_on']

    date_hierarchy = 'added_on'


    # def has_delete_permission(self, request, obj=None):
    #     return False
    
    # def has_change_permission(self, request, obj=None):
    #     return False
    


    def mark_as_public(self, request, queryset):
        updated = queryset.update(is_public=True)
        self.message_user(request, ngettext(
                "%d user successfully activated",
                "%d users successfully activated",
                updated,
            ) % updated, messages.SUCCESS)
    mark_as_public.short_description = 'Mark slected articles as public'



    def mark_as_private(self, request, queryset):
        updated = queryset.update(is_public=False)
        self.message_user(request, ngettext(
                "%d user successfully activated",
                "%d users successfully activated",
                updated,
            ) % updated, messages.SUCCESS)
    mark_as_private.short_description = 'Mark slected articles as private'



admin.site.register(Article, ArticleAdmin)
