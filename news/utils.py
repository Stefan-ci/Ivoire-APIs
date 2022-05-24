from django.contrib import messages
from django.utils.translation import ngettext
from import_export.admin import ImportExportModelAdmin


class ArticleModelAdminStuffs(ImportExportModelAdmin):
    """A class from where ``Article`` models admin classes inherit (especially actions)."""

    date_hierarchy = 'added_on'
    actions = ['mark_as_public', 'mark_as_private', 'mark_as_premium', 'mark_as_non_premium']
    search_fields = ['title', 'summary', 'author', 'content', 'tags', 'category', 'published_on',
        'language', 'base_url', 'website', 'added_on']


    def mark_as_public(self, request, queryset):
        updated = queryset.update(is_public=True)
        self.message_user(request, ngettext(
                "%d article successfully published",
                "%d articles successfully published",
                updated,
            ) % updated, messages.SUCCESS)
    mark_as_public.short_description = 'Mark selected articles as public'



    def mark_as_private(self, request, queryset):
        updated = queryset.update(is_public=False)
        self.message_user(request, ngettext(
                "%d article successfully hidden",
                "%d articles successfully hidden",
                updated,
            ) % updated, messages.SUCCESS)
    mark_as_private.short_description = 'Mark selected articles as private'



    def mark_as_premium(self, request, queryset):
        updated = queryset.update(is_premium=False)
        self.message_user(request, ngettext(
                "%d article successfully marked as premium",
                "%d articles successfully marked as premium",
                updated,
            ) % updated, messages.SUCCESS)
    mark_as_premium.short_description = 'Mark selected articles as premium'


    def mark_as_non_premium(self, request, queryset):
        updated = queryset.update(is_premium=False)
        self.message_user(request, ngettext(
                "%d article successfully marked as non-premium",
                "%d articles successfully marked as non-premium",
                updated,
            ) % updated, messages.SUCCESS)
    mark_as_non_premium.short_description = 'Mark selected articles as non-premium'

