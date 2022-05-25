from django.contrib import messages
from django.utils.translation import ngettext
from import_export.admin import ImportExportModelAdmin


class ReceipeModelAdminStuffs(ImportExportModelAdmin):
    """A class from where ``Receipe`` models admin classes inherit (especially actions)."""

    date_hierarchy = 'added_on'
    actions = ['mark_as_public', 'mark_as_private', 'mark_as_premium', 'mark_as_non_premium']
    search_fields = ['name', 'details', 'category', 'added_on',
        'ingredients__name', 'cuisine__name', 'submited__username']


    def mark_as_public(self, request, queryset):
        updated = queryset.update(is_public=True)
        self.message_user(request, ngettext(
                "%d receipe successfully published",
                "%d receipes successfully published",
                updated,
            ) % updated, messages.SUCCESS)
    mark_as_public.short_description = 'Mark selected receipes as public'



    def mark_as_private(self, request, queryset):
        updated = queryset.update(is_public=False)
        self.message_user(request, ngettext(
                "%d receipe successfully hidden",
                "%d receipes successfully hidden",
                updated,
            ) % updated, messages.SUCCESS)
    mark_as_private.short_description = 'Mark selected receipes as private'



    def mark_as_premium(self, request, queryset):
        updated = queryset.update(is_premium=False)
        self.message_user(request, ngettext(
                "%d receipe successfully marked as premium",
                "%d receipes successfully marked as premium",
                updated,
            ) % updated, messages.SUCCESS)
    mark_as_premium.short_description = 'Mark selected receipes as premium'


    def mark_as_non_premium(self, request, queryset):
        updated = queryset.update(is_premium=False)
        self.message_user(request, ngettext(
                "%d receipe successfully marked as non-premium",
                "%d receipes successfully marked as non-premium",
                updated,
            ) % updated, messages.SUCCESS)
    mark_as_non_premium.short_description = 'Mark selected receipes as non-premium'

