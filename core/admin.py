from django.contrib import admin, messages
from django.contrib.auth.models import User
from django.utils.translation import ngettext
from core.models import Documentation, Profile




class UserCustomAdmin(admin.ModelAdmin):
	list_display = ['username', 'email', 'is_active', 'is_staff', 'is_superuser', 'date_joined']
	list_filter = ['is_active', 'is_staff', 'is_superuser']
	search_fields = ['first_name', 'last_name', 'username', 'date_joined']
	actions = ['activate_user', 'deactivate_user', 'make_user_staff', 'remove_user_staff']

	date_hierarchy = 'date_joined'

	# def has_delete_permission(self, request, obj=None):
	# 	return False

	"""
		Add custom actions to Model `User`
	"""
	def activate_user(self, request, queryset):
		updated = queryset.update(is_active=True)
		self.message_user(request, ngettext(
				"%d user successfully activated",
				"%d users successfully activated",
				updated,
			) % updated, messages.SUCCESS)
	text = 'Activate selected users'
	activate_user.short_description = text



	def deactivate_user(self, request, queryset):
		updated = queryset.update(is_active=False)
		self.message_user(request, ngettext(
				"%d user successfully deactivated",
				"%d users successfully deactivated",
				updated,
			) % updated, messages.SUCCESS)
	text = "Deactivate selected users"
	deactivate_user.short_description = text



	def make_user_staff(self, request, queryset):
		updated = queryset.update(is_staff=True)
		self.message_user(request, ngettext(
				"%d user successfully promoted to staff",
				"%d users successfully promoted to staff",
				updated,
			) % updated, messages.SUCCESS)
	text = "Promote selected users"
	make_user_staff.short_description = text



	def remove_user_staff(self, request, queryset):
		updated = queryset.update(is_staff=False)
		self.message_user(request, ngettext(
				"%d user is no more staff",
				"%d users are no more staff",
				updated,
			) % updated, messages.SUCCESS)
	text = "Deprive selected users"
	remove_user_staff.short_description = text






class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'sex', 'date']
    list_filter = ['sex', 'date']
    search_fields = ['user__username', 'user__email', 'age', 'birth_date', 'date']

    date_hierarchy = 'date'








class DocumentationAdmin(admin.ModelAdmin):
    list_display = ['title', 'version', 'is_public', 'date', 'summary']
    list_filter = ['version', 'is_public', 'date']
    search_fields = ['description', 'summary', 'title']

    date_hierarchy = 'date'










admin.site.site_header = "Ivoire APIs "
admin.site.index_title = "Ivoire APIs "





admin.site.unregister(User)
admin.site.register(User, UserCustomAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Documentation, DocumentationAdmin)

